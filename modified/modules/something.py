""" Whatever Plugin by Noobs of Telegram i.e. """




#@modbot.on(modified_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁🌞      ☁     🦅     ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
            🌲/    | 🚍  \🌳👭
           🌳/  🚘 | 🏃    \🌴 🏇
     👬  🌴/    🤸🏽  |   🚔    \🌲
  🐕    🌲/  🚖     l     ⛹🏽    \
      🌳/🚶        |   🚍      \ 🌴🚴🚴
    🌴/        🏃🏿   |      🚖     \🌲"""
    )





CMD_HELP.update(
    {
        "something": "**Something**\
\n\n**Syntax : **`.lmoon`\
\n**Usage :** creates funny emoji with moons.\
\n\n**Syntax : **`.city`\
\n**Usage :** creates funny city emoji.\
\n\n**Syntax : **`.hello`\
\n**Usage :** creates hello text to wish.\
\n\n**Syntax : **`.cheer`\
\n**Usage :** creates funny emoji.\
\n\n**Syntax : **`.getwell`\
\n**Usage :** creates funny emoji to show getwell.\
\n\n**Syntax : **`.sprinkle`\
\n**Usage :** creates funny text emoji."
    }
)
