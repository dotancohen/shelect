
import re
import sqlite3

from collections import OrderedDict


"""
Parse first line for field names - get the character range for each field.

Note that field names might right-aligned left-aligned or centered!

1. Determine number of fields from whitespace separated header lines.
2. Determine nuber of field separaters by columnruns (consecutive columns) with whitespace in all rows
3. If they do not match, try alternative parsing methods. Alternative parsing methods, for now, just throws an excpetion.
4. Normalize field names to lowercase then [a-z0-9-]. Beware of e.g. the `ps` command `%cpu` and `%mem` fields.
"""


# $ ps | head
ps = """\
    PID TTY          TIME CMD
    526 pts/5    00:00:00 b
 256296 pts/5    00:00:00 bash
 257684 pts/5    00:00:00 ps
 257685 pts/5    00:00:00 head\
"""

ps_expected_fields = {
	"pid": [1,6],
	"tty": [8,12],
	"time": [17,24],
	"cmd": [26,29],
}



# $ ps aux | head
ps_aux = """\
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0 170240  9568 ?        Ss   Aug28   0:10 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    Aug28   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Aug28   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Aug28   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   Aug28   0:00 [netns]
root           7  0.0  0.0      0     0 ?        I<   Aug28   0:00 [kworker/0:0H-events_highpri]
root          10  0.0  0.0      0     0 ?        I<   Aug28   0:00 [mm_percpu_wq]
root          11  0.0  0.0      0     0 ?        S    Aug28   0:00 [rcu_tasks_rude_]
root          12  0.0  0.0      0     0 ?        S    Aug28   0:00 [rcu_tasks_trace]\
"""

ps_aux_expected_fields = {
	"user": [0,3],
	"pid": [13,15],
	"cpu": [17,20],
	"mem": [22,25],
	"vsz": [27,32],
	"rss": [35,38],
	"tty": [40,42],
	"stat": [49,52],
	"start": [54,58],
	"time": [62,65],
	"command": [67,95],
}



def main(cmd: str):

	lines = cmd.split("\n")
	fields = get_fields(lines)
	#print(fields) # DEBUGGING

	con = sqlite3.connect(":memory:")
	cur = con.cursor()
	create_table = "CREATE TABLE shelect (" + ",".join(fields.keys()) + ")"
	insert_stmt = "INSERT INTO shelect VALUES(" + ",".join(["?"]*len(fields)) + ")"
	cur.execute(create_table)
	con.commit()


	for line in lines[1:]:
		line_fields = []

		for name,size in fields.items():
			field_value = line[size[0]:size[1]+1].strip()
			line_fields.append(field_value)

		cur.execute(insert_stmt, line_fields)


	res = cur.execute("SELECT * FROM shelect")
	print( str(res.fetchall()) )

	res = cur.execute("SELECT pid, cmd FROM shelect")
	print( str(res.fetchall()) )

	con.close()

	return


def get_fields(cmd_lines: list) -> OrderedDict:

	width = len(max(cmd_lines, key=len))
	cols_is_space = [True]*(width+1)

	for line in cmd_lines:
		pos = 0
		for char in line:
			if char != ' ':
				cols_is_space[pos] = False
			pos += 1


	fields = OrderedDict()
	pos = 0
	in_field = False
	current_field_name = ""
	current_field_pos_begin = 0
	title_row = cmd_lines[0] + " "*(width-len(cmd_lines[0]))

	for col_is_space in cols_is_space:

		if in_field:
			if col_is_space:
				in_field = False
				field_name = re.sub("[^a-z0-9]", "", current_field_name.strip().lower())
				fields[field_name] = [current_field_pos_begin, pos-1]

			else:
				current_field_name += title_row[pos]

		else:
			if not col_is_space:
				in_field = True
				current_field_name = title_row[pos]
				current_field_pos_begin = pos

		pos += 1

	return fields


if __name__ == "__main__":
	main(ps)
	#print(ps_aux_expected_fields) # DEBUGGING
	#main(ps_aux)

