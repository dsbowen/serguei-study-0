"""Hemlock survey template"""

from hemlock import *

from random import shuffle

@route('/survey')
def Start(origin=None):
    b = Branch()
    
    p = Page(b)
    Label(p, label='<p>This is a consent form.</p>')
    Input(p, label='<p>Enter your MTurk ID.</p>', var='MTurkID', all_rows=True)

    p = Page(b)
    c = Check(
        p,
        label='<p>Which type of social media do you like most?</p>',
        choices=['Facebook','Twitter','Instagram'],
        var='SocialMedia'
    )
    shuffle(c.choices)
    Validate.require(c)

    p = Page(b)
    i = Input(p, label='<p>Enter your name.</p>', var='Name', all_rows=True)
    Validate.require(i)
    i = Input(p, label='<p>Enter your age.</p>', var='Age', all_rows=True)
    Validate.is_type(i, int)
    Validate.min_val(i, 0)

    p = Page(b, terminal=True)
    Label(p, label='<p>Your responses have been recorded. Your payment code is xyz.</p>')
    return b