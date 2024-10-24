#writing to a file
file = open('example.txt','w')
file.write('Hello World!')
file.close()

#using the with statement
#The with statement automatically manages file opening and closing, even if exception occur.
with open('example.txt','r')as file:
    content = file.read()
    print(content)
    
#reading from files
#read(size) :Reads a specified number of characters (or the whole file if not specified).
with open('example.txt','r')as file:
    content = file.read(10) #reads the first10 characters
    print(content)
    
#readline():reads a single line from the file.
with open('example.txt','r')as file:
    line = file.readline()
    print(line)
    
#readlines():reads all lines and returns a list of strings.
with open('example.txt','r')as file:
    lines = file.readlines()#reads all lines into a list
    print(lines)
    
#writing to files
#write(string):writes a string to the file.
with open('example.txt','w')as file:
    file.write("This is a test file.")
    file.write("This is a test file.")
    file.write("This is a test file.")
    file.write("This is a test file.")
    
#writelines(list):writes a list of strings to the file.
lines = ["Line 1\n","Line 2\n","Line 3\n"]
with open('example.txt','w')as file:
    file.writelines(lines)
    
#appending to files
#when using 'a' mode,data is added to the end of the file without overwriting the existing content.
with open('example.txt','a')as file:
    file.write("\nAppended text.")    