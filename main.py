import os
def write_in_txt_file():
    with open('file.txt', 'w') as writer:
        writer.write('I love Git')
        return True

def delete_file():
    file_path = 'file.txt'
    try:
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False
