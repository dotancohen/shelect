
# Shell Select - Shelect

Wrap awk, sort, wc, and other text-processing utilities in an SQL-like syntax.

## Usage

### Show available fields

```
ps aux | shelect
```

### Select specific fields

```
ps aux | shelect COUNT(*), user GROUP BY user ORDER BY 1
```

### Select specific fields formatted for consumption by scripts

Disables header line and table borders, separates fields by nullbytes and separates lines by newlines.

```
ps aux | shelect -0 COUNT(*), user GROUP BY user ORDER BY 1
```


## Similar projects

Shelect was inspired by [Murex](https://github.com/lmorg/murex/) in [this HN discussion](https://news.ycombinator.com/item?id=30610532).

