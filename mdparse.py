#!/usr/local/bin/env python3

# imports
import sys
import io

def main():
    # Check if there are enough cl args and if the .md file exists and if the file is a markdown file
    if len(sys.argv) > 1:
        # if an invalid file was passed (ie not markdown)
        if (sys.argv[1][-3:] != '.md'):
            return err(0)
        try:
            with io.open(sys.argv[1]) as f:
                parse(f.readlines())
            return f.close()
        except:
            return err(1)


        # check if an html file of the same name exists
        # if so prompt user if they want to override the previous itteration of the file
        # pass contents of file to the parser code

    elif len(sys.argv) == 1:
        return err(2)
    else:
        return print('Not sure what you did yet')

def parse(md):
    # parse markdown to html
    # write to an html file of the same name
    with io.open('note.html', 'w') as f:
        for line in md:
            f.write(line)
        f.close()
    return

def err(id):
    # Not a markdown file
    if id == 0:
        return print(sys.argv[1] + ' is not a markdown file')
    # if the file just doesn't exist
    elif id == 1:
        return print(sys.argv[1] + ': this file does not exist')
    # if no file was passed
    elif id == 2:
        return print('No file was passed')

if __name__ == '__main__':
    main()
