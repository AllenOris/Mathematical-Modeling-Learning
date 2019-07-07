# k-近邻算法

## 适用问题类型

* 分类 or 回归.
> 回归即取neighbors的平均值作为新样本预测值

* 数值型和标称型

## 优点

* 精度高，对异常值不敏感，无数据输入假定

## 缺点

* 计算复杂度高，空间复杂度高

## algo insights

> 总结自《统计学习方法》

### 超参数

knn本质上对应于特征空间的划分。这种划分由三个超参数决定。

1. 距离度量：$L_p$距离 等
    > 对结果是的确有影响的

2. k取值

* k值较小，相当于取值邻域较小，学习的近似误差（approximation error）会减小，但估计误差（estimation error）会增大，预测结果对近邻的点非常敏感（比如噪声）。即k值较小容易过拟合。

* k值较大，可以减少学习的估计误差，但使近似误差增大。此时与实例较远的点，也会对预测其作用。更大的k相当于使模型变得更简单。

    > 通常采用交叉验证法选取最优的k值
    > 
    > 近似误差：可以理解为对现有训练集的训练误差。
    > 
    > 估计误差：可以理解为对测试集的测试误差。
3. 分类决策规则

* 多数表决（书中说明了它的合理性）

* [加权knn](https://www.cnblogs.com/bigmonkey/p/7387943.html)（借助高斯函数加权，避免反函数）

### 优化

* 时间：[ball tree / kd tree](https://www.zhihu.com/question/30957691)

    * kd tree (k-demensional tree) dim < 20时非常快，增长到很大时，效率变低 【TODO】
    > kd tree沿着笛卡尔轴（坐标轴）分割数据，ball tree 沿着一系列的超球面分割数据。树的构造代价更高，但对于搞结构化的数据十分有效，即使维度很高。

    * ball tree -- 对于高维度数据比较好
    > Brute force 查询时间以 O[DN]增长Ball tree 查询时间大约以 O[Dlog(N)]增长KD tree 的查询时间 D的变化是很难精确描述的.对于较小的D(小于20) 的成本大约是O[Dlog(N)], 并且 KD 树更加有效.对于较大的D成本的增加接近O[DN], 由于树结构引起的开销会导致查询效率比暴力还要低.


### 个人理解

> 直觉上实现简单的算法，实际有很多可以讨论的内容。

## coding tips

1. [`numpy.tile()`](https://blog.csdn.net/ksearch/article/details/21388985) 用于将小矩阵复制，扩大。在kNN中用于拓展构造查询向量

```python
In[21]: numpy.tile([0,0],(2,3)) # 在列的方向上复制2次，在行的方向上复制3次
Out[21]:
array([[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]])
```

2. `nparr.sum(axis=1)`

* 行求和，投影到列上

3. `sorted(), np.argsort()`

* argsort() 返回的是数组值从小到大的索引值

* sorted就是排序，可以配合`operater.itemgetter()`选择排序的key

```
classCount = {}
...
sortedClassCount = sorted(classCount.items(),
                          key=operator.itemgetter(1), reverse=True)
```
