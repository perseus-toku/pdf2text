import os 
import pickle
#import numpy as np
from utils import Config, safe_pickle_dump


max_train = 5000 # max number of tfidf training documents (chosen randomly), for memory efficiency

#first navigate to the txt folder 
txt_path = Config.txt_dir 
txt_files = os.listdir(txt_path)
print(txt_files)
glove_path = Config.glove_path
#for i,f in enumerate(files): # there was a ,start=1 here that I removed, can't remember why it would be there. shouldn't be, i think.
glove_file_path = os.path.join(glove_path,"glove.6B.50d.txt")

#get the document for GloVe
with open(glove_file_path, 'r') as vector_ref: 
	#this is trying with a 50 dimensional representation, change the number above to alter the number of dimension from [50,100,200,300]
	vector_doc = vector_ref.read().rstrip()



def get_vector_representation(word): 
	"""
	This function returns the vector representation of a word
	"""
	l = len(word)
	ind = vector_doc.find(word) 
	if ind == -1: # when the word is not found 
		return None  # only do this for now 

	ind2 = (vector_doc[ind+l:]).find("\n")
	ind2 =ind+ind2+ l
	word_vector = vector_doc[ind:ind2]
	word_vector = word_vector.split()
	return word_vector[1:]

def document_to_vec(doc): 
	"""
	This function takes in a txt document as an input and convert all words to
	vectors
	input: doc is a list of words

	"""
	result=[]
	for word in doc: 
		word_vector = get_vector_representation(word)
		result.append(word_vector)
	return result






for i,f in enumerate(txt_files): 
	if not f.endswith(".txt"):
		print("the file ",f,"is not a txt file")
		continue  # continue with the loop 
	doc_path = os.path.join(txt_path,f)
	with open (doc_path,'r') as f: 
		doc = f.read().split()  #convert the document into a list 
	print(document_to_vec(doc[:50]))
	#学术paper词太多了 


	break 


