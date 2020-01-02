"""Hemlock survey template"""

from hemlock import *

@route('/survey')
def Start(origin=None):
    b = Branch()
    p = Page(b, terminal=True)
    Label(p, label='Hello World')
    return b