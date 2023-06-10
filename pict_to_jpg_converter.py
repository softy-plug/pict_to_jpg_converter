import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
pict_folder = askdirectory(title='Select folder with pict images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the pict folder
for file_name in os.listdir(pict_folder):
    if file_name.endswith('.pict'):
        # open pict image and convert to jpg
        pict_file_path = os.path.join(pict_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        pict_image = Image.open(pict_file_path)

        # save jpg image with maximum quality
        pict_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All pict images in {pict_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug