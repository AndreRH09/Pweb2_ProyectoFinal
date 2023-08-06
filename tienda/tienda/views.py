from django.http import HTTP404
import datetime
from . import renderers

def pdf_view(self, request, *args, **kwargs):
    data = {
        'today': datetime.date.today(), 
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
    }
    return renderers.render_to_pdf('pdfs/invoice.html', data)
