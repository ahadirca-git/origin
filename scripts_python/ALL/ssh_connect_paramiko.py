import os.path
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("t1.dev.noction.com", username="root",
            key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_ed25519"))

stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.readlines())
ssh.close()

