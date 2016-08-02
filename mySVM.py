from svmutil import *
import sys


def readFiletoList(textFile):
	f = open(textFile)
	data = []
	i = 0
	l = f.readline()

	# Read Data
	while (l != ''):
		a = l.split()
		l2 = []
		for j in range (0, len(a), 1):
			l2.append(int(a[j]))
		data.append(l2)
		l = f.readline()
	f.close()
	return data

def main(data, labels):
    dataList = readFiletoList(data)
    print "dataList", dataList[0]
    labelList = readFiletoList(labels)
    print "labelList", labelList[0]
    model = svm_train(labelList, dataList)


if __name__ == '__main__':
    data = sys.argv[1]
    labels = sys.argv[2]
    main(data, labels)