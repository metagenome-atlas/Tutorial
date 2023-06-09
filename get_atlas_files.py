

import os
import yaml
import paramiko
import stat

# Define your output directory and base path on server
output_dir = 'NewExample'
base_path_server = '/gpfs/home/rdkiesersi1/s/MD'

# Load and parse the yaml file
with open('atlas_output_files.yaml') as file:
    file_dict = yaml.safe_load(file)["v2.16"]

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server (replace 'ssh_alias' with your SSH alias)
    ssh.connect('gate.nihs.ch.nestle.com',username="rdkiesersi1")
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    exit(1)

# Create an SFTP client
sftp = ssh.open_sftp()



import os
import yaml
import paramiko

# Define your output directory and base path on server
output_dir = 'NewExample'
base_path_server = '/gpfs/home/rdkiesersi1/s/MD'

# Load and parse the yaml file
with open('atlas_output_files.yaml') as file:
    file_dict = yaml.safe_load(file)["v2.16"]

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server (replace 'ssh_alias' with your SSH alias)
    ssh.connect('gate.nihs.ch.nestle.com',username="rdkiesersi1")
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    exit(1)

# Create an SFTP client
sftp = ssh.open_sftp()

# Function to download files
def download_file(remote_file_path):
    # Create full path on server
    full_remote_path = f"{base_path_server}/{remote_file_path}"
    # Create full local path
    local_file_path = os.path.join(output_dir, remote_file_path.replace('/', os.sep))
    local_file_dir = os.path.dirname(local_file_path)

    # Check if the file already exists locally
    if os.path.exists(local_file_path):
        print(f"{local_file_path} already exists. Skipping download.")
        return

    try:
        # Check if the remote file exists
        sftp.stat(full_remote_path)

        # Create local directory structure if it doesn't exist
        os.makedirs(local_file_dir, exist_ok=True)

        # Download the file
        sftp.get(full_remote_path, local_file_path)
    except IOError:
        print(f"{full_remote_path} does not exist on the remote server. Skipping download.")
    except Exception as e:
        print(f"Failed to download {full_remote_path}: {e}")


# Go through the parsed yaml data and download the files
for key1, value1 in file_dict.items():
    if isinstance(value1, str):
        # It's a direct path, download the file
        download_file(value1)
    elif isinstance(value1, dict):
        # It's a nested dictionary, go deeper
        for _, value2 in value1.items():
            download_file(value2)


# Close the connections
sftp.close()
ssh.close()
