

@modbot.on(modified_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")


CMD_HELP.update(
    {
        "hyperlink": "**Hyperlink**\
\n\n**Syntax : **`.hl <link>`\
\n**Usage :** Creates a hyperlink with given link."
    }
)
