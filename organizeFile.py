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
""" 

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

"""

routerName = ""
def routerSelection(name, idArray):
    #routerName = name[idArray].get("name")
    #print(routerName)
    if(name[idArray].get("name") == "Mikrotik"):
        print("Working")
        return backupMikrotik(name,idArray)

    else:
        return ""

def backupMikrotik(data,idArray):
    host = data[idArray].get("host")
    username = data[idArray].get("username")
    password = data[idArray].get("password")
    name = data[idArray].get("name")
    ssh.connect(host, 22, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    doc = ' '.join(lines)
    stdin, stdout, stderr = ssh.exec_command("system identity print")
    lines = stdout.readlines()
    lines = str(lines[0])
    backupArchive = open("/home/ricardo/Documentos/PythonProjects/BackupFiles/"+lines.strip("name: ")+".txt","w")
    
    backupArchive.write(doc)
    backupArchive.close()
    print(i)


def exec():
    for i in dictFile:
        routerSelection(dictFile,i)

        