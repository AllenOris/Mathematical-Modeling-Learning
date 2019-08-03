# 3. Types of learning

> 本节课对机器学习的问题从主要的四个角度进行了划分，进行了分别的介绍

## 不同类别的输出`y`

1. 二分类

2. 多分类

3. 回归问题

> 输出在连续域上

4. structured learning 

> 可以认为是更复杂、泛化的多分类问题。开始的时候，只知道“类别的域”；诸如词性标注，需要对每个句子标注词性，这个句子最终的输出是一个词性的sequence，这个序列可以视为一个更大的类【hyperclass】，这个hyperclass的可能性有很多，只不过它的具体形式是在开始时便已经确定的。

5. and more...

## 不同的标签形式

1. 监督式

2. 非监督

> 典型问题：
> * 聚类【cluster】
> * 密度分析【density estimation】
> * 异常检测【outlier detection】

3. 半监督

由于成本等原因，只告诉一部分的标签

4. 强化学习

“learn with partial/implicit information”

建立惩罚机制，让机器根据产生的输出带来的反馈【goodness，可以认为是好或坏，即不完全的标签】进行学习

> 是很不同的方式

5. and more...

## 不同的数据喂给方式

1. batch learning 

直接根据一堆数据建立一次性的模型，predict with fixed `g`

2. online

接受序列的【不断的】的输入，不断update `g`

> PLA可以很容易使用online protocol，因为它每次只根据一个错误的点进行w的挑战

> 强化学习经常是online的，都是时序的嘛。

3. active learning

> 让算法有针对性的问问题【即问一些X的标签y】，期望用更少的带有标签的数据，训练更好的模型。

4. and more...

## 不同类别的输入`X`

1. concrete features

输入的数据是在某种形式上经过人类预处理过的数据形式，数据中的特征表现会更明显，抽象级别较低，有比较明显的物理含义，机器容易理解。

2. raw data

指诸如pixel，音频数据等原数据，在学习的过程中，每一个特征只具有简单的物理意义，单独的每个对于结果的获取，都起到很小的作用。若使用机器学习算法，可能需要人为的构建特征【特征工程】，或利用深度学习等手段让计算机自己寻找好的特征。

3. abstract 

一些由无物理意义的数字构成的指代【如主键】，比如1号顾客喜欢10号产品。这类数据一般不包含真实含义，从这类数据本身，计算机无法学到任何知识。需要进一步的 ‘feature conversion/extraction/construction’。

