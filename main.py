from PyPDF2 import PdfReader
import pandas as pd

# put the file path in the parentheses in this format: "C://Users//khanz//Downloads//PTHRQFCR-R67.pdf"
reader = PdfReader()
data = []
# change the range depending on where the data you're looking for is in the pdf but some data has too many lines to fit
# in excel so it may have to be done in parts
for i in range(18136, 36270):
    page = reader.pages[i]
    text = page.extract_text()
    for line in text.split("\n")[6:]:
        data.append(line)

df = pd.DataFrame(list(data))
df.to_excel(r"C:\Users\khanz\Downloads\FullPDF2.xlsx", index=False)
