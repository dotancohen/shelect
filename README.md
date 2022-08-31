
# Shell Select - Shelect

Parse the output of unix utilities and enable SQL-like queries on that output.

## Usage

### Show formatted input

```
$ ps aux | shelect
```

### Select specific fields

```
$ ps aux | shelect pid, command
```


## Similar projects

Shelect was inspired by [Murex](https://github.com/lmorg/murex/) in [this HN discussion](https://news.ycombinator.com/item?id=30610532).

