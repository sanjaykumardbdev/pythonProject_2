#read from one file n write into another file


f1 = open("test1.txt",'w')
f1.write("This is my 1st test date\n")
f1.write("This is my 2nd test date\n")
f1.write("This is my 3rd test date\n")
f1.write("This is my 4th test date\n")
f1.close()


f2 = open("test1.txt", "r")
for i in f2:
    print(i)

f3 = open("test1.txt","r")
f4 = open("test2.txt","w")
for i in f3:
    f4.write(i)

f4.close()

print('Reading file which is written recently \n --------------- ')
f2 = open("test2.txt", "r")
for i in f2:
    print(i)



print('copy image \n ----------rb: read,binary---- wb: write, binary ----- ')

img1 = open('mypic1.JPG','rb')

img_copy = open('myNewpic.JPG', 'wb')
for i in img1:
    img_copy.write(i)


