
# Shell Select - Shelect

Perform SQL-like queries on the output of CLI utilities.

## Usage

### Show formatted input

```
$ ps | shelect
      pid    tty      time      cmd
0  338644  pts/4  00:00:00     bash
1  339023  pts/4  00:00:00       ps
2  339024  pts/4  00:00:00  python3
```

### Select specific fields

```
$ ps | shelect pid, cmd
      pid      cmd
0  338644     bash
1  339046       ps
2  339047  python3
```


## Similar projects

Shelect was inspired by [Murex](https://github.com/lmorg/murex/) in [this HN discussion](https://news.ycombinator.com/item?id=30610532).

## License

GNU GPL v3

