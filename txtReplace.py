#!/usr/bin/env python2
import os
import re
import sys


def generate_file_list(source, filetype=".txt"):
    files = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filter(lambda s: s.endswith(filetype), filenames):
            files.append(os.path.join(root, filename))
    return files


def find_replace(files, find, replace):
    count = 0
    find, replace = map(re.escape, [find, replace])
    for textfile in files:
        with open(textfile, 'r') as f:
           content, count = re.subn(find, replace, f.read())
        with open(textfile, 'w') as f:
            f.write(content)
    return count


def main():
    try:
        scriptname, source, filetype, find, replace = sys.argv
    except Exception as e:
        print "Invalid arguments passed. Usage:\n\t txtReplace.py <source-path> <file-type> <find-argument> <replace-argument>"
        sys.exit()
    
    fileList = generate_file_list(source, filetype)
    print fileList
    changeCount = find_replace(fileList, find, replace)
    print "Replaced %s occurences of %s in %s" % (str(changeCount), find, source)

if __name__ == "__main__":
    main()
