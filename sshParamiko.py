import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.56.105',username='kali', password='kali')

stdin,stdout,stderr = ssh.exec_command('cd Desktop && pwd && ls')

print(stdout.read().decode())

ssh.close()

