# -*- coding: gbk -*-
#我们构造一个简单的人工训练数据集，它可以使我们能够直观比较学到的参数和真实的模型参数的区别。设训练数据集样本数为1000，
#输入个数（特征数）为2。给定随机生成的批量样本特征 X∈R1000×2 ，我们使用线性回归模型真实权重 w=[2,3.4]和偏差 b=4.2 ，
#以及一个随机噪声项来生成标签
from IPython import display
from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random

num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))#创建二维随机数组，shape表示几行几列的，scale表示正太分布的标准差为1
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b#求和,labels是一个一千个的一维数组
labels += nd.random.normal(scale=0.01, shape=labels.shape)#再加上随机噪声误差
def use_svg_display():
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize
set_figsize()
plt.scatter(features[:, 1].asnumpy(), labels.asnumpy(), 1);

plt.show()#通过生成第二个特征features[:, 1]和标签 labels 的散点图，可以更直观地观察两者间的线性关系。
def data_iter(batch_size, features, labels):#在训练模型的时候，我们需要遍历数据集并不断读取小批量数据样本。这里我们定义一个函数：它每次返回batch_size（批量大小）个随机样本的特征和标签。
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)  # 样本的读取顺序是随机的
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i: min(i + batch_size, num_examples)])
        yield features.take(j), labels.take(j)  # take函数根据索引返回对应元素
#取10个数据

batch_size = 10
'''
for x, y in data_iter(batch_size, features, labels):
    print(x, y)
    break
'''

w = nd.random.normal(scale=0.01, shape=(num_inputs, 1))
print("初始化:",w)
b = nd.zeros(shape=(1,))
print("初始化:",b)
w.attach_grad()
b.attach_grad()   

def linreg(X, w, b):  
    return nd.dot(X, w) + b #dot()返回的是两个数组的点积(dot product)

def squared_loss(y_hat, y):  # 本函数已保存在d2lzh包中方便以后使用
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):  # 本函数已保存在d2lzh包中方便以后使用
    for param in params:
        param[:] = param - lr * param.grad / batch_size
        

lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):  # 训练模型一共需要num_epochs个迭代周期
    # 在每一个迭代周期中，会使用训练数据集中所有样本一次（假设样本数能够被批量大小整除）。X
    # 和y分别是小批量样本的特征和标签
    for X, y in data_iter(batch_size, features, labels):
        with autograd.record():
            l = loss(net(X, w, b), y)  # l是有关小批量X和y的损失
            print("loss",l)
            print("loss")
        l.backward()  # 小批量的损失对模型参数求梯度
        sgd([w, b], lr, batch_size)  # 使用小批量随机梯度下降迭代模型参数
    train_l = loss(net(features, w, b), labels)
    print('epoch %d, loss %f' % (epoch + 1, train_l.mean().asnumpy()))
print(true_w,w)
print(true_b,b)
plt.show()

