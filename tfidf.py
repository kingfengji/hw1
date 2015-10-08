#import sys
import jieba as jb
#reload(sys)
#sys.setdefaultencoding('utf-8')



def txtToList(filepath):
    """
    pass in a txt filepath
    output a list, each element of the list is one line from the file
    e.g
    txtList = ["hello suckers","my name is your papa,idoit"]
    """
    f = open(filepath,'r')
    txtList = list()
    for line in f.readlines():
        txtList.append(line)
    f.close()
    return txtList

def listToTokenList(ltxt):
    token_list = list()
    for instance in ltxt:
        token_list.append(jb.lcut(instance, cut_all=False))
    return token_list
"""
import jieba as jb
for i in range(len(result)):
    lists = jb.cut(result[i])
    print "seg  " +"/".join( lists )
"""
import glob
filepathList =  glob.glob("./lily/*.txt")
print filepathList

"""
the filepathList should be:
    ['./lily/Basketball.txt', './lily/D_Computer.txt', './lily/FleaMarket.txt', './lily/Girls.txt', './lily/JobExpress.txt',..]
"""

class_name_list = list()
for filepath in filepathList:
    class_name = filepath.split('/')[-1].split('.')[0]
    class_name_list.append(class_name)

#print class_name_list
"""
the class_name_list is just a list of class we want to classify
["Basketball","D_Computer",...]

"""

dic_org = {}

for filepath in filepathList:
    class_name = filepath.split('/')[-1].split('.')[0]
    dic_org[class_name] = list(txtToList(filepath))

#print dic.keys()
#print dic.values()
#print dic['Basketball'][33]
dic_tokenList = {}
for filepath in filepathList:
    class_name = filepath.split('/')[-1].split('.')[0]
    dic_tokenList[class_name] = listToTokenList(list(dic_org[class_name]))

#print "/". join(dic_tokenList['D_Computer'][3])

#now delete the stopping words

#l3 = l1 - l2
#l3 = [x for x in l1 if x not in l2]
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
 