import pypandoc
import os
import re

def convert_md_to_rst():
    filtered = pypandoc.convert('README.md', 'rst')
    f = open('README', 'w+')
    f.write(filtered)
    f.close()

convert_md_to_rst()