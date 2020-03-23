"""Hemlock survey template"""

from hemlock import *

from flask import render_template

from random import shuffle

# Number of pages in the study
N_PAGES = 2
# Grocerty items
ITEMS = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberry']
# Range of prices
PRICES = list(range(1,len(ITEMS)+1))

@route('/survey')
def Start(origin=None):
    b = Branch()
    [gen_page(b) for i in range(N_PAGES)]
    p = Page(b, terminal=True)
    Label(p, label='<p>Thank you for completing the study!</p>')
    return b

def gen_page(branch):
    # Generates a grocery item page
    p = Page(branch)
    p.timer.var = 'CompletionTime'
    prices = PRICES.copy()
    shuffle(prices)
    slider_ids = [gen_range(p, i, price) for i, price in zip(ITEMS, prices)]
    slider_info = zip(slider_ids, prices)
    # check_responses.js checks if all sliders are correct
    # if so, it makes the submit button visible
    p.add_internal_js(
        render_template('check_responses.js', 
        slider_info=slider_info)
    )

    # Displays time to submit gocery item page
    display_page = Page(branch)
    l = Label(display_page)
    Compile.display_response_time(l, p.timer)

def gen_range(page, item, price):
    # Generate a range slider for a single grocerty item
    r = Range(
        page, 
        label='<p>{0} ${1}'.format(item, price), 
        min=0, max=len(ITEMS)+1, step=.1, default=0
    )
    # range.js triggers a check to see if all sliders are correct
    r.add_internal_js(render_template('slider.js', range_id=r.model_id))
    return r.model_id

@Compile.register
def display_response_time(label, timer):
    # Create a label with the response time from the grocerty page
    label.label = '<p>Your response took {0:.1f} seconds.</p>'.format(timer.data)
