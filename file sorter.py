#!/usr/bin/env python
# coding: utf-8

# **The following python script goes into my downloads directory and extracts file extensions and outputs them as a python set. The aim of this exercise is to then move different file extensions into specific folders and group them per file type, e.g ".jpg" and ".png" are both image file types and will therefore be moved to the "images folder".**

# In[1]:


# imports
import os, shutil


# In[2]:


# Directory path 
path = r"/Users/bk/Downloads/"


# In[3]:


file_name = os.listdir(path)


# In[4]:


# a function that extracts all file types in my downloads directory and outputs them as a python set

def list_file_types(directory):
    file_types = set()
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_types.add(filename.split(".")[-1])
    return file_types


path = path
file_types = list_file_types(path)
print("File types in", path, ":", file_types)


# In[5]:


# For loop to check if folder exists and if not, create one

folder_names = ['pdf docs', 'image files', 'txt files', 'excel files', 'powerpoint files',
                'jupyter notebooks & python files', 'zip folders', 'word docs', 'video files']

for loop in range(0,9):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))


# In[6]:


# Organise files in download directory based on their file extensions

for file in file_name:
    if ".pdf" in file and not os.path.exists(path + 'pdf docs/' + file):
        shutil.move(path + file, path + 'pdf docs/' + file)
    elif ".jpeg" and ".jpg" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)
    elif ".JPG" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)
    elif ".png" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)
    elif ".doc" and ".docx" in file and not os.path.exists(path + 'word docs/' + file):
        shutil.move(path + file, path + 'word docs/' + file)
    elif ".xlsx" and ".xls" in file and not os.path.exists(path + 'excel files/' + file):
        shutil.move(path + file, path + 'excel files/' + file)
    elif ".csv" in file and not os.path.exists(path + 'excel files/' + file):
        shutil.move(path + file, path + 'excel files/' + file)
    elif ".txt" in file and not os.path.exists(path + 'txt files/' + file):
        shutil.move(path + file, path + 'txt files/' + file)
    elif ".ipynb" and ".py" in file and not os.path.exists(path + 'jupyter notebooks & python files/' + file):
        shutil.move(path + file, path + 'jupyter notebooks & python files/' + file)
    elif ".ipynb" in file and not os.path.exists(path + 'jupyter notebooks & python files/' + file):
        shutil.move(path + file, path + 'jupyter notebooks & python files/' + file) 
    elif ".zip" in file and not os.path.exists(path + 'zip folders/' + file):
        shutil.move(path + file, path + 'zip folders/' + file) 
    elif ".pptx" and ".pptm" in file and not os.path.exists(path + 'powerpoint files/' + file):
        shutil.move(path + file, path + 'powerpoint files/' + file)
    elif ".mp4" in file and not os.path.exists(path + 'video files/' + file):
        shutil.move(path + file, path + 'video files/' + file)  


# **I asked Chatgpt to help me improve the for loop above to organise files in download directory based on their file extensions.**
# 
# Here are a few suggestions to improve the script according to chatgpt:
# 
# 1. Use a dictionary to map file extensions to their corresponding folders. This will make the code more readable and easier to maintain.
# 
# 2. Use os.path.splitext to extract the file extension from the filename. This will make the code more concise and less error-prone.
# 
# 3. Use os.path.join to join paths instead of concatenating them with the + operator. This will make the code more platform-independent.

# In[7]:


# Code generated by Chatgpt

folders = {
    '.pdf': 'pdf docs',
    '.jpg': 'image files',
    '.jpeg': 'image files',
    '.png': 'image files',
    '.doc': 'word docs',
    '.docx': 'word docs',
    '.xls': 'excel files',
    '.xlsx': 'excel files',
    '.csv': 'excel files',
    '.txt': 'txt files',
    '.ipynb': 'jupyter notebooks & python files',
    '.py': 'jupyter notebooks & python files',
    '.zip': 'zip folders',
    '.pptx': 'powerpoint files',
    '.pptm': 'powerpoint files',
    '.mp4': 'video files'
}

for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_name)
        if ext.lower() in folders:
            folder = folders[ext.lower()]
            dest_folder = os.path.join(path, folder)
            if not os.path.exists(os.path.join(dest_folder, file_name)):
                shutil.move(file_path, os.path.join(dest_folder, file_name))


# In[ ]:




