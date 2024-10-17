from fasthtml.common import *
from datetime import datetime
from reminder import *
import threading

# Render a quote
def render(quote):
    qid = f'quote-{quote.id}'
    delete = Button('Remove', hx_delete=f'/{quote.id}',
               hx_swap='outerHTML', style='float: right', target_id=qid)
    return Card(
                I(quote.title), 
                Br(),
                Br(display_date(quote.date), delete),
                id=qid
                )

# Returns app, router, table name, type of data in table
app, rt, quotes, Quote = fast_app('quotes.db', live=True, render=render, 
                                    id=int, title=str, date=str, pk='id')
# Home page
@rt('/')
def get():
    form = Form(Group(make_input(), Button('Add')), 
                hx_post='/', target_id='quotes-list', hx_swap='afterbegin')
    return Titled('Quotes',
                  Div(
                      form,
                      Div(*quotes(order_by='id desc'), id='quotes-list'),
                    )
                  )

# Returnable form input to clear
def make_input():
    return Input(placeholder='New quote...', id='title', hx_swap_oob='true', required=True)

# Add a quote
@rt('/')
def post(quote:Quote): # type: ignore (pylance)
    threading.Thread(target=send_quote_reminder).start()
    quote.date = get_today()
    return quotes.insert(quote), make_input()

# Delete a quote
@rt('/{qid}')
def delete(qid:int):
    quotes.delete(qid)

# Serve application
serve()

# Send reminder email in another thread
def send_quote_reminder():
    reminder_email()

# Return today's date/time in string format like 'YYYY-MM-DD HH:MM:SS.SSS'
def get_today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

# Convert date string in the form of '2024-10-16 11:53:40.816433' to a prettier string
def display_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    return date_obj.strftime('%B %d, %Y')