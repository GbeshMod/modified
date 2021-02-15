
import os
import sys
import random
import asyncio
from telethon import events






@bot.on(admin_cmd(pattern=f"quickheal$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"quickheal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(0, 11)
    event = await edit_or_reply(event, "quickheal..")
    animation_chars = [
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\Result: No Virus Found...`",
        ]

        for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])



@bot.on(admin_cmd(pattern=f"vquickh$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"vquickh$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(0, 11)
    event = await edit_or_reply(event, "Downloading Files....")
    animation_chars = [
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult:⚠️Virus Found⚠️\nMore Info: Trojan, Spyware, Adware, Ransomware`",
        ]

        for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])



@borg.on(admin_cmd(pattern="hackw ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 0.7

    animation_ttl = range(0, 11)

    
    await event.edit("Python Whatsapp Installing...")

    animation_chars = [
        
            "`Installing Files To Hacked Private Server...`",
            "`Target Selected.`",
            "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 84%\n█████████████████████▒▒▒▒ `",
            "`Installing... 100%\n████████Installed██████████ `",
            "`Target files Uploading...\n\nDirecting To Remote  server to hack..`"
        ]
  
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
         # Made for GbeshMod
        await event.edit(animation_chars[i % 11])

    await asyncio.sleep(2)

    animation_interval = 0.6
    animation_ttl = range(0,14)
    await event.edit("Connecting nd getting combined token from api.whatsapp.com ")
    await asyncio.sleep(1)
    animation_chars = [
            "`root@anon:~#` ",
            "`root@anon:~# ls`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~#`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# `",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...\n\nAll Done!`",
            "root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected  in ghost ...\n\nAll Done!\nInstalling Token!\nToken=`Mng6hulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
          # Modified by Gβε₷Ἥ   
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
    
    await asyncio.sleep(2)

    await event.edit("`starting Whatsapp hack`")
    await asyncio.sleep(1)
    await event.edit("`Hacking... 0%completed.\nTERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (1.3) kB`")#credit to kraken,sawan
    await asyncio.sleep(2)
    await event.edit(" `Hacking... 4% completed\n TERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Package`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....6% completed\n TERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....8%completed\n TERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking....15%completed\n Terminal:chat history from Whatsapp exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installing`")
    await asyncio.sleep(1)
    await event.edit("`hacking....24%completed\n TERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\nerminal:chat history from Whatsapp exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creting data into pdf`")
    await asyncio.sleep(1)
    await event.edit("`hacking....32%completed\n looking for use history \n downloading-Whatsapp -id prtggtgf . gfr (12.99 mb)\n collecting data starting imprute attack to user account\n chat history from Whatsapp exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creted data into pdf\nDownload sucessful Bruteforce-Whatsapp-0.1.tar.gz (1.3)`")
    await asyncio.sleep(1)
    await event.edit("hacking....38%completed\n\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Whatsapp-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB): finished with status 'done'\nCreated wheel for Whatsapp: filename=Whatsapp-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e`")
    await asyncio.sleep(1)
    await event.edit("`hacking....52%completed\nexterting data from Whatsapp private server\ndone with status 36748hdeg \n checking for more data in device`")
    await asyncio.sleep(2)
    await event.edit("`hacking....60%completed\nmore data found im target device\npreparing to download data\n process started with status 7y75hsgdt365ege56es \n status changed to up`")
    await asyncio.sleep(1)
    await event.edit("`hacking....73% completed\n downloading data from device\n process completed with status 884hfhjh\nDownloading-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking...88%completed\nall data from Whatsapp private server downloaded\nterminal download sucessfull--with status jh3233fdg66y yr4vv.irh\n data collected from tg-bot\nTERMINAL:\n Bruteforce-Whatsapp-0.1.tar.gz (1.3)downloaded`")
    await asyncio.sleep(.5)
    await event.edit("`100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Whatsapp-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Whatsapp-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for Whatsapp: filename=Whatsapp-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `")
    await asyncio.sleep(2)
    await event.edit("`accoount hacked\n collecting all data\n compressing data and auto~rename  into (hack($.`0-9)).rar if Hack.rar already   exists`")
    await asyncio.sleep(1)
    h=(random.randrange(1,5)) 
    if h==1:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and Compress Private Whatsapp files......` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==2:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and Compress Private Whatsapp files......` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==3:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and Compress Private Whatsapp files......` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==4:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and Compress Private Whatsapp files......` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==5:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and Compress Private Whatsapp files......` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")


@borg.on(admin_cmd(pattern="hackt ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 0.7

    animation_ttl = range(0, 11)

    
    await event.edit("Python Telegram Installing...")

    animation_chars = [
        
            "`Installing Files To Hacked Private Server...`",
            "`Target Selected.`",
            "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 84%\n█████████████████████▒▒▒▒ `",
            "`Installing... 100%\n████████Installed██████████ `",
            "`Target files Uploading...\n\nDirecting To Remote  server to hack..`"
        ]
  
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
          # Made for GbeshMod
        await event.edit(animation_chars[i % 11])

    await asyncio.sleep(2)

    animation_interval = 0.6
    animation_ttl = range(0,14)
    await event.edit("Connecting nd getting combined token from my.telegram.org ")
    await asyncio.sleep(1)
    animation_chars = [
            "`root@anon:~#` ",
            "`root@anon:~# ls`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~#`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# `",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...\n\nAll Done!`",
            "root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected  in ghost ...\n\nAll Done!\nInstalling Token!\nToken=`DJ65gulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
            # Modified by Gβε₷Ἥ   
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
    
    await asyncio.sleep(2)

    await event.edit("`starting telegram hack`")
    await asyncio.sleep(1)
    await event.edit("`Hacking... 0%completed.\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB`")#credit to kraken,sawan
    await asyncio.sleep(2)
    await event.edit(" `Hacking... 4% completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....6% completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....8%completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking....15%completed\n Terminal:chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installing`")
    await asyncio.sleep(1)
    await event.edit("`hacking....24%completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\nerminal:chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creting data into pdf`")
    await asyncio.sleep(1)
    await event.edit("`hacking....32%completed\n looking for use history \n downloading-telegram -id prtggtgf . gfr (12.99 mb)\n collecting data starting imprute attack to user account\n chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creted data into pdf\nDownload sucessful Bruteforce-Telegram-0.1.tar.gz (1.3)`")
    await asyncio.sleep(1)
    await event.edit("hacking....38%completed\n\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e`")
    await asyncio.sleep(1)
    await event.edit("`hacking....52%completed\nexterting data from telegram private server\ndone with status 36748hdeg \n checking for more data in device`")
    await asyncio.sleep(2)
    await event.edit("`hacking....60%completed\nmore data found im target device\npreparing to download data\n process started with status 7y75hsgdt365ege56es \n status changed to up`")
    await asyncio.sleep(1)
    await event.edit("`hacking....73% completed\n downloading data from device\n process completed with status 884hfhjh\nDownloading-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking...88%completed\nall data from telegram private server downloaded\nterminal download sucessfull--with status jh3233fdg66y yr4vv.irh\n data collected from tg-bot\nTERMINAL:\n Bruteforce-Telegram-0.1.tar.gz (1.3)downloaded`")
    await asyncio.sleep(.5)
    await event.edit("`100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `")
    await asyncio.sleep(2)
    await event.edit("`accoount hacked\n collecting all data\n compressing data and auto~rename  into (hack($.`0-9)).rar if Hack.rar already   exists`")
    await asyncio.sleep(1)
    h=(random.randrange(1,5)) 
    if h==1:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==2:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==3:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==4:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==5:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")


@borg.on(admin_cmd(pattern="hack ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 0.7

    animation_ttl = range(0, 11)

    
    await event.edit("Installing..")

    animation_chars = [
        
            "`Installing Files To Hacked Private Server...`",
            "`Target Selected.`",
            "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Installing... 84%\n█████████████████████▒▒▒▒ `",
            "`Installing... 100%\n████████Installed██████████ `",
            "`Target files Uploading...\n\nDirecting To Remote  server to hack..`"
        ]
  
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
          # Made for GbeshMod
        await event.edit(animation_chars[i % 11])

    await asyncio.sleep(2)

    animation_interval = 0.6
    animation_ttl = range(0,14)
    await event.edit("Connecting nd getting combined token from my.telegram.org ")
    await asyncio.sleep(1)
    animation_chars = [
            "`root@anon:~#` ",
            "`root@anon:~# ls`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~#`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# `",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...`",
            "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...\n\nAll Done!`",
            "root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected  in ghost ...\n\nAll Done!\nInstalling Token!\nToken=`DJ65gulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
           # Modified by Gβε₷Ἥ   
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
    
    await asyncio.sleep(2)

    await event.edit("`starting telegram hack`")
    await asyncio.sleep(1)
    await event.edit("`Hacking... 0%completed.\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB`")#credit to kraken,sawan
    await asyncio.sleep(2)
    await event.edit(" `Hacking... 4% completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....6% completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished`")
    await asyncio.sleep(1)
    await event.edit("`hacking.....8%completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking....15%completed\n Terminal:chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installing`")
    await asyncio.sleep(1)
    await event.edit("`hacking....24%completed\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target account chat\n lding chat tg-bot bruteforce finished\nerminal:chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creting data into pdf`")
    await asyncio.sleep(1)
    await event.edit("`hacking....32%completed\n looking for use history \n downloading-telegram -id prtggtgf . gfr (12.99 mb)\n collecting data starting imprute attack to user account\n chat history from telegram exporting to private database.\n terminal 874379gvrfghhuu5tlotruhi5rbh installed\n creted data into pdf\nDownload sucessful Bruteforce-Telegram-0.1.tar.gz (1.3)`")
    await asyncio.sleep(1)
    await event.edit("hacking....38%completed\n\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e`")
    await asyncio.sleep(1)
    await event.edit("`hacking....52%completed\nexterting data from telegram private server\ndone with status 36748hdeg \n checking for more data in device`")
    await asyncio.sleep(2)
    await event.edit("`hacking....60%completed\nmore data found im target device\npreparing to download data\n process started with status 7y75hsgdt365ege56es \n status changed to up`")
    await asyncio.sleep(1)
    await event.edit("`hacking....73% completed\n downloading data from device\n process completed with status 884hfhjh\nDownloading-0.1.tar.gz (9.3 kB)\nCollecting Data Packageseeing target\n lding chat tg-bot bruteforce finished\n creating pdf of chat`")
    await asyncio.sleep(1)
    await event.edit("`hacking...88%completed\nall data from telegram private server downloaded\nterminal download sucessfull--with status jh3233fdg66y yr4vv.irh\n data collected from tg-bot\nTERMINAL:\n Bruteforce-Telegram-0.1.tar.gz (1.3)downloaded`")
    await asyncio.sleep(.5)
    await event.edit("`100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `")
    await asyncio.sleep(2)
    await event.edit("`accoount hacked\n collecting all data\n compressing data and auto~rename  into (hack($.`0-9)).rar if Hack.rar already   exists`")
    await asyncio.sleep(1)
    h=(random.randrange(1,5)) 
    if h==1:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==2:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==3:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==4:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")
    if h==5:
        await event.edit("`rar file created click link below to download data\n\n😂 Don't worry only i can open this 😎😎.. It encrypted and compress..` 🙂\n\nhttps://drive.google.com/file/d/1ccKHvGP285v6M-nXMOY0_GioOQoDA6xP/view?usp=sharing")

    
CMD_HELP.update(
    {
        "hack": "**Hack**\
\n\n**Syntax : **`.hack <reply to your friend>`\
\n**Usage :** prank your friends with this hacking plugin\
\n**Syntax :** .hackw this hacking Whatsapp \
\n**Syntax :** .hackt this hacking Telegram\
\n try  .help quickheal .quickh & .vquickh"
    }
)


CMD_HELP.update(
    {
        "quickheal": "**Quick heal**\
\n\n**Syntax : **`.quickh`\
\n**Usage :** prank plugin that acts like antivirus.\
\n\n**Syntax : **`.vquickh`\
\n**Usage :** Prank plugin that scans and shows virus result."
    }
)
