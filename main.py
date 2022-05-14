import organizeFile
host = "192.168.3.20"
username = "admin"
password = ""
port = 22
command = "export"

file = open("/home/ricardo/Documentos/Backup/mikrotik.txt","w")

ssh = organizeFile.paramiko.SSHClient()

ssh.set_missing_host_key_policy(organizeFile.paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)

lines = stdout.readlines()
doc = ' '.join(lines)
file.write(doc)
file.close()
print(lines)
