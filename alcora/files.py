from os import listdir, path

def count_by_extension(dir_path: str, ext: str) -> int:
    """
    Count files with a specific file extension in a directory.
    """
    if path.isdir(dir_path):
        dir_contents = listdir(dir_path)
        count = 0

        if len(dir_contents) > 0:
            for file in dir_contents:
                if path.isfile(path.join(dir_path, file)) and path.splitext(file)[1] == ext.casefold():
                    count += 1
        else:
            return 0
        
        return count
    else:
        return 0
