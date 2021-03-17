# %%
import re
import pdfplumber
from collections import namedtuple

# %%
Transaction = namedtuple('Transaction', ['tag', 'amount'])

# %%
example_str = '01/25/21 01/20/21 00408951196 NYSTA 25 01/20/21 24 01/20/21 23:50 BUSINESS 5H $1.35 $128.42'

# %%
tag_re = re.compile(r'\d{11}')
amount_re = re.compile(r'([\d,]+\.\d{2} )')

# %%
tag = tag_re.search(example_str)
amount = amount_re.search(example_str)

# %%
t1 = Transaction(tag, amount)
print(t1.tag)

# %% For multiple pages:
# with pdfplumber.open("misc/examples/statement_02_25_2021.pdf") as pdf:
#     pages = pdf.pages
#     for page in pdf.pages:
#         texts = [page.extract_text() for page in pages]

# %% For a single page:
with pdfplumber.open("misc/examples/statement_02_25_2021.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# %%
lines = text.split('\n')

# %%
for line in lines:
    if filter.match(line):
        print(line)
