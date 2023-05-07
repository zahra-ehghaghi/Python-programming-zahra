import zipfile
import  pathlib

def extract_archive(filepath, dest_dir):
    filepath = pathlib.Path(filepath)
    dest_dir = pathlib.Path(dest_dir)
    with zipfile.ZipFile(filepath,"r") as zip:
        zip.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("compressed.zip", "dest/")

