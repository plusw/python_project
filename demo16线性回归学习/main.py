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
plt.show()