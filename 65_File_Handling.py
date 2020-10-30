import os

#   The key function for working with files in Python is the open() function.
#   The open() function takes two parameters; filename, and mode.
#   There are four different methods (modes) for opening a file:
#        "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#        "a" - Append - Opens a file for appending, creates the file if it does not exist
#        "w" - Write - Opens a file for writing, creates the file if it does not exist
#        "x" - Create - Creates the specified file, returns an error if the file exists
#    In addition you can specify if the file should be handled as binary or text mode
#        "t" - Text - Default value. Text mode
#        "b" - Binary - Binary mode (e.g. images)



#65 Python Tutorial for Beginners | File handling

f = open('File_handling.txt','r')

# below command to read entire file at once.
#print(f.read())

print('-----------------------')
print(f.readline(), end="")
print(f.readline())

# to print char from the point of cursor:
print(f.readline(2))

print('-----CREATE AND WRITE into FILE------------------')
#if file is not exists then it will create file for you.

f1 = open("File_handling1.txt", "w")
f1.write("Hello \n This is my first file \n")
f1.write("Hello \n This is my second file ")

f1.close();

f1 = open("File_handling1.txt", 'a')
f1.write("\n\nAppended data to this file")

print('-----Append comp------------------')


try:
    f2 = open("File_handling1.txt", 'x')
    f2.write("\n\nAppended data to this file")

except Exception as e:
    print("file already exists", e)


print("\n\n\n\nCreate or delete files\n\n")

f3 = open('temp1.txt', 'w')
f3.write("file into dir")


f3 = open('temp1.txt', 'r')
print(f3.readline(4))
print(f3.read())
f3.close()

# it will overwrite file if exists
f3 = open('temp1.txt', 'w')
f3.write("file into dir new")
f3.close()


# it will remove file even open in python window.
os.remove('temp1.txt')

print('------------------------------------------ssss-')
print("\nCreate or drop dir \n")



#if os.path.exists('myfile1.txt'):
#    os.remove('myfile1.txt')
#    os.rmdir('mydir1')
#else:
#    os.mkdir('mydir1')
#    f4 = open('\\mydir1\myfile1.txt','w')
#    f4.write("new file inside dir")
#    f4.write("new file inside dir")


#f4.close()
print('-------------------------------------------')
