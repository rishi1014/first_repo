import os, shutil            #imported to modules that is os and shutil

#Suppose you have a file that have a lot of file like audio vido document etc etc now you want to separate them in folders
dict_extensions = {
    'audio_extensions' : ('.mp3','.wav','.m4a'),
    'video_extensions'  :('.mp4','.mkv','.MKV','.mpeg'),
    'documents_extensions' : ('.doc','.pdf','.txt'),
}

folderpath = input("enter the folder path :-  ")    # Taking the path of the folder from the user 

def file_identifier(folderpath , file_extensions):               #created a func to identify type of files it takes 2 values 
    files = []                            #created empty list 
    for file in os.listdir(folderpath):          #loop to see all type of files in the folder 
        for extension in file_extensions:        #loop to see extensions of files
            if file.endswith(extension):         #if condition for the extensions 
                files.append(file)               #appending the files in the files list
    return files        
# print(file_identifier(folderpath, video_extensions))

for extension_type , extension_tuple in dict_extensions.items():
    folder_name =extension_type.split('_')[0] + 'Files'     #audio_extension splitted and we took audio +file as or folder name
    folder_path = os.path.join(folderpath,folder_name)     #created folder_path and joined it with folderpath and foldername
    os.mkdir(folder_name)                  #created folder by folder_name
    for item in file_identifier(folderpath , extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_newpath = os.path.join(folder_path,item)
        shutil.move(item_path,item_newpath)            #created to move file to designated folders according to the file type
        
    # print("calling file identifier \n")
    # print(file_identifier(folderpath, extension_tuple))
