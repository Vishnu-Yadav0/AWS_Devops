#### Session Video:
```
https://drive.google.com/file/d/15qrxLihMOk0jNCbsmMmRNGHvyRIYjTAZ/view?usp=sharing
```

#### Version Control System / Source Code Management : Git
- Getting Started with VCS//SCM
- What is Git, AWS CodeCommit and GitHub?
- About Version Control System and types
- Git Workflow
- Installing on Windows & Linux
- Getting Started with Git Commands
- Working with Branches
- Merging Branches
- Creating and Committing a Pull Request
- Working with Stash

#### Download, Install & Configure Git, & Visual Studio on Windows :


- Download, Install & Configure VSC/SCM CLI Tool i.e. Git on Host Machine
    - https://git-scm.com/
        

- Download, Install & Configure IDE(integrated development environment) Tool on Host Machine
    - https://visualstudio.microsoft.com/


#### What is a Version Control System?

    - A Version Control System (VCS) is a software tool that helps developers manage changes to their code over time. 
    - VCS allows developers to track and record changes made to a project's source code, enabling collaboration and simplifying the process of resolving conflicts between different versions of the same code.

#### Why do we need a Version Control System?

    VCS has become essential in software development for the following reasons:
        - Collaboration: VCS allows multiple developers to work on the same codebase simultaneously, without risking conflicts or losing important code changes.

        - History Tracking: VCS provides a detailed history of all changes made to the code, including who made the changes, when the changes were made, and why they were made.

        - Code Backup: VCS provides a backup of the code at any given point in time, enabling developers to restore a previous version if necessary.

        - Rollback: VCS provides the ability to revert changes, undoing the effects of previous code changes.

#### Types of Version Control Systems

    There are two types of VCS:
    
    1. Centralized Version Control System (CVCS) 
        - In CVCS, there is a central server that stores all code changes made by developers. 
        - Developers checkout code from the server and make changes to their local copies. 
        - After making changes, developers commit the changes to the central server. 
        - Examples of CVCS include Subversion (SVN) and Perforce.

    2. Distributed Version Control System (DVCS)
        - In DVCS, each developer has a local copy of the code, and code changes are synchronized between the local copies. 
        - Each developer can commit code changes to their local copy and push those changes to other developers. 
        - Examples of DVCS include Git and Mercurial.

#### Git Workflows

    1. Centralized Workflow
        In a centralized workflow, there is a single central repository that serves as the "source of truth." Developers clone the repository, make changes locally, and push their changes to the central repository. This workflow is simple and easy to understand, but it can lead to conflicts if multiple developers are working on the same code at the same time.

    2. Feature Branch Workflow
        In a feature branch workflow, each feature or change is developed in a separate branch. Developers clone the repository, create a new branch for their feature, make changes, and submit a pull request to merge their changes back into the main branch. This workflow allows for better collaboration and reduces the risk of conflicts.

    3. Gitflow Workflow
        Gitflow is a branching model that uses two main branches: a master branch for stable releases and a develop branch for ongoing development. Developers create feature branches off the develop branch, make changes, and submit pull requests to merge their changes back into the develop branch. Once the develop branch is stable, it is merged into the master branch for a release. This workflow is well-suited for larger teams working on long-term projects with frequent releases.

    4. Forking Workflow
        In a forking workflow, each developer forks the main repository into their own repository, makes changes in their fork, and submits a pull request to merge their changes back into the main repository. This workflow is useful for open-source projects, as it allows contributors to make changes without needing write access to the main repository.

    Note: These are just a few examples of Git workflows. The specific workflow used may vary depending on the team's needs and preferences. It's important to choose a workflow that fits the team's development process and supports collaboration and communication.
       
#### We'll focus on Git, which is the most widely used DVCS.
    To get started with Git, follow these steps:
        - Install Git
        - The first step is to install Git on your machine. 
        - You can download Git from the official website (https://git-scm.com/downloads).

        Create a Git repository:
            - After installing Git, you can create a new Git repository by running the following command:
            $ git init

        - This command creates a new Git repository in the current directory.

        Add files to the repository:
            - Once you've created a new Git repository, you can add files to it using the following command:
            $ git add <filename>

        This command stages the file for commit. You can stage multiple files at once by specifying their filenames separated by spaces.

        Commit changes:
            - After adding files to the repository, you can commit changes using the following command:
            $ git commit -m "commit message"

            This command commits the changes to the repository along with a descriptive commit message. The commit message should explain the changes made to the code.
        View repository history:
            - You can view the history of the Git repository using the following command:
            $ git log

            This command displays a list of all commits made to the repository, including the commit hash, commit message, and author.
        
        Branching:
            - One of the key features of Git is branching. 
            - A branch is a separate line of development that allows developers to work on new features or bug fixes without affecting the main codebase. 

            To create a new branch, run the following command:
                $ git branch <branchname>

            This command creates a new branch with the specified name. 
            
            To switch to the new branch, run the following command:
                $ git checkout <branchname>

#### Here is a list of some common Git commands:

    git init: Initializes a new Git repository in the current directory.

    git clone: Clones an existing Git repository from a remote location to your local machine.

    git add: Adds changes to the staging area.

    git commit: Commits changes to the repository.

    git status: Shows the status of the working directory and staging area.

    git log: Shows the commit history.

    git branch: Lists all branches in the repository.

    git checkout: Switches to a different branch or commit.

    git merge: Merges changes from one branch into another.

    git pull: Fetches changes from a remote repository and merges them into the local branch.

    git push: Sends changes from the local branch to a remote repository.

    git stash: Saves changes temporarily without committing them.

    git tag: Creates a new tag for a specific commit.

    git remote: Shows the remote repositories linked to the local repository.

    git fetch: Fetches changes from a remote repository without merging them into the local branch.


#### Source Control Management / Version Control System / Source Code Management :
```
Two Solutions :

CLI/CUI : git 

CLI/CUI SCM/VCS :  Git [ Linus Torvalds --> 2005 & Linux Kernel ] --> Ubuntu, Debian, RHEL, CentOS, etc...

GUI :  GitHub, GitLab, BitBucket, AWS CodeCommit, & Azure Repos [ Web-based Git repository hosting service ]

    1. GitHub : 
        - git + GUI 
    
    2. GitLab :
        - git + GUI 
    
    3. BitBucket
        - git + GUI 

    4. AWS CodeCommit
        - git + GUI 
    
    5. Azure Repos 
        - git + GUI 

Public & Private Repositories

GitHub, GitLab, BitBucket 

Private Repositories :

AWS CodeCommit & Azure Repos
```
# ----------------------------------------------------------------- #

Source Control Management / Version Control System / Source Code Management :

CLI : git 

GUI Vendors : 

Public & Private Repositories
    1. github 
    2. gitlab 
    3. bitbucket 

Private Repositories
    4. aws codecommit  
    5. azure repos 

CLI/CUI SCM/VCS :  Git [ Linus Torvalds --> 2005 & Linux Kernel ] --> Ubuntu, Debian, RHEL, CentOS, etc...

GUI SCM/VCS : GitHub, GitLab, BitBucket, AWS CodeCommit & Azure Repos

Software development teams to collaborate communicate in order to
quickly solve problems and deliver new features.

What we store : Source Code / Raw Code

Create a secure repository to store and share your code.

What we do : Public & Private Repositories

GitHub, GitLab, BitBucket [ Web-based Git repository hosting service ]

Private Repositories :

AWS CodeCommit & Azure Repos  [ Web-based Git repository hosting service ]

Distributed Version Control System :

Source Control Management / Source Code Management / Version Control System : 

GIT : Software [ CLI/CUI  ] Public & Private Repositories

Git is a distributed revision control system with an emphasis on speed data integrity and support for distributed non-linear workflows.
Git was initially designed and developed by Linus Torvalds for Linux kernel development in 2005 and has since become the most widely 
adopted version control system for software development.

GITHUB : [ WEB-BASED | GUI ] | Public & Private Repositories
GitHub is a web-based Git repository hosting service which offers all of the distributed revision control and source code management 
(SCM) functionality of Git as well as adding its own features. 

Unlike Git which is strictly a command-line tool GitHub provides a web-based graphical interface and desktop as well as
 mobile integration. GitHub offers both commercial plans and free accounts.

GITLAB SCM : [ WEB-BASED | GUI ] | Public & Private Repositories
GitLab's SCM (source code management) solution supports software development teams to collaborate communicate in order to 
quickly solve problems and deliver new features. GitLab offers both commercial plans and free accounts.

ATLASSIAN BITBUCKET : [ WEB-BASED | GUI ] | Public & Private Repositories
Bitbucket is a web-based hosting service for projects that use either the Mercurial (since launch) or 
Git (since October 2011[1]) revision control systems. Bitbucket offers both commercial plans and free accounts.

AWS CodeCommit : [ WEB-BASED | GUI ] | Private Repositories
    - Create a secure repository to store and share your code.

Azure Repos : [ WEB-BASED | GUI ] | Private Repositories


https://education.github.com/git-cheat-sheet-education.pdf

https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

https://about.gitlab.com/images/press/git-cheat-sheet.pdf

https://ndpsoftware.com/git-cheatsheet.html#loc=index;
