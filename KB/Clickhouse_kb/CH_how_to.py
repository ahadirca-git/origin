import os.path
import time
import paramiko
ssh = paramiko.SSHClient()
keypassword=input("introdu key password: ")
eval_host = input("introdu eval: ")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(eval_host, username="root",key_filename="/home/alexandru/.ssh/id_ed25519", password=keypassword)
stdin, stdout, stderr = ssh.exec_command('apt-get update')
time.sleep(540)
stdin.close()
print(stdout.read())
print(stderr.read())
print(stdin.read())
SystemExit
ssh.close()