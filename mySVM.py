from svmutil import *
import sys


def readDatatoList(textFile):
	f = open(textFile)
	data = []
	i = 0
	l = f.readline()

	# Read Data
	while (l != ''):
		a = l.split()
		l2 = []
		for j in range (0, len(a)/100, 1):
			l2.append(float(a[j]))
		data.append(l2)
		l = f.readline()
	f.close()
	return data

def readLabelstoList(labelFile):
	f = open(labelFile)
	data = []
	i = 0
	l = f.readline()
	# Read Data
	while (l != ''):
		a = l.split()
		data.append(int(a[0]))
		l = f.readline()
	f.close()
	return data

def main(data, labels):
    dataList = readDatatoList(data)
    labelList = readLabelstoList(labels)
    model = svm_train(labelList, dataList)


if __name__ == '__main__':
    data = sys.argv[1]
    labels = sys.argv[2]
    main(data, labels)