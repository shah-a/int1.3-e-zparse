# %%
import re
import pdfplumber
from pandas import DataFrame
from collections import namedtuple

# %%
Transaction = namedtuple('Transaction', ['tag', 'amount'])

# %%
tag_re = re.compile(r'\d{11} ')
amount_re = re.compile(r'([\d,]+\.\d{2} )')

# %%
example_str = '01/25/21 01/20/21 00408951196 NYSTA 25 01/20/21 24 01/20/21 23:50 BUSINESS 5H $1.35 $128.42'

# %%
tag = tag_re.search(example_str).group()
amount = amount_re.search(example_str).group()

print(tag)
print(amount)

# %%
file = "misc/examples/statement_02_25_2021.pdf"
with pdfplumber.open(file) as pdf:
    pages = [page.extract_text() for page in pdf.pages]


# %%
transactions = []

for page in pages:
    for line in page.split('\n'):
        tag = tag_re.search(line)
        amount = amount_re.search(line)
        if tag and amount:
            transactions.append(Transaction(tag.group(), float(amount.group())))

amount = 0

for _ in range(len(transactions)):
    amount += transactions[_].amount

print(round(amount, 2))

# %%
df = DataFrame(transactions)
df.to_csv('results.csv', index=False)
