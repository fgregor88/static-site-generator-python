from os import listdir, mkdir
from os.path import exists, isdir, isfile, join
from shutil import copy, rmtree


def main():
    path = "static/"
    target = "public/"
    clean_dir(target)
    inspect_dir(path, target)


def clean_dir(target_path: str):
    if exists(target_path):
        rmtree(target_path)
    mkdir(target_path)


def inspect_dir(src_path: str, target_path: str):
    paths = listdir(src_path)
    for path in paths:
        full_path = join(src_path, path)
        if isfile(full_path):
            target = join(target_path, full_path.replace("static/", ""))
            print(f"{path} | is a file | located at: {full_path} | copy to {target}")
            copy(full_path, target.replace(f"{path}", ""))
        elif isdir(full_path):
            target = join(target_path, full_path.replace("static/", ""))
            print(f"{path} | is a dir | located at: {full_path} | copy to {target}")
            mkdir(target)
            print(listdir("public/"))
            inspect_dir(full_path, target_path)
        else:
            print("fuck")


if __name__ == "__main__":
    main()
