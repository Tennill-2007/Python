file_name = 'sample.txt'

def read_file():
    with open(file_name,'r') as file_1:
        read_file = file_1.read()
        print("Reading file content:\n",read_file)

try: 
    read_file()
except FileNotFoundError:
    print("Error: The file",file_name,"was not found")

