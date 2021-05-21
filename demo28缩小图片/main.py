from PIL import Image
import os

n=16#ËõÐ¡±¶Êý
input_file_extention='jpg'
output_file_extention='jpeg'
input_dir = 'E:/python_project/demo27Pytorch-UNet/data/all_data/train/'
output_dir = 'E:/python_project/demo27Pytorch-UNet/data/all_data/train_small_16/'

for file in os.listdir(input_dir):
    if not file.endswith(input_file_extention):
        continue
    img = Image.open(os.path.join(input_dir, file))

    width=img.width
    height=img.height
    #print('%sx%s' % (width, height))
    
    img.thumbnail((width//n, height//n))
    #print('%sx%s' % (width//4, height//4))

    img.save(output_dir + file, output_file_extention)