import os
def delete_file():
    file_path = 'file.txt'
    try:
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False
#The beast team!!
