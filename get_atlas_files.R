# Required packages
library(yaml)
library(ssh)
library(fs)

# Define your output directory and base path on server
output_dir <- "/path/to/your/local/directory"
base_path_server <- "/path/to/server/base"
ssh_server <- "username:password@hostname"
atlas_version <- "v2.26"


# Load and parse the yaml file
file_dict <- yaml.load_file("atlas_output_files.yaml")[[atlas_version]]

# Create an SSH session (replace 'ssh_alias' with your SSH alias)
session <- ssh_connect(ssh_server)

# Function to download files or directories
download <- function(remote_path) {
    # Create full path on server
    full_remote_path <- file.path(base_path_server, remote_path, fsep = "/")
    # Create full local path
    local_path <- file.path(output_dir, remote_path)

    # Check if the file already exists locally
    if (dir.exists(local_path) || file.exists(local_path)) {
        print(paste(local_path, "already exists. Skipping download."))
        return(NULL)
    }

    tryCatch(
        {
            # Create local directory structure if it doesn't exist
            dir.create(dirname(local_path), recursive = TRUE, showWarnings = FALSE)

            # Download the file or directory
            scp_download_dir(session, full_remote_path, local_path)
        },
        error = function(e) {
            print(paste("Failed to download", full_remote_path, ":", e$message))
        }
    )
}


# Go through the parsed yaml data and download the files
for (key1 in names(file_dict)) {
    value1 <- file_dict[[key1]]
    if (is.character(value1)) {
        # It's a direct path, download the file
        download(value1)
    } else if (is.list(value1)) {
        # It's a nested list, go deeper
        for (value2 in value1) {
            download(value2)
        }
    }
}

# Close the SSH session
ssh_disconnect(session)
