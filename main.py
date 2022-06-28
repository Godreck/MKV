
def read_txt_file():
	file = 'file.txt'
	with open(file, 'r', encoding = 'utf-8') as f:
		data = f.read()
		print(data)
		return data 

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

#The beast team!!

if __name__ == "__main__":
    if write_in_txt_file():  # создаём и пишем в файл "I love Git"
        print("[OK] write")
    
    print(read_txt_file())  # читаем содержимое
    
    if delete_file():   # удаляем файл
        print("[OK] delete")

