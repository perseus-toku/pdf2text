

"""
The pdf2text function used here is from PDFMiner:  https://pypi.python.org/pypi/pdfminer.six/20170419
which is the current best implementation of dealing with page extractions 


"""

import os
import io 
import sys
import time
import shutil
import pickle
from utils import Config
#import pdf miner 
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage



def convert_pdf_to_txt(path):
  """
  Based on PDF Miner, extract the pdf file and turn it into a text file 
  """
  rsrcmgr = PDFResourceManager()
  retstr = io.StringIO()
  codec = 'utf-8'
  laparams = LAParams()
  device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
  fp = open(path, 'rb')
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  caching = True
  pagenos = set()
  for page in PDFPage.get_pages(fp, pagenos, caching=caching,check_extractable=True):
    interpreter.process_page(page)
  
  text = retstr.getvalue()
  fp.close()
  device.close()
  retstr.close()
  return text




# make surepdftotext is installed

#change the pdf reader to pdf
#if not shutil.which('PyPDF2'): # needs Python 3.3+
 # print('ERROR: you don\'t have pdftotext installed. Install it first before calling this script')
  #sys.exit()
if not os.path.exists(Config.txt_dir):
  print('creating ', Config.txt_dir)
  os.makedirs(Config.txt_dir)

have = set(os.listdir(Config.txt_dir))
files = os.listdir(Config.pdf_dir)
print(files)



for i,f in enumerate(files): # there was a ,start=1 here that I removed, can't remember why it would be there. shouldn't be, i think.
  if not f.endswith(".pdf"):  #check if the current file is a pdf file 
    continue 
  txt_basename = f.replace(".pdf","") + '.txt' # remove .pdf from the name
  
  if txt_basename in have:
    print('%d/%d skipping %s, already exists.' % (i, len(files), txt_basename, ))
    continue

  pdf_path = os.path.join(Config.pdf_dir, f)
  txt_path = os.path.join(Config.txt_dir, txt_basename)
  # convert a PDF file to txt 
  text =convert_pdf_to_txt(pdf_path) 
  os.system('touch ' + txt_path)
  print("creating file: ",txt_basename)

  txtfile = open(txt_path,'w') 
  txtfile.write(text)
  txtfile.close()


  # check output was made
  #if not os.path.isfile(txt_path):
    # there was an error with converting the pdf
  #  print('there was a problem with parsing %s to text, creating an empty text file.' % (pdf_path, ))
  #  os.system('touch ' + txt_path) # create empty file, but it's a record of having tried to convert

  time.sleep(0.01) # silly way for allowing for ctrl+c termination







