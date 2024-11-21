#### Session Video:
```
https://drive.google.com/file/d/1ZccMDLpvMAx0GAylRTzPU8d5iEVPSCeX/view?usp=sharing

https://github.com/kesavkummari/javaproject
```

#### Configuration Management Tools:

```
https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/url_test.html

https://galaxy.ansible.com/ui/standalone/roles/oasis_roles/jbosseap/


```

#### Ansible Windows Node Setup

Setting up a Windows node with Ansible involves installing and configuring the necessary components on both the Ansible control machine and the Windows target node. Here's a guide to help you get started:

#### Step 1: Setting Up the Ansible Control Machine
```
Install Ansible:
    - On most Linux distributions, you can install Ansible with package managers like apt, yum, or dnf.

    - To use Ansible with Windows nodes, ensure you're running a recent version of Ansible (at least 2.10), as this provides better Windows support.

    $ sudo apt update
    $ sudo apt install ansible
```

```
Install Additional Dependencies:
    - Ansible uses the pywinrm package to communicate with Windows nodes over WinRM (Windows Remote Management). 
    - Install it to ensure connectivity with Windows nodes.

    $ sudo apt-get install python3-pip
    $ pip install pywinrm

```

#### Step 2: Configuring the Windows Target Node

```
To allow Ansible to manage a Windows system, you need to enable and configure WinRM.

Enable WinRM:
    - Open a PowerShell window with administrative privileges.
    - Run the following command to configure WinRM for basic communication and set up the required listener:

    $ https://github.com/ansible/ansible-documentation/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1
    $ ./ConfigureRemotingForAnsible.ps1
    $ winrm quickconfig -q
    $ winrm set winrm/config/service '@{AllowUnencrypted="true"}'
    $ winrm set winrm/config/service/auth '@{Basic="true"}'

Note: If you'd prefer encrypted communication, additional steps are needed to configure HTTPS for WinRM.


Set Up Remote Administrator Account:
    - Ensure there's an account with administrator privileges that Ansible can use to manage the node. 
    - You can use a local account or a domain account if you're in a Windows domain environment.

Optional Security Configurations:
    - For production environments, consider securing WinRM:
    - Use HTTPS with a trusted certificate.
    - Restrict access to specific IPs.
    - Limit allowed commands and users with Group Policy or other Windows security tools.

```

#### Step 3: Testing Ansible Connection to Windows Node

```
Create an Inventory File:
    - Create an inventory file (inventory.ini, for example) with your Windows node information:


[windows]
win_node ansible_host=192.168.1.100 
ansible_user=your_user 
nsible_password=your_password 
ansible_port=5985 
nsible_connection=winrm


Test the Connection:
    - Use the ansible command to test connectivity:
        
        $ ansible -i inventory.ini windows -m win_ping

```

#### Step 4: Using Ansible to Manage the Windows Node

```
    - After setting up and testing the connection, you can create playbooks to manage the Windows node. 

    - Here's a simple example that installs a Windows feature:

- name: Install a Windows Feature
  hosts: windows
  tasks:
    - name: Install IIS
      win_feature:
        name: Web-Server
        state: present

```
#### Conclusion
```
    - With these steps, you should be able to set up an Ansible control machine and a Windows target node for Ansible management. 
    
    - For more advanced configurations and Windows security best practices, consult Ansible documentation and Windows administration resources.
```
