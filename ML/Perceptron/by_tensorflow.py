import tensorflow as tf
import numpy as np
import time
import matplotlib.pyplot as plt
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

nSize = 1000
correct_w = -1
correct_b = 100
x_axis = np.random.uniform(0, 100, size=nSize)
y_axis = np.random.uniform(0, 100, size=nSize)
label = [1 if x_axis[i] * correct_w + correct_b > y_axis[i] else -1 for i in range(nSize)]
print(label)

positive_x = []
positive_y = []
negative_x = []
negative_y = []
for i in range(nSize):
    if label[i] < 0:
        positive_x.append(x_axis[i])
        positive_y.append(y_axis[i])
    else:
        negative_x.append(x_axis[i])
        negative_y.append(y_axis[i])


def plt_init():
    plt.figure()
    plt.scatter(np.array(positive_x), np.array(positive_y), marker='+')
    plt.scatter(np.array(negative_x), np.array(negative_y), marker='^')
    plt.plot(np.array([i for i in range(100)]), np.array([correct_w * i + correct_b for i in range(100)]), color='r')


# init perceptron
m = 2  # dimension
training_size = nSize
learning_rate = 0.2
iter = 50000

x_data = np.array([[x_axis[i], y_axis[i]] for i in range(nSize)])
y_data = np.array([[y] for y in label])

# print(x_data)
W = tf.Variable(tf.random_normal(shape=[m, 1], dtype=tf.float32, stddev=1, seed=0), name='w')
B = tf.Variable(.0, name='b')
x = tf.placeholder(dtype=tf.float32, shape=[None, m], name='x')
y = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='y')
y_prediction = tf.add(tf.matmul(x, W), B)
result = tf.multiply(y, y_prediction)
zeros = tf.constant(0, dtype=tf.float32, shape=[training_size, 1])
loss = tf.reduce_sum(tf.where(result < 0, tf.abs(y_prediction), zeros))

train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

print("===start training===")
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    iteration = 0
    for i in range(iter):
        sess.run(train_step, feed_dict={x: x_data, y: y_data})
        training_loss = sess.run(loss, feed_dict={x: x_data, y: y_data})
        print("loss:", training_loss)
        iteration = i
        if training_loss < 1e-6:
            break
    plt_init()
    print(W.eval(), B.eval())
    w = W.eval()
    A1, A2 = w[0][0], w[1][0]
    x_line = [i for i in range(100)]
    y_line = []
    for i in x_line:
        y_line.append((-A1 * i - B.eval()) / A2)
    plt.plot(np.array(x_line), np.array(y_line), color='blue', linewidth=2)
    plt.show()
    print("iteration:", iteration)
