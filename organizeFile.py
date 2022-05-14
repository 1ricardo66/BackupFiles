import json
import paramiko
import warnings
from datetime import datetime
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)

date = str(datetime.date(datetime.now()))
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

    try:

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
        print(date)
        dateAndName = "Backup-"+lines.strip("name: ")+"-"+date+".txt"
        path = "/home/ricardo/Documentos/PythonProjects/BackupFiles/"+dateAndName 
        backupArchive = open(path,"w")
        
        backupArchive.write(doc)
        backupArchive.close()
        print(i)
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed")


def exec():
    for i in dictFile:
        routerSelection(dictFile,i)

        