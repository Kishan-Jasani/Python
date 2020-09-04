#Write Only (‘w’): 
# --> Open the file for writing. For an existing file, the data is truncated and over-written.

#Read Only (‘r’): 
# --> Open the file for reading.

#Write and Read (‘w+’): 
# --> Open the file for reading and writing. For an existing file, data is truncated and over-written.

#Append Only (‘a’): 
# --> Open the file for writing. The data being written will be inserted at the end, after the existing data.

#Append and Read (‘a+’): 
# --> Open the file for reading and writing. The data being written will be inserted at the end, after the existing data.


#open(file_path,operation)
# --> This method is used to open the file for the specified operation. The operation can either be r,w,a for read, write and append.
open_file = open("D:\File_Handling.txt","w")


#write()
# --> This method is used to write a string to a file, if file is present. If not, it creates the file and writes the string into it.
open_file.write("Hello")



#close()
# --> This method is used to close a file which is already open.
open_file.close()



#read()
# --> This method is used to read all the contents of a file into a string.
try:
    read_file=open("D:\File_Handling.txt","r")
    text=read_file.read()
    print(text)
    read_file.write(",Good Morning")    #Throw exception here because file has only read access.
    read_file.close()
except:
    print("Error occurred")
    if read_file.closed:
        print("File is closed")
    else:
        print("File is open")