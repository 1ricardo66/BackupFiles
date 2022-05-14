import json
import paramiko
import warnings
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)


jsonArchive = open("data.json", encoding='utf-8')


file = json.load(jsonArchive)
dictFile = dict()

for i in range(len(file)):
    dictFile[i] = file[i]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
command = "export"
for i in dictFile:
    host = dictFile[i].get("host")
    username = dictFile[i].get("username")
    password = dictFile[i].get("password")
    name = dictFile[i].get("name")
    ssh.connect(host, 22, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    backupArchive = open("/home/ricardo/Documentos/PythonProjects/BackupFiles/backup.txt"+str(i),"w")
    lines = stdout.readlines()
    doc = ' '.join(lines)
    backupArchive.write(doc)
    backupArchive.close()
    print(lines)

print(host)


