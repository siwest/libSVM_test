import math

from svmutil import *
import sys


def read_data_to_list(text_file):
    f = open(text_file)
    data = []
    i = 0
    l = f.readline()

    # Read Data
    while l != '':
        a = l.split()
        l2 = []
        for j in range(0, len(a), 150):
            l2.append(float(a[j]))
        data.append(l2)
        l = f.readline()
    f.close()
    return data


def read_labels_to_list(label_file):
    f = open(label_file)
    data = []
    i = 0
    l = f.readline()
    # Read Data
    while l != '':
        a = l.split()
        data.append(int(a[0]))
        l = f.readline()
    f.close()
    return data


def pearson_coefficient(x, y):
    """Calculate pearson correlation coefficient for two vectors x and y of equal length."""
    assert (len(x) == len(y))

    def std(v):
        n = len(v)
        e_v_sq = sum([v[i] * v[i] for i in range(0, n)]) / float(n)
        e_v = sum([v[i] for i in range(0, n)]) / float(n)
        return math.sqrt(e_v_sq - e_v * e_v)

    n = len(x)
    x_mean = sum(x) / float(n)
    y_mean = sum(y) / float(n)

    return sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(0, n)]) / (n * std(x) * std(y))


def main(data, labels):
    data_list = read_data_to_list(data)
    label_list = read_labels_to_list(labels)
    model = svm_train(label_list, data_list)
    # p_labels, p_acc, p_vals = svm_predict(labelList, dataList, model)
    # Prediction test
    test_list = read_data_to_list('testdata')
    test_label_list = [0] * len(test_list)
    p_labels, p_acc, p_vals = svm_predict(test_label_list, test_list, model)

    # ACC, MSE, SCC = evaluations(testList, p_labels)
    print "p_labels ", p_labels


# print "p_acc", p_acc
# print "p_vals", p_vals


if __name__ == '__main__':
    main(data=sys.argv[1], labels=sys.argv[2])
