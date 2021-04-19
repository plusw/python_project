#https://blog.csdn.net/hszzjs/article/details/81005636?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&dist_request_id=1331988.554.16187293659979865&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control
#使用自己的图片进行训练
import torch
import torchvision
from torchvision import transforms, utils
import matplotlib.pyplot as plt
 
img_data = torchvision.datasets.ImageFolder('./flower_photos',
                                            transform=transforms.Compose([
                                                transforms.Scale(256),
                                                transforms.CenterCrop(224),
                                                transforms.ToTensor()])
                                            )
 
print(len(img_data))
data_loader = torch.utils.data.DataLoader(img_data, batch_size=20,shuffle=True)
print(len(data_loader))
 
 
def show_batch(imgs):
    grid = utils.make_grid(imgs,nrow=5)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')
 
 
for i, (batch_x, batch_y) in enumerate(data_loader):
    if(i<4):
        print(i, batch_x.size(), batch_y.size())
 
        show_batch(batch_x)
        plt.axis('off')
        plt.show()