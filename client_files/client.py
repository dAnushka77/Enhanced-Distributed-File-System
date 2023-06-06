import hashlib
import socket
import os
import sys
import time
import re
import getpass
from configparser import ConfigParser
import rsa

def send_to_all_servers(client_message, content):
    message_recv_from_server1 = send_data_to_server1(content)
    message_recv_from_server2 = send_to_server2(client_message, content)
    # message_recv_from_server3 = send_to_server3(client_message, content)
    return message_recv_from_server1, message_recv_from_server2


def send_to_server1(message):
    # HOST = '10.200.137.77'
    # HOST = socket.gethostbyname(socket.gethostname())
    host = socket.gethostbyname('localhost')
    port = 9090
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((host, port))
    s_socket.send(message.encode('utf-8'))
    message_recv_from_server = None
    if (message.split('|')[0] in ["ls"]) or (
            message.split(' ')[0] in ["create", "read", "cd", "delete", "mkdir", "write", "rename"]):
        if message.split(' ')[0] == "read":
            message_recv_from_server = s_socket.recv(1024)
        else:
            message_recv_from_server = s_socket.recv(1024).decode('utf-8')
    s_socket.close()
    return message_recv_from_server

def send_data_to_server1(content):
    # HOST = '10.200.137.77'
    # HOST = socket.gethostbyname(socket.gethostname())
    host = socket.gethostbyname('localhost')
    port = 9090
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((host, port))
    encrypted_content = rsa.encrypt(content.encode(), publicKey)
    s_socket.send(encrypted_content)

    message_recv_from_server = None
    message_recv_from_server = s_socket.recv(1024)
    s_socket.close()
    return message_recv_from_server

def send_to_server2(client_message, content):
    try:
        # print("attempt to connecting from client")
        host = socket.gethostbyname('localhost')
        port = 9091
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_socket.connect((host, port))
        status2 = ('Client Connected to Server2', 'Server2')
        print(status2[0], status2[1])

        command = client_message + ' | ' + content
        s_socket.send(command.encode('utf-8'))
        response = s_socket.recv(1024).decode('utf-8')
        # if (message.split('|')[0] in ["ls"]) or (message.split(' ')[0] in ["read", "cd", "delete", "mkdir", "write", "rename"]):
        #    response = s_socket.recv(1024).decode('utf-8')
        # else:
        #    response = None
        time.sleep(1)
        s_socket.close()
        return response
    except ConnectionRefusedError:
        status2 = ('Could not connect to Server2', 'Server2')
        print(status2[0], status2[1])


def send_to_server3(client_message, content):
    try:
        host = socket.gethostbyname('localhost')
        port = 9092
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_socket.connect((host, port))
        status3 = ('Client Connected to Server3', 'Server3')
        print(status3[0], status3[1])
        command = client_message + ' | ' + content
        s_socket.send(command.encode('utf-8'))
        response = s_socket.recv(1024).decode('utf-8')
        # if (message.split('|')[0] in ["ls"]) or (message.split(' ')[0] in ["read", "cd", "delete", "mkdir", "write", "rename"]):
        #    response = s_socket.recv(1024).decode('utf-8')
        # else:
        #    response = None
        time.sleep(1)
        s_socket.close()
        return response
    except ConnectionRefusedError:
        status3 = ('Could not connect to Server3', 'Server3')
        print(status3[0], status3[1])

def encrypting_pwd(word):

    result = hashlib.md5(word.encode())

    # printing the equivalent hexadecimal value.
    # print("The hexadecimal equivalent of hash is : ")
    return result.hexdigest()

def creating_new_user():
    config = ConfigParser()
    config.read('auth.ini')
    username_list = list(config['AUTHENTICATION'])
    username = input("please enter your new username: ")
    if username in username_list:
        print("Error creating new user. user already exists!")
        sys.exit()
    pwd = input("please enter your new password: ")
    enc_pwd = encrypting_pwd(pwd)
    config.set('AUTHENTICATION', username, enc_pwd)

    with open('auth.ini', 'w') as configfile:
        config.write(configfile)

def main():
    global publicKey, privateKey
    publicKey, privateKey = rsa.newkeys(1024)

    """config = ConfigParser()
    config.read('auth.ini')

    username_list = list(config['AUTHENTICATION'])
    print("username: ", username_list)
    existing_user = input("Existing user? Y/N: ")
    if existing_user != 'Y':
        print('Please create a new user')
        creating_new_user()
    user_status = 'Not Verified'
    attempt = 0
    while user_status == 'Not Verified':
        username = input("Enter Your Username : ")
        password_bfr = getpass.getpass("Enter Your Password : ")
        password = encrypting_pwd(password_bfr)
        attempt += 1

        if (username in username_list) and (password == config['AUTHENTICATION'][username]):
            user_status = 'Verified user'
        else:
            print("1 Please enter a valid password.You have " + str(3 - attempt) + " left.")
        if attempt == 3:
            print("Your access has been denied. Please try again.")
            sys.exit()"""
    while True:
        print("Hello..")

        client_message = input("Enter the command you want to perform: ")
        message_recv_from_server = send_to_server1(client_message)
        print(message_recv_from_server)
        client_message_0 = client_message.split()[0]

        if client_message_0 == "ls":
            print("The list of existing files: ", message_recv_from_server)
        if client_message_0 == "create":
            message_recv_from_server = send_to_server2(client_message, "None")
            message_recv_from_server = send_to_server3(client_message, "None")
            print(message_recv_from_server)
        if client_message_0 == "delete":
            message_recv_from_server = send_to_server2(client_message, "None")
            message_recv_from_server = send_to_server3(client_message, "None")
            print(message_recv_from_server)
        if client_message_0 == "read":
            message_recv_from_server2 = send_to_server2(client_message, "None")
            message_recv_from_server3 = send_to_server3(client_message, "None")
            decrypted_message = rsa.decrypt(message_recv_from_server, privateKey)
            print(decrypted_message)
        if client_message_0 == "write" and message_recv_from_server not in ("Access denied", "File doesn't exist"):
            content = input()
            message_recv_from_server = send_to_all_servers(client_message, content)
            print(message_recv_from_server)
        if client_message_0 == "rename":
            new_name = input()
            send_to_server1(new_name)
        if client_message_0 == "cd":
            print(message_recv_from_server)
        if client_message_0 == "mkdir":
            print(message_recv_from_server)


if __name__ == "__main__":
    main()
