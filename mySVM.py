import math

from svmutil import *
import sys


def read_data_to_list(text_file):
    """Read data as a list of lists: each row represented as a list"""
    f = open(text_file)
    data = []
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
    return data


def read_labels_to_list(label_file):
    """Read only labels - LibSVM requires only labels, no line numbers."""
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
    """Select top 15 correlates features and return new data list containing only data for those columns"""
    r_cols = []
    for i in range(0, len(data_list[0]), 1):
        col_list = []
        for j in range(0, len(data_list), 1):
            col_list.append(data_list[j][i])
        r = pearson_coefficient(col_list, label_list)
        r_cols.append(abs(r))
    # print "Printing all r in order ", r_cols
    top_correlated_cols = []
    # print "Printing max r's "

    col_output_file = open('selected_feature_cols', 'w+')
    for i in range(0, 150, 1):
        # print max(r_cols)
        selected_col = r_cols.index(max(r_cols))
        print>> col_output_file, selected_col
        top_correlated_cols.append(selected_col)
        r_cols[selected_col] = 0
    col_output_file.close()

    return top_correlated_cols


def clean_data(top_correlated_cols, data_list):
    new_data_list = [list() for row in data_list]
    for i in range(0, len(data_list), 1):
        temp_list = []
        for j in range(0, len(top_correlated_cols), 1):
            temp_list.append(data_list[i][top_correlated_cols[j]])
        new_data_list[i] = temp_list

    return new_data_list


def main(train_data, train_labels, test_data):
    data_list = read_data_to_list(train_data)
    label_list = read_labels_to_list(train_labels)

    top_correlated_cols = select_features(data_list, label_list)
    new_data_list = clean_data(top_correlated_cols, data_list)

    model = svm_train(label_list, new_data_list, '-h 0')
    print "Printing accuracy based on training data: ",
    svm_predict(label_list, new_data_list, model)

    test_list = read_data_to_list(test_data)
    new_test_list = clean_data(top_correlated_cols, test_list)
    test_label_list = [0] * len(new_test_list)
    p_labels, p_acc, p_vals = svm_predict(test_label_list, new_test_list, model)

    output_file = open('output', 'w+')
    for label in p_labels:
        print>> output_file, label

    # print "p_acc", p_acc
    # print "p_vals", p_vals


if __name__ == '__main__':
    main(train_data=sys.argv[1], train_labels=sys.argv[2], test_data=sys.argv[3])
