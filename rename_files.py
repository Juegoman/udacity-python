import os
img_dir = r"" #insert the directory with all of the encrypted images.
def rename_files(): #define the rename_files() function
    file_list = os.listdir(img_dir) #get the list of all the images in the directory
    saved_path = os.getcwd() #save the starting working directory
    os.chdir(img_dir) #change the working directory to the image directory
    for file_name in file_list: #for each image in the directory
        #print a summary of the operation performed (removing digits)
        print("Old name: " + file_name + " New name: " + file_name.translate(str.maketrans("", "", "0123456789")))
        #perform the renaming operation (removing digits)
        os.rename(file_name, file_name.translate(str.maketrans("", "", "0123456789")))
    os.chdir(saved_path) #reset the working directory
rename_files() #execute rename_files()
