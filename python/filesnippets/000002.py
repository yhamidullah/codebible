import os
import glob

datapath = "./data"
ext = ".jpg"

def rename_files(path, subdirname, files, indexe, ext=".jpg"):
    """
        Rename files inside 2 subfolders
        :param path -> path to subfolders
        :param subdirname -> subfolder name
        :files -> path to files
        :indexe -> for itereation 
        :ext -> file extension
        :return -> None
        :0 -> subfolder name. files will take subfolder name. (0 for subfold1 and 1 for subfold2) 
    """   
    absname = os.path.join(path,str(subdirname))
    newname = os.path.join(str(subdirname)+"_"+str(indexe)+ext)
    os.rename(files, os.path.join(absname, newname))

for iter, filename in enumerate(glob.glob(datapath+"/*/*")):
    subdir = filename.split("\\")[1]
    if "0"== subdir: rename_files(datapath, subdir, filename, iter)
    else: rename_files(datapath, subdir, filename,  iter)
    
