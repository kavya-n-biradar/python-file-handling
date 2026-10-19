# File Modes in Python: `r`, `w` and `a`

When you open a file with `open()`, the second argument is the **mode**. It decides what you can do with the file and what happens to the existing content.

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Using `with` closes the file automatically, even if an error happens.

## Comparison

| Mode | Name | Reads? | Writes? | If the file exists | If the file does not exist |
|---|---|---|---|---|---|
| `r` | Read | Yes | No | Opens from the start | Raises `FileNotFoundError` |
| `w` | Write | No | Yes | **Erases all content**, then writes | Creates a new file |
| `a` | Append | No | Yes | Keeps content, adds to the **end** | Creates a new file |

## `r` (read)

Use it when you only need to read data and must not change the file. It is the default mode. Because the file must already exist, reading code should handle `FileNotFoundError`.

**In this project:** `read_file.py` uses `r` to read `data/input.txt` and count its words.

## `w` (write)

Use it when you want a fresh file, or want to replace everything in it. **Opening an existing file in `w` mode deletes its old content immediately**, so be careful.

**Example use:** saving a report that should be regenerated from scratch each time.

## `a` (append)

Use it when you want to keep old data and add new data at the end, such as logs, history or collected entries. Nothing already in the file is lost.

**In this project:** `write_file.py` uses `a` so that every run adds three new quotes to `data/quotes.txt` instead of overwriting the earlier ones. If it used `w`, only the quotes from the latest run would remain.

## When to use each

- Need to **read** existing data: `r`
- Need to **replace** a file completely: `w`
- Need to **add** to a file and keep what is there: `a`

## Other things to remember

- Add `"\n"` yourself when writing, because `write()` does not start a new line automatically.
- Use `encoding="utf-8"` so text with special characters works on every system.
- Handle errors such as `FileNotFoundError` and `PermissionError` with `try / except`.