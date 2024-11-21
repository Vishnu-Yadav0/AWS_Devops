##### Session Video:
    https://drive.google.com/file/d/1fcrmELA_pNNQIYm8pvqxw09tG2w233Jy/view?usp=sharing
    
# Text Editors in Linux 

####
    1. Insert Mode: 
        - i = inserts the text at current cursor position
        - I = inserts the text at beginning of line
        - A = Appends the text at end of line
        - o = inserts a line below current cursor position
        - O = inserts a line above current cursor position
        - r = replace a single char at current cursor position

    2. Execute Mode:
        - :q       = quit without saving
        - :!       = forcefully
        - :q!	     = quit forcefully without saving
        - :w       = save
        - :wq      = save & quit
        - :wq!     = save, quit forcefully
        - :se nu   = setting line numbers for reading only 
        - :se nonu = Removing the line numbers
        - :20      = Press enter to go to specific line like 20
        - :6,10 w! <new_file> : We can copy desire lines     [ :12,18 w! >>/root/Desktop/mac.txt ] 
        - :%s/cursor/devops/g : Search and Replace 

    3. Command Mode:
        - dd   = Deletes a line 
        - ndd  = Delete 2 lines  # 2dd 
        - yy   = Copy a line
        - nyy  = copies 3 lines  # 3yy # 100yy
        - p    = put (paste deleted or copied text)
        - u    = undo (can undo 1000 times)
        - ctrl+r = Redo
        - G      = Moves cursor to last line of file
        - /<word to find> = To search for a particular word.


Sure! Unix/Linux permissions are a crucial aspect of managing files and directories in a Unix-like operating system. They determine who can do what with a file or directory. There are three types of permissions: read (r), write (w), and execute (x), and three categories of users: owner (u), group (g), and others (o).

Here are some step-by-step notes with examples to help you understand Unix/Linux permissions:

Step 1: Viewing Permissions
You can view permissions using the ls command with the -l flag. It will show a long listing that includes permissions.


$ ls -l
-rw-r--r-- 1 user group 4096 Oct  1 13:30 myfile.txt
In this example, rw-r--r-- represents the permissions for the file myfile.txt.

Step 2: Understanding Permission Notations
Permissions are represented using a 10-character string:

- r w x   r w x   r w x
| | |   | | |   | | |
| | |   | | |   | | +----> Others can execute
| | |   | | |   +-------> Others can write
| | |   | | +-----------> Others can read
| | |   | +-------------> Group can execute
| | |   +---------------> Group can write
| | +------------------> Group can read
| +---------------------> Owner can execute
+-----------------------> Owner can write
Step 3: Changing Permissions
3.1. Using Octal Notation
You can use numbers to set permissions using octal notation:

4 stands for read (r)
2 stands for write (w)
1 stands for execute (x)
0 means no permission
Example:

$ chmod 755 myfile.txt
This sets the permissions to rwxr-xr-x for the owner, r-xr-xr-x for the group, and r-xr-xr-x for others.

3.2. Using Symbolic Notation
You can use symbolic notation to change permissions:

+ adds a permission
- removes a permission
= sets the permission explicitly
Example:


$ chmod u+x myfile.txt    # Adds execute permission for the owner
$ chmod go-w myfile.txt   # Removes write permission for group and others
$ chmod g=r myfile.txt    # Sets group permission to read-only

Step 4: Changing Ownership
You can change ownership using the chown command:


$ chown newowner:newgroup myfile.txt
This changes the owner to newowner and the group to newgroup.

Step 5: Changing Group
You can change the group of a file using the chgrp command:


$ chgrp newgroup myfile.txt
This changes the group of myfile.txt to newgroup.

Step 6: Special Permissions
There are some special permissions:

Setuid (s): Allows a program to run with the permissions of the owner.
Setgid (s): Allows a program to run with the permissions of the group.
Sticky bit (t): Prevents users from deleting files in a directory they don't own.
Example:


$ chmod +s myprogram     # Sets the setuid permission
$ chmod +t mydirectory   # Sets the sticky bit

Step 7: Default Permissions

You can set default permissions for newly created files and directories using umask.

$ umask 022    # Sets default permissions to rw-r--r--

Here's how the digits map to permissions:

4 represents read permission.
2 represents write permission.
1 represents execute permission.
0 represents no permission.
To calculate the absolute mode:

Read permission (r) = 4
Write permission (w) = 2
Execute permission (x) = 1
Add these values together to get the desired permission combination.

Examples:
To give read and write permissions to the owner, and read-only permissions to the group and others:

Owner: r+w = 4+2 = 6
Group: r = 4
Others: r = 4

Absolute mode: 644

To give full permissions to the owner, and read-only permissions to the group and others:

Owner: r+w+x = 4+2+1 = 7
Group: r = 4
Others: r = 4

Absolute mode: 744

To give execute permission to the owner and group, but not others:

Owner: r+w+x = 4+2+1 = 7
Group: r+w+x = 4+2+1 = 7
Others: None = 0

Absolute mode: 770

Applying Absolute Mode:
You can apply the absolute mode using the chmod command:


$ chmod 644 myfile.txt
This sets the permissions for myfile.txt to read-write for the owner, and read-only for the group and others.


$ chmod 770 myscript.sh
This sets the permissions for myscript.sh to read-write-execute for the owner and group, and no permissions for others.

Remember, be cautious when setting file permissions, especially for system-critical files. Incorrect permissions can lead to security risks or system malfunctions. Always ensure you have the necessary permissions before making changes.