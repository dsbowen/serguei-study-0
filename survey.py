"""Hemlock survey template"""

from hemlock import *

from random import choice

@route('/survey')
def Start(origin=None):
    b = Branch()
    p = Page(b)
    Label(p, label='<p>Hello World!</p>')
    return b