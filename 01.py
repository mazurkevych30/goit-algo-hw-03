import sys
from pathlib import Path
import shutil

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка: {e}")
    return wrapper

def structure_of_directory(path: Path, output: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            structure_of_directory(element, output)
        else:
            copy_file(element, output)

def copy_file(file: Path, output) -> None:
    ext = file.suffix
    new_path: Path = output / ext
    new_path.mkdir(exist_ok=True, parents=True)
    shutil.copyfile(file, new_path / file.name)

@error_handler
def main():
    source = Path(sys.argv[1])
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("./dist")

    if source.is_dir() and source.exists():
        structure_of_directory(source, output)
    else:
        print("Помилка. Вказаний шлях не існує або він не веде до директорії")

if __name__ == "__main__":
    main()
