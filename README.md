# Python File Handling

A beginner Python project for the CodeMore Python Programming Internship (Week 1, Task 3). It reads data from a text file, writes and appends user input to a new file, and explains the difference between the `r`, `w` and `a` file modes.

## Project Structure

```
python-file-handling/
├── README.md
├── src/
│   ├── read_file.py
│   └── write_file.py
├── docs/
│   └── file_modes.md
├── data/
│   ├── input.txt
│   └── quotes.txt
└── assets/
    └── screenshots/
```

## Requirements

- Python 3.8 or newer. No external libraries.

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-file-handling.git
cd python-file-handling
```

**1. Read and analyze a text file**
```bash
python src/read_file.py
```
Reads `data/input.txt` and prints the word, line and character counts. If the file is missing, it prints a friendly error message instead of crashing. To try another file:
```bash
python src/read_file.py data/missing.txt
```

**2. Write and append quotes**
```bash
python src/write_file.py
```
Asks for three favorite quotes and appends them to `data/quotes.txt`, one per line. Run it several times, and each run adds to the file without overwriting earlier quotes.

## Documentation

[`docs/file_modes.md`](docs/file_modes.md) explains the differences between the `r`, `w` and `a` modes and when to use each. Screenshots of both scripts and the generated files are in [`assets/screenshots/`](assets/screenshots/).

## What I Learned

- How to read a file with `open()` in `r` mode and process its text
- How to handle `FileNotFoundError` and other file errors with `try / except`
- How `w` replaces a file, `a` adds to it, and why append mode keeps data between runs
- Why `with open(...)` is the safest way to open files
- How to organise a project into `src`, `docs`, `data` and `assets` folders

## Author

Kavya Biradar