"""E-ZPass parsing utility functions."""

import re
from collections import namedtuple
import pdfplumber
from pandas import DataFrame, Series, concat

def load_pages(file):
    """Returns a list of a pdf's pages as strings/text."""
    try:
        with pdfplumber.open(file) as pdf:
            return [page.extract_text() for page in pdf.pages]
    except:
        return []

def get_transactions(pages, search_term):
    """Returns a list of transaction tuples."""
    Transaction = namedtuple('Transaction', ['tag', 'amount'])

    tag_re = re.compile(fr'{search_term}', flags=re.IGNORECASE)
    amount_re = re.compile(r'([-\$\d,]+\.\d{2} )')

    transactions = []

    for page in pages:
        for line in page.split('\n'):
            tag = tag_re.search(line)
            amount = amount_re.search(line)
            if tag and amount:
                tag = tag.group().strip()
                amount = float(amount.group().replace('$', '').replace(',', ''))
                transactions.append(Transaction(tag, amount))

    return transactions if transactions else None

def parse(pages, tags):
    """Parses invoice for all tags and returns csv results."""
    df_combined = DataFrame()

    for tag in tags:
        data = get_transactions(pages, tag)
        if not data:
            continue
        df = DataFrame(data)
        total = round(df['amount'].sum(), 2)
        df['total'] = Series(total)
        df_combined = concat([df_combined, df], axis=1)

    return df_combined.to_csv(index=False)
