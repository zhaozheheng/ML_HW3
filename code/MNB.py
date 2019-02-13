#coding:utf8
import os
import re
import math

#multiple naive bayes modeling
class MNBModel(object):
    def __init__(self, trainPath, testPath, dirsNum, splitCode = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n]+'):
        self.trainPath = trainPath
        self.testPath = testPath
        self.dirsNum = dirsNum
        self.splitCode = splitCode

    #trainPath = "20news-bydate/20news-bydate-train"
    #testPath = "20news-bydate/20news-bydate-test"
    
    #take every txt file into an array
    def getDataset(self, trainPath):
        trainTxt = []
        i = 0
        fileList = os.walk(trainPath)
        for root, dirs, files in fileList:
            for folder in dirs:
                if i < self.dirsNum:
                    trainTxt.append(os.path.join(root, folder))
                    i = i + 1
                else:
                    break
        return trainTxt

    #count the frequency of words in trainset
    def countTrain(self, trainTxt):
        countTrainTxt = {}
        frequency = {}
        for trainSet in trainTxt:
            frequency[trainSet] = 0  
            countTrainTxt[trainSet] = self.parseTrainText(trainSet, frequency)
        return countTrainTxt, frequency

    #predict in the testset
    def predict(self, countTrainTxt, frequency):
        errors = {}
        allTokenNum, allWords, textnum = self.calculateWords(frequency, errors, countTrainTxt)
        for freq in frequency:
            testSet = freq.replace(self.trainPath, self.testPath)
            self.parseTestText(errors, freq, testSet, frequency, textnum, countTrainTxt, allTokenNum, allWords)
        return errors, textnum

    #parse traintext
    def parseTrainText(self, trainSet, frequency, flag = 1):
        text = {}
        for root, dirs, files in os.walk(trainSet):
            for file in files:
                frequency[trainSet] = frequency[trainSet] + 1
                fo = open(os.path.join(root, file), 'r')
                lines = fo.readlines()
                for line in lines:
                    line = re.sub(self.splitCode, '', line)
                    if line == "":
                        continue
                    words = line.split(' ')
                    if words[0] == "Lines" and flag == 1:
                        flag = 0
                        continue
                    if flag == 1:
                        continue
                    for word in words:
                        word = word.upper()
                        text[word] = text.get(word, 0) + 1
        return text

    #calculate prior
    def calculatePrior(self, frequency, textnum):
        marks = {}
        for num in frequency:
            marks[num] = math.log(frequency[num]/float(textnum))
        return marks

    #calculate conditional probability
    def calculateCondprob(self, marks, countTrainTxt, allTokenNum, allWords, word):
        for mark in marks:
            marks[mark] += math.log((countTrainTxt[mark].get(word, 0) + 1)/float(allTokenNum[mark] + len(allWords)))
        return marks

    #update maxMark and calculate errors
    def calculateErrors(self, errors, marks, freq):
        maxMark = float('-inf')
        for mark in marks:
            if maxMark < marks[mark]:
                maxMark = marks[mark]
        if maxMark != marks[freq]:
            errors[freq] += 1
        return errors

    #parse testtext
    def parseTestText(self, errors, freq, testSet, frequency, textnum, countTrainTxt, allTokenNum, allWords, flag = 1):
        marks = {}
        for root, dirs, files in os.walk(testSet):
            for file in files:
                marks = self.calculatePrior(frequency, textnum)
                fo = open(os.path.join(root, file), 'r')
                lines = fo.readlines()
                for line in lines:
                    line = re.sub(self.splitCode, '', line)
                    if line == "":
                        continue
                    words = line.split(' ')
                    if words[0] == "Lines" and flag == 1:
                        flag = 0
                        continue
                    if flag == 1:
                        continue
                    for word in words:
                        word = word.upper()
                        marks = self.calculateCondprob(marks, countTrainTxt, allTokenNum, allWords, word)
                self.calculateErrors(errors, marks, freq)
        return

    #calculate all the words used in the trainset
    def calculateWords(self, frequency, errors, countTrainTxt):
        textnum = 0
        allTokenNum = {}
        allWords = set()
        for trainSet in frequency:
            errors[trainSet] = 0
            textnum += frequency[trainSet]
            allTokenNum[trainSet] = 0
            txt = countTrainTxt.get(trainSet)
            for word in txt:
                allTokenNum[trainSet] += txt[word]
                allWords.add(word)
        return allTokenNum, allWords, textnum

    #calculate the total accuracy of the model
    def calculateAccuracy(self, errors, textnum):
        testerror = 0
        for error in errors:
            testerror += errors[error]
        accuracy = 1 - testerror/float(textnum)
        return accuracy

    #start multiple naive bayes learner
    def MNBLearning(self):
        trainPathTxt = self.getDataset(trainPath)
        countTrainTxt, frequency = self.countTrain(trainPathTxt)
        errors, textnum = self.predict(countTrainTxt, frequency)
        accuracy = self.calculateAccuracy(errors, textnum)
        print 'The total accuracy is ' + str(accuracy)

    

#get the path of trainset and testset
def getDataPath():
    trainPath = raw_input("Enter the training data's path: ")
    testPath = raw_input("Enter the test data's path: ")
    dirsNum = int(raw_input("Enter the num of dataset you want to train (Max: 20): "))
    if dirsNum > 20:
        dirsNum = 20
    if dirsNum < 0:
        dirsNum = 0
    return trainPath, testPath, dirsNum

if __name__ == '__main__':
    trainPath, testPath, dirsNum = getDataPath()
    mnb = MNBModel(trainPath, testPath, dirsNum)
    mnb.MNBLearning()

