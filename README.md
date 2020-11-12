# bib fix

_Get your LaTeX bibliography camera-ready, with one command!_

Some LaTeX styles don't ensure that the capitalization of the references' titles are preserved. By default, only the first letter is capitalized. Many bibliography sources, e.g. Google Scholar, don't wrap the rest of the capitals in {} to preserve them. This script will wrap the capital letters of the title with curly brackets. It will also produce some coherent indentation (first line not indented, the rest with four-space indent). And it will also correct the double quotation marks to the [LaTeX syntax standard](https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer) of \`\` ".

## Prerequisites

- Python3

## Usage

- Input: (path +) your bib file. 
- Output: (path +) name of the new bib file to be made (can use same name to over-write).

`python bib_fix.py [input bib file] [output bib file]`

## TODOs

- Fix single quoation marks
- Add coherent one-space-only between references
- Your suggestions in **Issues**!
