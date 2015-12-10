#!/usr/local/bin/env python3

# imports
import sys
import io
import os
import os.path
import webbrowser

def main():
    # Clear terminal window on osx/linux
    os.system('clear')

    # Check if there are enough cl args and if the .md file exists and if the file is a markdown file
    if len(sys.argv) > 1:
        # if an invalid file was passed (ie not markdown)
        if (sys.argv[1][-3:] != '.md'):
            return print(err(0, sys.argv[1]))
        # check if an html file of the same name exists
        elif os.path.exists(sys.argv[1][:-3] + '.html'):
            # if so prompt user if they want to override the previous itteration of the file
            will_overwrite = input('The file ' + sys.argv[1][:-3] + '.html already exists. Do you want to overwrite it? (y/n):  ')
            if will_overwrite.strip().lower() == 'y':
                try:
                    with io.open(sys.argv[1]) as f:
                        # pass contents of file to the parser code
                        parse_wrapper(f.readlines(), sys.argv[1])
                    f.close()
                    open_browser = input("Would you like to open the html file in your browser? (y/n):  ")
                    if open_browser.strip().lower() == 'y':
                        try:
                            return webbrowser.open_new_tab('file://' + os.path.realpath(sys.argv[1][:-3] + '.html'))
                        except:
                            return print(err(3, sys.argv[1][:-3] + '.html'))
                    else:
                        return
                except:
                    return print(err(1, sys.argv[1]))
            else:
                return print("Not overwriting the file. Exiting now.")
    elif len(sys.argv) == 1:
        return print(err(2))
    else:
        return print('Not sure what you did yet')

def parse_wrapper(md, filename):
    # write to an html file of the same name
    with io.open(filename[:-3] + '.html', 'w') as f:
        for line in md:
            f.write(parse(line))
    return f.close()

def parse(line):
    # parse markdown to html
    return line

def err(id, filename=None):
    # Not a markdown file
    if id == 0:
        return filename + ' is not a markdown file'
    # if the file just doesn't exist
    elif id == 1:
        return filename + ': this file does not exist'
    # if no file was passed
    elif id == 2:
        return 'No file was passed'
    elif id == 3:
        return 'Unable to open ' + filename + 'in your browser'
    else:
        return id + ' is not a valid ID'

if __name__ == '__main__':
    main()
