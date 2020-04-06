import slate
import utils

pdf='pdf_file'
with open(pdf, 'rb') as f:
    doc=slate.PDF(f)

f=open('text.txt',"wt")
for s in doc:
    f.write(s)

f.close()
