"""
Very Easy kNN Code

referencing 'Machine Learning in Action'
20190706 by lxy
"""
from pprint import pprint

import matplotlib
import matplotlib.pyplot as plt

from numpy import *
import operator
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['r', 'r', 'b', 'b']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # plt.scatter(dataSet[:, 0], dataSet[:, 1], c=labels)
    # plt.scatter(inX[:, 0], inX[:, 1])
    # plt.show()

    dataSetSize = dataSet.shape[0]
    print('dataSetSize:', dataSetSize)
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),  # dict=>list, operator.itemgetter() 用于获取对象域中的某些/个值
                              key=operator.itemgetter(1), reverse=True)  # 按value排序，逆序
    print(sortedClassCount)
    return sortedClassCount[0][0]


def testClassify0():
    group, labels = createDataSet()
    print(classify0([0, 0], group, labels, 3))


'''
dating match

1. 收集数据
2. 准备数据
3. 分析数据
4. 训练算法
5. 测试算法
6. 使用算法 
'''

likeDict = {'didntLike': 1, 'smallDoses': 2, 'largeDoses': 3}
likeDict2 = {1:1, 2:2, 3:3}


def file2matrix(filename):
    file = []
    with open(filename, 'r') as f:
        for line in f:
            file.append(line)
    l = len(file)
    X = zeros((l, 3))
    labels = []
    index = 0
    for line in file:
        # print(line)
        line = line.strip()
        # print(line)
        row = line.split('\t')
        # print(row)
        X[index, :] = row[0:3]
        # print(row[-1])
        # labels.append(likeDict[row[-1]])
        labels.append(int(row[3]))
        # print(type(row[3]))
        # print(int(row[3]))
        # print(labels)
        index += 1
    return X, labels


def dataPlot(X, labels):
    # autoNorm(X)

    """ 比较好看的绘制方法 """

    plt.figure(figsize=(8, 5), dpi=80)
    axes = plt.subplot(111)
    # 将三类数据分别取出来
    # x轴代表飞行的里程数
    # y轴代表玩视频游戏的百分比
    type1_x = []
    type1_y = []
    type2_x = []
    type2_y = []
    type3_x = []
    type3_y = []
    print(
        'range(len(labels)):')
    print(
        range(len(labels)))
    for i in range(len(labels)):
        if labels[i] == 1:  # 不喜欢
            type1_x.append(X[i][1])
            type1_y.append(X[i][2])

        if labels[i] == 2:  # 魅力一般
            type2_x.append(X[i][1])
            type2_y.append(X[i][2])

        if labels[i] == 3:  # 极具魅力
            print(
                i, '：', labels[i], ':', type(labels[i]))
            type3_x.append(X[i][1])
            type3_y.append(X[i][2])

    type1 = axes.scatter(type1_x, type1_y, s=20, c='red')
    type2 = axes.scatter(type2_x, type2_y, s=40, c='green')
    type3 = axes.scatter(type3_x, type3_y, s=50, c='blue')
    # plt.scatter(X[:, 0], X[:, 1], s=20 * numpy.array(labels),
    #             c=50 * numpy.array(labels), marker='o',
    #             label='test')
    plt.xlabel(u'每年获取的飞行里程数')
    plt.ylabel(u'玩视频游戏所消耗的事件百分比')
    axes.legend((type1, type2, type3), ('didn\'t like', 'a little', 'like'), loc=2)


# 2
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    # print(normDataSet)
    return normDataSet, ranges, minVals


def testDatingMatch():
    hoRatio = 0.10
    X, labels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(X)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     labels[numTestVecs:m], 2)
        print('the classifier came back with: %d, the real answer is: %d'
              % (classifierResult, labels[i]))

        if classifierResult != labels[i]:
            errorCount += 1
    print('the total error rate is: %f' % (errorCount/float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input('percentage of time spent playing video games?'))

    ffMiles = float(input('frequent flier miles earned per year?'))
    iceCream = float(input('liters of ice cream consumed per year?'))

    X, labels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(X)
    inArr = array([ffMiles, percentTats, iceCream])

    classifierResult = classify0((inArr-minVals)/ranges, normMat, labels, 3)
    print('You will probably like this person:', resultList[classifierResult-1])

'''
digit classifier?
'''

'''
main()
'''


def main():
    classifyPerson()


if __name__ == '__main__':
    main()
