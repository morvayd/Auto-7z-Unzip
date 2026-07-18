# Auto Unzip

A simple Python utility that scans a selected folder for `.zip` and `.7z` archives and extracts each one directly into the archive's parent folder.

This version uses the system-installed 7zip executable (`7z`) rather than a Python archive package.

## Features

- Scans any folder recursively for `.zip` and `.7z` files
- Extracts each archive using the installed system 7zip app
- Unpacks directly into the archive's existing parent folder
- Works without extra Python archive dependencies

## Requirements

- Python 3
- A working 7zip executable on your `PATH`

On macOS, you can install it with Homebrew:

```bash
brew install p7zip
```

Verify the command is available:

```bash
7z
```

## Usage

1. Open a terminal in the project folder.
2. Run:

```bash
python3 auto_unzip.py
```

3. Enter the folder path you want to scan when prompted.

## Example

```bash
python3 auto_unzip.py
Enter the folder path to scan for .zip and .7z files: ~/Downloads
```

The script will search that folder recursively and extract all matching archives directly into their parent folders.

## Files

- `auto_unzip.py` — main script
- `requirements.txt` — currently empty because this app relies on the system 7zip executable

## Notes

- The script uses the system `7z` binary, so the app is lightweight and does not depend on `py7zr`.
- If `7z` is not installed or not found in `PATH`, the app will exit with a helpful error message.
