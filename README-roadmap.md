
# Shell Select - Shelect

Perform SQL-like queries on the output of CLI utilities.

## Usage

### Show formatted input

```
$ ps aux | shelect
```

### Select specific fields

```
$ ps aux | shelect pid, command
```

### Select specific fields formatted for consumption by scripts - Not yet implemented, many need to rethink this.

Disables header line and table borders, separates fields by nullbytes and separates lines by newlines.

```
$ ps aux | shelect -0 pid, command
```


## SQL Features - Not yet implemented.

Shelect uses [SQLite](https://www.sqlite.org/) under the hood, so many SQL features are available.

```
$ ps aux | shelect pid, command WHERE pid < 10000
$ ps aux | shelect pid, command WHERE command LIKE 'java%'
```

The following SQLite feature are supported, as may be others under undocumented:

* WHERE
* ORDER BY


## Similar projects

Shelect was inspired by [Murex](https://github.com/lmorg/murex/) in [this HN discussion](https://news.ycombinator.com/item?id=30610532).

