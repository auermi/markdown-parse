# markdown-parse
Python based Markdown to HTML parser

## Usage
##### Running the script
```shell
python3 mdparse.py note.md
```
##### Current Limitations of the Parser
- Currently, the parser reads each line of your markdown one at a time so you can only use one kind of styling per line

## Markdown Spec
The initial version will be based off of the [Daring Fireball Spec](http://daringfireball.net/projects/markdown/basics)

## Supported Markdown
##### Header tags using '#' notation from \<h1\> to \<h6\>
```markdown
# H1 Title
```
##### Bold text using asterisks or underscore notation
```markdown
**Bold Text**    __Bold Text__
```
##### Italic text using asterisks or underscore notation
```markdown
*Italic text*    _Italic text_
```
##### Code blocks i.e.
```markdown
``console.log('markdown is awesome!');``
```
##### Images (Alt text, Image URL)
```markdown
![alt text here](http://thecatapi.com/?id=bsb)
```
##### Links (Link Text, Link URL)
```markdown
[View Markdown Parse on Github][https://github.com/auermi/markdown-parse]
```
