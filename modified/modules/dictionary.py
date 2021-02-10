
"""Dictionary
Syntax: .ud <word>  
Dictionary Plugin for @UniBorg
Syntax: .meaning <word> or .means"""
import requests
import asyncurban
from PyDictionary import PyDictionary


@bot.on(modified_cmd(pattern="ud (.*)"))
@bot.on(sudo_cmd(pattern="ud (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await edit_or_reply(
            event,
            "ㄒ乇乂ㄒ ᎒᎒ **{}**\n\nᴍᴇᴀɴɪɴɢ ᎒᎒ **{}**\n\nExample: __{}__".format(
                mean.word, mean.definition, mean.example
            ),
        )
    except asyncurban.WordNotFoundError:
        await edit_or_reply(event, "No result found for **" + word + "**")


@bot.on(modified_cmd(pattern="meaning (.*)"))
@bot.on(sudo_cmd(pattern="meaning (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    gbesh = dictionary.meaning(word)
    output = f"**山ㄖ尺刀 ⁛⁛ ** __{word}__\n\n"
    try:
        for a, b in gbesh.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Couldn't fetch meaning of {word}")

@bot.on(modified_cmd(pattern="means (.*)"))
@bot.on(sudo_cmd(pattern="means (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/dictionary/?s={}".format(input_str)
    headers = {"USER-AGENT": "Modified"}
    caption_str = f"Meaning of __{input_str}__\n"
    try:
        response = requests.get(input_url, headers=headers).json()
        pronounciation = response.get("p")
        meaning_dict = response.get("lwo")
        for current_meaning in meaning_dict:
            current_meaning_type = current_meaning.get("type")
            current_meaning_definition = current_meaning.get("definition")
            caption_str += (
                f"**{current_meaning_type}**: {current_meaning_definition}\n\n"
            )
    except Exception as e:
        caption_str = str(e)
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        await borg.send_file(
            event.chat_id,
            pronounciation,
            caption=f"Pronounciation of __{input_str}__",
            force_document=False,
            reply_to=reply_msg_id,
            allow_cache=True,
            voice_note=True,
            silent=True,
            supports_streaming=True,
        )
    except:
        pass


CMD_HELP.update(
{
    "dictionary": "**Dictionary**\
\n\n**Syntax :** `.ud <word>`\
\n**Usage : **fetches meaning from Urban dictionary\
\n\n**Syntax :** `.means <word>`\
\n**Usage : **fetches meaning from and api dictionary\
\n\n**Syntax : **`.meaning <word>`\
\n**Usage : **Fetches meaning of the given word\`"
    }
)