import sys
from os import listdir, mkdir
from os.path import exists, isdir, isfile, join
from shutil import copy, rmtree

from markdown_blocks import generate_page


def main():

    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    print(f"base_path: {base_path}")

    path = "static/"
    target = "public/"

    if base_path != "/":
        target = "docs/"

    clean_dir(target)
    inspect_dir(path, target)

    from_path = "content/index.md"
    template_path = "template.html"

    if not exists(from_path):
        print(f"from_path doesn't exist: {from_path}")

    if not exists(template_path):
        print(f"template_path doesn't exist: {template_path}")

    # generate_page(from_path, template_path, dest_path)
    generate_pages_recursive("content", template_path, target, base_path)


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


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, base_path: str
):
    paths = listdir(dir_path_content)
    for path in paths:
        full_path = join(dir_path_content, path)
        if isfile(full_path):
            if path.endswith(".md"):
                dest_file_path = join(dest_dir_path, path[:-3] + ".html")
                generate_page(full_path, template_path, dest_file_path, base_path)
        elif isdir(full_path):
            new_dest_dir = join(dest_dir_path, path)
            if not exists(new_dest_dir):
                mkdir(new_dest_dir)
            generate_pages_recursive(full_path, template_path, new_dest_dir, base_path)


if __name__ == "__main__":
    main()
