#!/usr/local/bin/env python3

# imports
import sys
import io

def main():
    # Check if there are enough cl args and if the .md file exists and if the file is a markdown file
    if len(sys.argv) > 1:
        # check if an html file of the same name exists
        # if so prompt user if they want to override the previous itteration of the file
        # pass contents of file to the parser code
        with io.open(sys.argv[1]) as f:
            parse(f.readlines())
        f.close()
    else:
        # if no file was passed
        if len(sys.argv) == 1:
            print("No file was passed")
        # if an invalid file was passed (ie not markdown)
        # if the file just doesn't exist
    return

def parse(md):
    # parse markdown to html
    # write to an html file of the same name
    with io.open('note.html', 'w') as f:
        for line in md:
            f.write(line)
        f.close()
    return

if __name__ == '__main__':
    main()
