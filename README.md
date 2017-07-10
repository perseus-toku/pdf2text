# pdf2text

This is a simply application that convert PDF files to GloVe trained vector documents


parse_pdf_to_text.py is the function to parse pdf files from a local PDF folder to a TXT Folder 
Dependencies: The pdf2text function used here is from PDFMiner:  https://pypi.python.org/pypi/pdfminer.six/20170419

To install the pretrained GloVe dataset, please refer to https://github.com/stanfordnlp/GloVe 
In this implementation, I chose the GloVe set: Wikipedia 2014 + Gigaword 5 (6B tokens, 400K vocab, uncased, 300d vectors, 822 MB download)

