# %%
import re
import pdfplumber
from pandas import DataFrame, Series, concat
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
    'Lease Tag Fee-INT',
    'Prepaid Toll Payment'
]

# %% For combined output (tags only; no lease tag fees or prepaid toll payments):
data = transactions(pages, r'\d{11} ')
df_amounts = DataFrame(data)

df_amounts['total'] = Series(df_amounts['amount'].sum())

# df_amounts.to_csv('transactions/proto_1/combined.csv', index=False)
df_amounts.to_excel('transactions/proto_1/combined.xlsx', index=False)

# %% for individual outputs:
for tag in tags:
    data = transactions(pages, tag)
    df = DataFrame(data)
    df['total'] = Series(df['amount'].sum())
    # df.to_csv(f'transactions/proto_2/{tag}.csv', index=False)
    df.to_excel(f'transactions/proto_2/{tag}.xlsx', index=False)

# %% for concatenated individual ouputs:
df_combined = DataFrame()

for tag in tags:
    data = transactions(pages, tag)
    df = DataFrame(data)
    df['total'] = Series(df['amount'].sum())
    df_combined = concat([df_combined, df], axis=1)

# df_combined.to_csv('transactions/proto_3/concatenated.csv', index=False)
df_combined.to_excel('transactions/proto_3/concatenated.xlsx', index=False)
