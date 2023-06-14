import cv2
import os

#dimensions of the Output images (1080x1080) by default.
im_width = 1080 #width pixels
im_height = 1080 #height pixels

#Input and Ouput Folders respectively.
input_dir,output_dir = "Input-Insert_Images_Here","Output-Edited_Images"

dirs = [output_dir,input_dir]

#Defining the image 
def resizer(im_width,im_height):
    tot_imgs = len(imgs)
    for file in imgs:
        perc = round((imgs.index(file)*100/tot_imgs),1)
        try:
            im = cv2.imread(f"{input_dir}/{file}")
            im = cv2.resize(im,(im_width,im_height))
            cv2.imwrite(os.path.join(output_dir,f"{file}"),im)
            print(f'{perc}% ({imgs.index(file)}/{tot_imgs}) - Succesfully edited the image: "{file}"\n')
        except: print(f'#ERROR: File "{file}" Could not be edited.')

#Checking if the Input and Output folders exists.
for dir in dirs:
    while True:
        try:
            os.listdir(dir)
            print(f"Access granted to dir {dir}")
            break
        except:
            os.mkdir(dir)
            print(f'The folder "{dir}" has been created.')

#Getting the images to be resized
imgs = os.listdir(input_dir)
print(imgs)

#Resizing the images
if (im_width>0) & (type(im_width)==int):
    if (im_height>0) & (type(im_height)==int):
        resizer(im_width,im_height)
    else: print('#ERROR: im_height is not an integer bigger than 0.')
else: print('#ERROR: im_width is not an integer bigger than 0.')