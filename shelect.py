
"""
Parse first line for field names - get the character range for each field.

Note that field names might right-aligned left-aligned or centered!

1. Determine number of fields from whitespace separated header lines.
2. Determine nuber of field separaters by columnruns (consecutive columns) with whitespace in all rows
3. If they do not match, try alternative parsing methods. Alternative parsing methods, for now, just throws an excpetion.
4. Normalize field names to lowercase then [a-z0-9-]. Beware of e.g. the `ps` command `%cpu` and `%mem` fields.
"""
