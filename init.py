#!/usr/bin/env python3 -i

from lib2to3.pgen2.token import COLONEQUAL
from multiprocessing.connection import wait
import sys
import os
import subprocess
import pkg_resources

required = {'keyring', 'termcolor', 'discord'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# ///// ///// ///// ///// /////

import keyring
import keyring.util.platform_ as keyring_platform
import uuid
from termcolor import colored, cprint

ENTRY = str(uuid.uuid1())
NAMESPACE = 'InforiaMX'
cred = keyring.get_credential(NAMESPACE, ENTRY)

# ///// ///// ///// ///// /////

os.system('color')
print(colored('Welcome to InforiaMX!', 'cyan', attrs=['underline']))
NAMESPACE = "InforiaMX-DC1"
if cred.password is not None:
    print(colored('PROFILE', 'cyan', 'on_white'), colored('Discord #1 detected', 'white'))
    import discord
    from discord.ext import commands
    client = commands.Bot(command_prefix=".", self_bot=True, help_command=None, intents=discord.Intents.all())
    intents = discord.Intents.default()
    intents.members = True

    @client.event
    async def on_ready():
        print(colored('PROFILE', 'cyan', 'on_white'), colored('Discord #1 has been activated', 'white'))
        print(colored('DISCORD', 'white', 'on_magenta'), colored('Logged in as {0.user}'.format(client), 'yellow'))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        #print('Message from {0.author}: {0.content}'.format(message))
        if message.guild is None:
            print(colored('DISCORD', 'white', 'on_magenta'), colored('Direct Message', 'magenta', 'on_white'), colored(message.author, 'yellow'), colored(message.content, 'white'))
        else:
            print(colored('DISCORD', 'white', 'on_magenta'), colored(message.guild, 'blue'), colored(message.channel, 'cyan'), colored(message.author, 'yellow'), colored(message.content, 'white'))

        #if message.content.startswith('$hello'):
            #await message.channel.send('Hello!')
            
    client.run("TOKEN_HERE", bot=False)





#keyring.set_password(NAMESPACE, ENTRY, "API_KEY")
#print(keyring.get_password(NAMESPACE, ENTRY))
# API_KEY

#cred = keyring.get_credential(NAMESPACE, ENTRY)
#print(f"Password for username {cred.username} in namespace {NAMESPACE} is {cred.password}")
# Password for username API_KEY in namespace my-app is API_KEY

#while True:
    #wait