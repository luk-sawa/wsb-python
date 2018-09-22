import os


def catalog(def_directory, branch):
    prefix = branch*"\t"
    for file in os.listdir(path=def_directory):
        print(prefix+file)
        if os.path.isdir(file):
            branch += 1
            def_directory = def_directory+'\\'+file
            catalog(def_directory, branch)
    return


directory = 'D:\Projekty\Python\Studia'
catalog(directory, 0)
