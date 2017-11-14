# -- coding: utf-8 --
from numpy import *

def loadDataSet():
    postingList=[['my','dog','has','flea','problem','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]#首先定义多组文字
    classVec=[0,1,0,1,0,1]#定义每组文字是否具有侮辱性
    return postingList,classVec

#将所有文字组合在一个list并且去重
def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

#构造长度为所有文字长度的list并且每个元素为0，将文字变成数字0或1 如果文字出现在list中则为1，
def setOfWord2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:print "the word:%s is not in my Vocabulary!" % word
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
   # p0Num=zeros(numWords);p1Num=zeros(numWords)
    p0Num=ones(numWords);p1Num=ones(numWords)  #构造全1矩阵
   # p0Denom=0.0;p1Denom=0.0
    p0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    #p1Vect=p1Num/p1Denom
    p1Vect =log(p1Num / p1Denom)
    #p0Vect=p0Num/p0Denom
    p0Vect =log(p0Num / p0Denom)
    return  p0Vect,p1Vect,pAbusive

myList,listClasses=loadDataSet()

myVocabList=createVocabList(myList)
#print myVocabList
#print setOfWord2Vec(myVocabList,myList[3])

trainMat=[]
for postinDoc in myList:
    trainMat.append(setOfWord2Vec(myVocabList,postinDoc))
p0v,p1v,pAb=trainNB0(trainMat,listClasses)

print p0v
print p1v
print pAb