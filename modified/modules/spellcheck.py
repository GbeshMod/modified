from textblob import TextBlob



@modbot.on(admin_cmd(pattern="spell (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    a = input_str
    b = TextBlob(a)
    c = b.correct()
    await event.edit(
        f"<b><u>Check Completed</b></u> \n\n<b>Original Text</b>:-  <code>{a}</code> \n<b>Corrected Text:-</b> <code>{c}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "spell": "**Spell Checker**\
\n\n**Syntax : **`.spell <text to check>`\
\n**Usage :** Checks for spelling mistakes in given text."
    }
)
