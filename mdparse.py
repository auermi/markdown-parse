#!/usr/local/bin/env python3

# imports
import sys
import io
import os
import os.path

def main():
    # Clear terminal window on osx/linux
    os.system('clear')
    
    # Check if there are enough cl args and if the .md file exists and if the file is a markdown file
    if len(sys.argv) > 1:
        # if an invalid file was passed (ie not markdown)
        if (sys.argv[1][-3:] != '.md'):
            return err(0)
        # check if an html file of the same name exists
        elif os.path.exists(sys.argv[1][:-3] + '.html'):
            # if so prompt user if they want to override the previous itteration of the file
            will_overwrite = input('The file ' + sys.argv[1][:-3] + '.html already exists. Do you want to overwrite it? (y/n):  ')
            if will_overwrite.strip().lower() == 'y':
                try:
                    with io.open(sys.argv[1]) as f:
                        # pass contents of file to the parser code
                        parse(f.readlines())
                    return f.close()
                except:
                    return err(1)
            else:
                return print("Not overwriting the file. Exiting now.")

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
