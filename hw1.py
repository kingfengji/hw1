"""
now we have the docs_token_all, aka a list for docs, each doc is a now0)
now0list, with tokens as its elements
eg:
[['I', 'totally agree.'],["they'll", 'die alnoe.'],
['we are', 'the one.'], ['they are', 'not.']]

"""
import string

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
    





