import sys
from os import listdir, path
from datetime import datetime

def main(directory_path):
    dir_path = str(directory_path)

    if path.isdir(dir_path):
        print("Analyzing directory " + dir_path)

        dir_contents = listdir(dir_path)

        if len(dir_contents) > 0:
            file_count = 0
            dir_count = 0

            for file in dir_contents:
                file_path = dir_path + "/" + file
                file_size = path.getsize(file_path)
                modification_datetime = datetime.fromtimestamp(path.getmtime(file_path))

                if path.isdir(file_path):
                    dir_count += 1
                elif path.isfile(file_path):
                    file_count += 1

                print(file + " (" + str(file_size) + " bytes)", end="")

                if path.isdir(file_path):
                    print(" [directory]")
                elif path.isfile(file_path):
                    print(" [file]")

                print("   Modified: " + str(modification_datetime))
            
            print(('Items in directory: {items} '
                '({dirs} directories, {files} files)') \
                .format(items=str(len(dir_contents)), dirs=str(dir_count), files=str(file_count)))
    else:
        print("Specified path " + dir_path + " is not a directory.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("One argument specifying directory path is required.")
