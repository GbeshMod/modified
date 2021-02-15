import pyfiglet




@modbot.on(modified_cmd(pattern="figlet ?(.*)", outgoing=True))
@modbot.on(sudo_cmd(pattern="figlet ?(.*)", allow_sudo=True))
async def figlet(event):
    arjun = await edit_or_reply(event, "`Figleting This Text xD`")
    if event.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
    }
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await arjun.edit("Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await arjun.edit("Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await arjun.edit("‌‌‎`{}`".format(result))


CMD_HELP.update(
    {
        "figlet": "**Figlet**\
\n\n**Syntax : **``.figlet <text>.<style>`\
\nUsage: convets text into ASCII art.\
\n\nExample: `.figlet Gbesh.3D`\
\n\nStyle: `slant`, `3D`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi` "
    }
)
