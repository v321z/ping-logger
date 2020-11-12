import discord
import time
import datetime
import asyncio
from colorama import Fore
import os
import requests
from discord.ext import commands
from discord.utils import get
from os import system
from discord.ext import commands
from random import choice as randchoices
import platform
### i dont think i need all these import made this at night time lol







token = input("Enter token you wanna host : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)


if src.status_code == 200:
    print('Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
    input("Press any key")




client = commands.Bot(command_prefix=".", self_bot=True)
ready = False

system('title ' + 'LOGGER')

start_time = datetime.datetime.utcnow()

BOT_PREFIX = 'x'






client = commands.Bot(command_prefix=BOT_PREFIX, self_bot=True)








system('title ' + ' lol')

start_time = datetime.datetime.utcnow()
os = platform.system()

if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(f'''{Fore.RED}



             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    


══════════════════════════════════════════════════
    MENTION LOGGER: ENABLED                                                  
══════════════════════════════════════════════════


   
                           ''' + Fore.RESET)
@client.event
async def on_connect():
    
    print(
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Version: {discord.__version__}\n'
    )





















###HELP EMBED 





client.remove_command('help')



























                          



@client.listen('on_message')
async def ifmentioned(message):
    if message.author == client.user:
        return
    if str(client.user.id) in message.content:
        print("══════════════════════════════════════════════════")
        print(Fore.RED + "[Mentioned] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"You were mentioned by {message.author} ." + Fore.RESET)
        print(Fore.BLUE + "[Mentioned] " + Fore.RESET + Fore.RED + f"Server: {message.guild}" + Fore.RESET)
        print(Fore.BLUE + "[Mentioned] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}")
        print(Fore.RED + "[Mentioned] " + Fore.RESET + Fore.WHITE + f"Message Content: {message.content}".replace(f"<@{client.user.id}>" or f"<@!{client.user.id}>", "") + Fore.RESET)
        print("══════════════════════════════════════════════════")












#####################################################SELFBOT COMMANDS WILL BE WORKED ON LATER ON to lazy rn






client.run(token, bot=False)
