# alcora

A lightweight disk content analyzer.

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nephyx/alcora)

## About

This small application should make it easy for you to analyze your filesystem. It's aiming to provide you brief or detailed overviews of files on your disk or functions which you can use in your applications.

Still being in early development, the features planned so far are:

- directory overview (size, file types, activity)
- listing directories by their contents
- listing files by their extensions
- listing files by dates (creation, modification, access, date range)
- listing files by size

## Usage

_alcora_ can be launched by running `main.py` with directory path argument in Python interpreter:

```
python3 main.py [directory_path]
```

By running this command, a console output with an overview of directory contents is generated.

Options for running _alcora_ will be extended soon.