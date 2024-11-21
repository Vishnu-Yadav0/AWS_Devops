# Opening a Python File Using with...open

# Reading from a file
# with open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", 'r') as file:
#     content = file.read()
#     print(content)


# Writing to a file 
# with open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", 'w') as file:
#     file.write("C3Ops - MLOps")


# Reading from a file
# with open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", 'r') as file:
#     content = file.read()
#     print(content)

# Appending to a file:
with open("/Users/ck/Desktop/Python_Module/fileHandling/devtools1.txt", 'a') as file:
    file.write("\nWelcome to MLOps Engineering on AWS")

# Here, with...open automatically closes the file, so we don't have to use the close() function.
    