import os.path
import secrets
from random import *

from password_strength import PasswordStats
from userbot import CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd


### ADD ➠➠  password_strength , secrets  to install requirements 👍


sedpath = "./uäαbAid0$/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@borg.on(admin_cmd("savepass ?(.*)"))
@borg.on(sudo_cmd("savepass ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ujwal = input_str.split(":")
    usermail = ujwal[0]
    passwd = ujwal[1]
    webo = ujwal[2]
    if os.path.exists("./uäαbAid0$/info.virus"):
        file = open("./uäαbAid0$/info.virus", "a")
    else:
        file = open("./uäαbAid0$/info.virus", "x")
        file.close()
        file = open("./uäαbAid0$/info.virus", "a")

### Don't be scared /info.virus is just a name


    userName = usermail
    password = passwd
    website = webo

    usrnm = "👥 UserName :  " + userName + "\n"
    pwd = "🔑 Password :  " + password + "\n"
    web = "🌐 Website :  " + website + "\n"

    file.write("⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼⪼\n")
    file.write("\n")
    file.close
    await event.edit(
        f"<b><u>Password Saved Successfully</b></u>",
        parse_mode="HTML",
    )


@borg.on(admin_cmd(pattern=r"passview"))
async def hi(event):
    if event.fwd_from:
        return
    file = open("./uäαbAid0$/info.virus", "r")
    content = file.read()
    file.close()
    await event.edit(
        f"<b><u>Here are your Saved Passwords</u></b>\n<code>{content}</code>",
        parse_mode="HTML",
    )

@borg.on(admin_cmd(pattern="passcheck (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stats = PasswordStats(input_str)
    gbeshmod = stats.strength()
    if stats.strength() >= 0.2:
        await event.edit(
            f"<b><u>Password Checked</b></u> \n<b>🔑 Password :</b> <code>{input_str}</code> \n<b>🛡 Strength :</b> <code>{gbeshmod}</code> \n<b>🗒 Result :</b> <code>Good Password 😎</code>",
            parse_mode="HTML",
        )
    else:
        await event.edit(
            f"<b><u>Password Checked</b></u> \n<b>🗝 Password :</b> <code>{input_str}</code> \n<b>💉 Strength :</b> <code>{gbeshmod}</code> \n<b>📝 Result :</b> <code>Bad Password 😢</code>",
            parse_mode="HTML",
        )


@borg.on(admin_cmd(pattern=r"passgen"))
async def hi(event):
    if event.fwd_from:
        return
    okbabe = secrets.token_urlsafe(16)
    stats = PasswordStats(okbabe)
    gbeshmod = stats.strength()
    await event.edit(
        f"<b>🙈 Password ⪼⪼ </b> <code>{okbabe}</code> \n<b>🙊 Strength ⪼⪼ </b> <code>{gbeshmod}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "password": "**Password Manager**\
\n\n**Syntax : **`.passgen`\
\n**Usage :** This plugin generates good strong password for you.\
\n\n**Syntax : **`.passcheck <your password>`\
\n**Usage :** This plugin checks the strength of your password...\
\n\n**Syntax : **`.savepass email:password:website`\
\n**Usage :** Saves the email, password and website.\
\n\n**Syntax : **`.passview`\
\n**Usage :** View all your saved emails and passwords.\
\n\n**Example : **`.savepass myemail@gmail.com:mypassword:netflix.com`\
\nThis above syntax is saving my Netflix account email and password.\
\n\n**Syntax : **`.passview`\
\n**Usage :** View all your saved emails and passwords."
    }
)
