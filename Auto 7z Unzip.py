from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def prompt_for_folder() -> Path:
    folder_input = input("Enter the folder path to scan for .zip and .7z files: ").strip()
    if not folder_input:
        print("No folder path entered. Exiting.")
        sys.exit(1)

    folder = Path(folder_input).expanduser()
    if not folder.exists() or not folder.is_dir():
        print(f"Folder not found: {folder}")
        sys.exit(1)

    return folder


def find_archives(folder: Path) -> list[Path]:
    archives = []
    for path in folder.rglob('*'):
        if path.is_file() and path.suffix.lower() in {'.zip', '.7z'}:
            archives.append(path)
    return sorted(archives)


def get_seven_zip_executable() -> str:
    executable = shutil.which('7z') or shutil.which('7zz') or shutil.which('7za')
    if executable is None:
        raise RuntimeError("System 7zip executable not found. Install 7zip and ensure '7z' is on your PATH.")
    return executable


def extract_archive(archive_path: Path, seven_zip_executable: str) -> None:
    extract_target = archive_path.parent / f"{archive_path.stem}_extracted"
    extract_target.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(
            [seven_zip_executable, 'x', str(archive_path), f'-o{extract_target}', '-y'],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        error_output = exc.stderr.strip() or exc.stdout.strip() or 'Unknown 7zip error.'
        raise RuntimeError(f"Failed to extract {archive_path}: {error_output}") from exc

    print(f"Extracted {archive_path.suffix.upper()}: {archive_path} -> {extract_target}")


def main() -> None:
    target_folder = prompt_for_folder()

    try:
        seven_zip_executable = get_seven_zip_executable()
    except RuntimeError as exc:
        print(exc)
        sys.exit(1)

    archives = find_archives(target_folder)

    if not archives:
        print(f"No .zip or .7z files were found in: {target_folder}")
        return

    print(f"Found {len(archives)} archive(s) in {target_folder}:")
    for archive in archives:
        print(f"- {archive}")

    for archive in archives:
        extract_archive(archive, seven_zip_executable)

    print("\nAll archive files have been processed.")


if __name__ == '__main__':
    main()
