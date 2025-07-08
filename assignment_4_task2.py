write_text = input("Enter text to write to the file: ")
with open('output.txt','w') as file_1:
    write_in_file = file_1.write(write_text)
    print("Data successfully written to output.txt")

append_text = input("Enter the additional text to append: ")
with open('output.txt','a') as file_1:
    append_in_file_1 = file_1.write("\n")
    append_in_file = file_1.write(append_text)
    print("Data successfully apended")

with open('output.txt','r') as file_1:
    read_file = file_1.read()
    print("Final content of output.txt: \n",read_file)
