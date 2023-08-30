#!/usr/bin/env python

import os
import yaml
import paramiko
import stat

from paramiko import RSAKey


connection_details_file=".connection_details.yaml"

default_values = {
    "output_dir": 'atlas_data',
    "atlas_version": "v2.17",
    "username": "me",
    "server":"myserver.server.com",
    "base_path_server": '/home/user/my_atlas_run',
    "private_key_path": None # "C:/Users/User/.ssh/id_rsa"
}





if os.path.exists(connection_details_file):

    with open(connection_details_file) as file:
        connection_dict = yaml.safe_load(file)
    
    # load all values as variables in the current namespace
    for key, value in connection_dict.items():

        print(f'{key} = "{value}"')
        exec(f'{key} = value')

else:
    # ask for the values via the command line and store them in the connection details file, propose default values

    with open(connection_details_file, 'w') as file:
        yaml.dump(default_values, file)

    print(f"Please fill in the connection details in the file {connection_details_file} and run the script again.")
    exit(1)

    



if private_key_path is None:

    mykey = None
else:
    mykey = RSAKey(filename=private_key_path)




# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server (replace 'ssh_alias' with your SSH alias)
    ssh.connect(server,username=username,pkey=mykey)
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    exit(1)

# Create an SFTP client
sftp = ssh.open_sftp()



# Function to download files
def download(remote_path):
    # Create full path on server
    full_remote_path = f"{base_path_server}/{remote_path}"
    # Create full local path
    local_path = os.path.join(output_dir, remote_path.replace('/', os.sep))

    try:
        # Check if the remote path is a file or a directory
        file_stat = sftp.stat(full_remote_path)

        if not stat.S_ISDIR(file_stat.st_mode):  # If it's a file...
            # Check if the file already exists locally
            if os.path.exists(local_path):
                print(f"{local_path} already exists. Skipping download.")
            else:
                # Create local directory structure if it doesn't exist
                os.makedirs(os.path.dirname(local_path), exist_ok=True)

                # Download the file
                sftp.get(full_remote_path, local_path)

                print(f"{local_path} downloaded!")

        else:  # If it's a directory...
            # Create local directory if it doesn't exist
            os.makedirs(local_path, exist_ok=True)

            # List all files and directories in the remote directory
            for filename in sftp.listdir(full_remote_path):
                # Recursively download the file or directory
                download(f"{remote_path}/{filename}")

    except IOError:
        print(f"{full_remote_path} does not exist on the remote server. Skipping download.")
    except Exception as e:
        print(f"Failed to download {full_remote_path}: {e}")




# Load and parse the yaml file
with open('atlas_output_files.yaml') as file:
    file_dict = yaml.safe_load(file)[atlas_version]

# Go through the parsed yaml data and download the files
for key1, value1 in file_dict.items():
    if isinstance(value1, str):
        # It's a direct path, download the file
        download(value1)
    elif isinstance(value1, dict):
        # It's a nested dictionary, go deeper
        for _, value2 in value1.items():
            download(value2)


# Close the connections
sftp.close()
ssh.close()
