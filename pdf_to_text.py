import slate
import utils

pdf=r'C:\Users\sjms1\Desktop\CTF-chal\AUCTF\Fahrenheit451\Fahrenheit451FullText.pdf'
with open(pdf, 'rb') as f:
    doc=slate.PDF(f)

f=open('text.txt',"wt")
for s in doc:
    f.write(s)

f.close()