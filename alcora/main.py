import sys
from os import listdir, path
from datetime import datetime

def main(directory_path):
    dir_path = str(directory_path)

    if path.isdir(dir_path):
        print("Analyzing directory " + dir_path)

        dir_contents = listdir(dir_path)

        if len(dir_contents) > 0:
            print("Items in directory: " + str(len(dir_contents)))

            for file in dir_contents:
                file_path = dir_path + "/" + file
                file_size = path.getsize(file_path)
                modification_datetime = datetime.fromtimestamp(path.getmtime(file_path))

                print(file + " (" + str(file_size) + " bytes)", end="")
                print(" [directory]" if path.isdir(file_path) else " [file]")

                print("   Modified: " + str(modification_datetime))
    else:
        print("Specified path " + dir_path + " is not a directory.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("One argument specifying directory path is required.")
