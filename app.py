# %%
import re
import pdfplumber
from pandas import DataFrame
from collections import namedtuple

def load_pages():
    invoice = "misc/examples/statement_02_25_2021.pdf"
    with pdfplumber.open(invoice) as pdf:
        return [page.extract_text() for page in pdf.pages]

def transactions(pages, search_term):
    Transaction = namedtuple('Transaction', ['tag', 'amount'])

    # tag_re = re.compile(r'\d{11} ')  # This line determines what the script searches for
    tag_re = re.compile(search_term)
    amount_re = re.compile(r'([\d,]+\.\d{2} )')

    transactions = []

    for page in pages:
        for line in page.split('\n'):
            tag = tag_re.search(line)
            amount = amount_re.search(line)
            if tag and amount:
                tag = tag.group().strip()
                amount = float(amount.group().replace(',', ''))
                transactions.append(Transaction(tag, amount))

    return transactions

# %%
pages = load_pages()

# %%
tags = [
    '00406214663',
    '00406293975',
    '00407040487',
    '00407041779',
    '00408951196',
    '00409181239',
    'Lease Tag'
]

# %% for individual outputs:
data_frames = []
for tag in tags:
    tag_transactions = transactions(pages, tag)
    df = DataFrame(tag_transactions)
    data_frames.append(df)
    df.to_csv(f'outputs/transactions_{tag}.csv', index=False)

# %% For combined output:
output = transactions(pages, r'\d{11} ')
df = DataFrame(output)
df.to_csv('outputs/combined.csv', index=False)
