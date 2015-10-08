from __future__ import division
import string
import math
import jieba as jb
import glob
from collections import Counter
import string


#this block of code does the dirty works
#ie. preprocessing the raw data

def txtToDocList(filepath):
    """
    pass in a txt filepath
    output a list, each element of the list is one line(one document) from the file
    e.g
    txtList = ["hello suckers","my name is your papa,idoit"]
    """
    f = open(filepath,'r')
    doc_list = list()
    for line in f.readlines():
        doc_list.append(line)
    f.close()
    return doc_list

def DocListToTokenList(ltxt):
    """
    takes in a list of documents,
    output the tokenized version for the documents in a list.
    [["hello","this is","your papa"],["wocao","nima"]]
    """
    doc_token_list = list()
    for instance in ltxt:
        doc_token_list.append(jb.lcut(instance, cut_all=False))
    return doc_token_list



#doc_raw_list = txtToDocList('./lily/Basketball.txt')
#doc_token_list = DocListToTokenList(doc_raw_list)


def make_big_dic(filesPath):
    """
    make a BIG dic with the following perperty:
    key: class name, ie "Basketball"
    Value: a list, each element itself is also a list, 
            [["尼玛", "我", "又饿了"], ["我", "也", "是"]]
    """
    files_path_list = glob.glob(filesPath) #['./lily/Basketball.txt', ..]
    class_to_docs_dic = {}
    for filePath in files_path_list:
        class_name = filePath.split('/')[-1].split('.')[0]
        doc_list = list(txtToDocList(filePath))
        class_to_docs_dic[class_name] = list(DocListToTokenList(doc_list))
    return class_to_docs_dic

def get_whole_corups(class_to_docs_dic):
    """

    input: class to docs dic
    output: a list containing all the tokenlized docs,ie, concate all the values in dic
            each element in the corups_list is a DOCUMENT(a list),with tokens as its elements
    eg
         [['I', 'totally agree.'], ["they'll", 'die alnoe.'], ['we are', 'the one.'], ['they are', 'not.']]

    """
    corups_list = list()
    for class_name in class_to_docs_dic.keys():
        for tokens in class_to_docs_dic[class_name]:
            corups_list.append(tokens)
    return corups_list



filesPath = "./lily/*.txt" 
class_to_docs_dic = make_big_dic(filesPath)
docs_token_all = get_whole_corups(class_to_docs_dic)







#check lenth match
doc_num = 0
for classes in class_to_docs_dic.keys():
    doc_num += len(class_to_docs_dic[classes])
print "the total number of docs in all classes is:"
print doc_num
print len(docs_token_all)

for classname in class_to_docs_dic.keys():
    print "there are " + str(len(class_to_docs_dic[classname])) +" docs in " + str(classname)

#print class_to_docs_dic.keys() #Should be ['Basketball', 'D_Computer',...'Stock']
print "all set. ready to go"



"""
now we have the docs_token_all, aka a list for docs, each doc is a list, with tokens as its elements
eg:         [['I', 'totally agree.'], ["they'll", 'die alnoe.'], ['we are', 'the one.'], ['they are', 'not.']]

"""

#first, make a tf

 

"""
now we have the docs_token_all, aka a list for docs, each doc is a now0)
now0list, with tokens as its elements
eg:
[['I', 'totally agree.'],["they'll", 'die alnoe.'],
['we are', 'the one.'], ['they are', 'not.']]

"""

def buidl_lexicon(docs_token_all):
    lexicon = set()
    for doc in docs_token_all:
        lexicon.update([token for token in doc])
    return lexicon

def tf(term,doc):
    return freq(term,doc)

def freq(term,doc):
    count = 0
    for token in doc:
        if token == term:
            count = count + 1
    return count

vocabulary = buidl_lexicon(docs_token_all)

print "the vocabulary vector is [" + ",".join(list(vocabulary))+']'
print "the total length of the vocabulary is :"
print len(list(vocabulary))

def make_tf_dic(class_to_docs_dic,vocabulary):
    """
    input : the class_to_docs_dic
    output: a new dic, with 
        key:    class_name
        values: list of tf_vectors for each doc 
    """
    class_tf_dic = {}
    for class_name in class_to_docs_dic.keys():
        class_tf_dic[class_name] = list()
        for doc in class_to_docs_dic[class_name]:
            class_tf_dic[class_name].append([tf(token,doc) for token in vocabulary ])
    return class_tf_dic

print "building class_tf_dic....."
print "the class_tf_dic is a dic with key=class_name, value [ [1,0,0,54,0...],[],..]"

class_tf_dic = make_tf_dic(class_to_docs_dic,vocabulary)

print "the class_tf_dic is ready..."