# Enhanced-Distributed-File-System 
## Client-Server File Management System

A simple client-server application allowing users to interact with files stored on a server. The application supports basic file operations such as creating, reading, writing, deleting, listing, renaming files, and changing directories.

## Features
- **Client-Server Architecture**: Multiple server instances (`Server1`, `Server2`, `Server3`) that communicate with the client.
- **File Management**: Create, delete, rename, read, write, and list files in the server's directories.
- **Encryption**: Passwords are hashed using MD5 for secure user authentication.
- **File Communication**: Data sent between client and server is encrypted with RSA encryption.

## Installation

### Prerequisites
- Python 3.x
- `rsa` library (Install via `pip install rsa`)
- `configparser` library (Install via `pip install configparser`)

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/repository-name.git
    cd repository-name
    ```

2. Install the required dependencies:
    ```bash
    pip install rsa configparser
    ```

3. Create a new user and set up authentication (optional):
    - Run `client.py` and follow the prompts to create a new user.

## Usage

### Starting the Servers
1. Open three terminal windows.
2. In each terminal, run the respective server script:
    ```bash
    python server1.py
    python server2.py
    python server3.py
    ```

### Running the Client
1. In a separate terminal window, run the `client.py` script:
    ```bash
    python client.py
    ```

2. The client will prompt for commands. Some example commands:
    - `ls`: Lists the files in the current directory.
    - `create <filename>`: Creates a new file with the specified name.
    - `read <filename>`: Reads the content of a file.
    - `write <filename>`: Writes content into a file.
    - `delete <filename>`: Deletes the specified file.
    - `rename <filename>`: Renames a file.
    - `cd <directory>`: Changes the directory.
    - `mkdir <directory_name>`: Creates a new directory.

### Encryption
- Passwords are encrypted with MD5 for storage.
- File data is transmitted securely using RSA encryption.

## Acknowledgments

- The project demonstrates a basic client-server model.
- File operations are performed with a focus on simplicity and clarity.
