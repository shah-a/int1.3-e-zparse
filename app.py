# %%
import re
import pdfplumber

# %%
# For multiple pages:
# with pdfplumber.open("misc/examples/statement_02_25_2021.pdf") as pdf:
#     pages = pdf.pages
#     for page in pdf.pages:
#         texts = [page.extract_text() for page in pages]

# %%
# For a single page:
with pdfplumber.open("misc/examples/statement_02_25_2021.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# %%
lines = text.split('\n')

# %%
filter = re.compile(r'^((\d{2}\/){2}\d{2} )+')

# %%
for line in lines:
    if filter.match(line):
        print(line)
