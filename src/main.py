import os
import shutil
import sys

from generate_page import generate_page, generate_pages_recursive


def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Deleted {destination}")
    
    os.mkdir(destination)
    print(f"Created {destination}")

    def copy_contents(src, dest):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                print(f"Copied file: {src_path} to {dest_path}")
            elif os.path.isdir(src_path):
                os.mkdir(dest_path)
                print(f"Created directory: {dest_path}")
                copy_contents(src_path, dest_path)
    
    copy_contents(source, destination)
        
def main():

    basepath = sys.argv[1] if len (sys.argv) > 1 else "/"
    print(f"Using basepath: {basepath}")

    copy_static("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath=basepath)

if __name__ == "__main__":
    main()
