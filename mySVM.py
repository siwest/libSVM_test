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
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        data.append(l2)
        l = f.readline()
    f.close()
    print "Finished read"
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


def select_features(data_list, label_list):
    r_cols = []
    for i in range(0, len(data_list[0]), 1):
        col_list = []
        for j in range(0, len(data_list), 1):
            col_list.append(data_list[j][i])
        r = pearson_coefficient(col_list, label_list)
        r_cols.append(r)
    print "Printing all r in order ", r_cols
    top_correlated_cols = []
    print "Printing max r's "
    for i in range(0, 15, 1):
        print max(r_cols)
        selected_col = r_cols.index(max(r_cols))
        top_correlated_cols.append(selected_col)
        r_cols[selected_col] = 0

    new_data_list = [list() for row in data_list]

    for i in range(0, len(data_list), 1):
        temp_list = []
        for j in range(0, len(top_correlated_cols), 1):
            temp_list.append(data_list[i][j])
        new_data_list[i] = temp_list

    return new_data_list




def main(data, labels):
    data_list = read_data_to_list(data)
    label_list = read_labels_to_list(labels)
    new_data_list = select_features(data_list, label_list)

    model = svm_train(label_list, new_data_list, '-h 0')
    print "Printing original accuracy"
    svm_predict(label_list, new_data_list, model)
    # p_labels, p_acc, p_vals = svm_predict(labelList, dataList, model)
    # Prediction test
    test_list = read_data_to_list('testdata')
    test_label_list = [0] * len(test_list)
    p_labels, p_acc, p_vals = svm_predict(test_label_list, test_list, model)

    # ACC, MSE, SCC = evaluations(testList, p_labels)
    #print "p_labels ", p_labels


# print "p_acc", p_acc
# print "p_vals", p_vals


if __name__ == '__main__':
    main(data=sys.argv[1], labels=sys.argv[2])
