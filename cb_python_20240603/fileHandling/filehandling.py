# Python File Operation

'''
A file is a named location used for storing data. 

For example, filehandling.py is a file that is always used to store Python code.

Python provides various functions to perform different file operations, a process known as File Handling.

'''

# Opening Files in Python

"""
In Python, we need to open a file first to perform any operations on it—we use the open() function to do so. Let's look at an example:

Suppose we have a file named devtools.txt

"""

# To open this file, we can use the open() function.

filename = open("/Users/ck/Desktop/Python_Module/fileHandling/devtools.txt")

# File Object Name : filename 
# Now, we can use this object to work with files.

# Reading Files in Python
'''
After we open a file, we use the read() method to read its content. For example,

Suppose we have a file named devtools.txt
'''

# Now, let's read the content of the file.

read_content = filename.read()

#print(read_content)

# Writing to Files in Python
'''
To write to a Python file, we need to open it in write mode using the w parameter.

Suppose we have a file named devtools.txt. Lets write to this file
'''
# open the devtools.txt in write mode
write_content = open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", 'w')

#write contents to the devtools.txt file
write_content.write('Welcome to Cloud Binary\n')
write_content.write('AWS DevOps\n')
write_content.write('MLOps\n')
write_content.write('FinOps\n')

# Closing Files in Python

'''
When we are done performing operations on the file, we need to close the file properly. 

We use the close() function to close a file in python.

'''

cb_file = open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", "r")

cb_read_content = cb_file.read()

print(cb_read_content)

# close the file
cb_file.close()

