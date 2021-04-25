#CIFAR-10数据集可视化保存到本地
#https://blog.csdn.net/qq_41895190/article/details/103522142
import pickle
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
 
 
 
classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
images_dir = "./images/"
test_dir = "./test/"
 
images_batch = "./data/cifar-10-batches-py/data_batch_"
test_batch = "./data/cifar-10-batches-py/test_batch"
 
 
def load_images(save_path, path_batch, num=1):
    data = []
    labels = []
    print("path_batch", path_batch)
    with open(path_batch, mode='rb') as file:
        data_dict = pickle.load(file, encoding='bytes')
        data += list(data_dict[b'data'])
        labels += list(data_dict[b'labels'])
    img = np.reshape(data, [-1, 3, 32, 32])
 
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for i in range(img.shape[0]):
        r = img[i][0]
        g = img[i][1]
        b = img[i][2]
 
        ir = Image.fromarray(r)
        ig = Image.fromarray(g)
        ib = Image.fromarray(b)
        rgb = Image.merge("RGB", (ir, ig, ib))
 
        if i < 10:  # 只显示前10张图片
            print("view")
            #plt.imshow(rgb)
            #plt.axis('off')  # 不显示坐标轴
            #plt.show()
        label = classification[labels[i]]
        save_dir = save_path + label + "/"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        name = label + "_img-" + str(i) + ".png"
        rgb.save(save_dir + name, "PNG")  # 文件夹下是RGB融合后的图像
 
 
if __name__ == "__main__":
    # images
    print("正在保存images图片:")
    for i in range(5):
        path = images_batch + str(i + 1)
        load_images(images_dir, path)
    print("保存images完毕.")
    # test
    print("正在保存test图片:")
    load_images(test_dir, test_batch)
    print("保存test完毕.")



'''
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
data = unpickle('datasets/cifar-10-batches-py/data_batch_1')
data1 = unpickle('datasets/cifar-10-batches-py/batches.meta')
print(data.keys())
print(data1.keys())
print(data1)
print(data1[b'num_cases_per_batch'])
print(data1[b'label_names'])
print(data1[b'num_vis'])
'''
'''
# 输出图像的函数
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


# 随机获取训练图片
dataiter = iter(trainloader)
images, labels = dataiter.next()

# 显示图片
imshow(torchvision.utils.make_grid(images))
# 打印图片标签
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
'''
'''
fig = plt.figure()
for i in range(6):
  plt.subplot(2,3,i+1)
  plt.tight_layout()
  plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
  plt.title("Ground Truth: {}".format(example_targets[i]))
  plt.xticks([])
  plt.yticks([])
plt.show()
'''
'''
import cv2
import numpy as np
file = './data/cifar-10-batches-py/data_batch_1'
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo,encoding='latin1')
    return dict
dict1 = unpickle(file)
for i in range(10):#我只保存的100张
    img = dict1["data"][i]#得到图片的数据
    img = np.reshape(img, (3, 32,32))  #转为三维图片数组
    img = img.transpose((1,2,0))#通道转换为CV2的要求形式
    img_name = dict1["filenames"][i]#拿到图片的名字
    img_label = str(dict1["labels"][i])#拿到图片的标签
    cv2.imwrite(str(i),img)#保存
 '''
