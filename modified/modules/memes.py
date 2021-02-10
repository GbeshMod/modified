import re
import os
import random
import asyncio
import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont
from modified.function import convert_to_image
from telethon import functions, types
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, MessageEntityMentionName
from modified import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, modmemes


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Modified"


async def get_user(event):
    # Get the user from argument or replied message.
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None
    return replied_user



sedpath = Config.TMP_DOWNLOAD_DIRECTORY


@modbot.on(modified_cmd(pattern="memify (.*)"))
async def starkmeme(event):
    hmm = event.pattern_match.group(1)
    if hmm == None:
        await event.edit("Give Some Text")
        return
    if not event.reply_to_msg_id:
        await event.edit("`PLease, Reply To A MsG`")
        return
    mryeast = await event.edit("Making Memes Until Praise MrBeast.")
    await event.get_reply_message()
    seds = await convert_to_image(event, borg)
    if ";" in hmm:
        stark = hmm.split(";", 1)
        first_txt = stark[0]
        second_txt = stark[1]
        top_text = first_txt
        bottom_text = second_txt
        generate_meme(seds, top_text=top_text, bottom_text=bottom_text)
        imgpath = sedpath + "/" + "memeimg.png"
        await borg.send_file(event.chat_id, imgpath)
        if os.path.exists(imgpath):
            os.remove(imgpath)
        await mryeast.delete()
    else:
        top_text = hmm
        bottom_text = ""
        generate_meme(seds, top_text=top_text, bottom_text=bottom_text)
        imgpath = sedpath + "/" + "memeimg.png"
        await borg.send_file(event.chat_id, imgpath)
        if os.path.exists(imgpath):
            os.remove(imgpath)
        await mryeast.delete()


def generate_meme(
    image_path, top_text, bottom_text="", font_path="Fonts/impact.ttf", font_size=11
):
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size
    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    char_width, char_height = font.getsize("A")
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = 9
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y + 2), line, font=font, fill="black")
        draw.text((x - 2, y + 2), line, font=font, fill="black")
        draw.text((x, y), line, fill="white", font=font)
        y += line_height

    y = image_height - char_height * len(bottom_lines) - 14
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y + 2), line, font=font, fill="black")
        draw.text((x - 2, y + 2), line, font=font, fill="black")
        draw.text((x, y), line, fill="white", font=font)
        y += line_height
    file_name = "memeimg.png"
    ok = sedpath + "/" + file_name
    im.save(ok, "PNG")




@bot.on(admin_cmd(pattern=r"slap(?: |$) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="slap(?: |$) (.*)", allow_sudo=True))
async def who(event):
    replied_user = await get_user(event)
    caption = await modmemes.slap(replied_user, event, DEFAULTUSER)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await edit_or_reply(event, caption)
    except BaseException:
        await edit_or_reply(
            event, "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


@bot.on(admin_cmd(outgoing=True, pattern="(yes|no|maybe|decide)$"))
@bot.on(sudo_cmd(pattern="(yes|no|maybe|decide)$", allow_sudo=True))
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id or None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    sandy = await event.client.send_message(
        event.chat_id, str(r["answer"]).upper(), reply_to=message_id, file=r["image"]
    )
    await event.client(
        functions.messages.SaveGifRequest(
            id=types.InputDocument(
                id=sandy.media.document.id,
                access_hash=sandy.media.document.access_hash,
                file_reference=sandy.media.document.file_reference,
            ),
            unsave=True,
        )
    )


@bot.on(admin_cmd(pattern=f"shout", outgoing=True))
@bot.on(sudo_cmd(pattern=f"shout", allow_sudo=True))
async def shout(args):
    msg = "```"
    messagestr = args.text
    messagestr = messagestr[7:]
    text = " ".join(messagestr)
    result = [" ".join([s for s in text])]
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "\n" + result
    await edit_or_reply(args, "`" + msg + "`")


@bot.on(admin_cmd(pattern="owo ?(.*)"))
@bot.on(sudo_cmd(pattern="owo ?(.*)", allow_sudo=True))
async def faces(owo):
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(owo, "` UwU no text given! `")
        return
    reply_text = re.sub(r"(r|l)", "w", message)
    reply_text = re.sub(r"(R|L)", "W", reply_text)
    reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = re.sub(r"\!+", " " + random.choice(modmemes.UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + random.choice(modmemes.UWUS)
    await edit_or_reply(owo, reply_text)


@bot.on(admin_cmd(pattern="clap(?: |$) (.*)"))
@bot.on(sudo_cmd(pattern="clap(?: |$) (.*)", allow_sudo=True))
async def claptext(event):
    textx = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif textx.message:
        query = textx.message
    else:
        await edit_or_reply(event, "Hah, I don't clap pointlessly!")
        return
    reply_text = "👏 "
    reply_text += query.replace(" ", " 👏 ")
    reply_text += " 👏"
    await edit_or_reply(event, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="smk(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="smk(?: |$)(.*)", allow_sudo=True))
async def smrk(smk):
    textx = await smk.get_reply_message()
    if smk.pattern_match.group(1):
        message = smk.pattern_match.group(1)
    elif textx.message:
        message = textx.message
    else:
        await edit_or_reply(smk, "ツ")
        return
    if message == "dele":
        await edit_or_reply(smk, message + "te the hell" + "ツ")
    else:
        smirk = " ツ"
        reply_text = message + smirk
        await edit_or_reply(smk, reply_text)


@bot.on(admin_cmd(pattern="ftext (.*)"))
@bot.on(sudo_cmd(pattern="ftext (.*)", allow_sudo=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await edit_or_reply(event, pay)


@bot.on(admin_cmd(pattern="wish ?(.*)"))
@bot.on(sudo_cmd(pattern="wish ?(.*)", allow_sudo=True))
async def wish_check(event):
    wishtxt = event.pattern_match.group(1)
    chance = random.randint(0, 100)
    if wishtxt:
        reslt = f"**Your wish **__{wishtxt}__ **has been cast.** ✨\
              \n\n__Chance of success :__ **{chance}%**"
    else:
        if event.is_reply:
            reslt = f"**Your wish has been cast. **✨\
                  \n\n__Chance of success :__ **{chance}%**"
        else:
            reslt = f"What's your Wish? Should I consider you as Idiot by default ? 😜"
    await edit_or_reply(event, reslt)



@bot.on(admin_cmd(pattern="lfy ?(.*)"))
@bot.on(sudo_cmd(pattern="lfy ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "`either reply to text message or give input to search`", 5
        )
    sample_url = f"https://da.gd/s?url=https://lmgtfy.com/?q={input_str.replace(' ', '+')}%26iie=1"
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, f"[{input_str}]({response_api.rstrip()})\n`Thank me Later 🙃` "
        )
    else:
        return await edit_delete(
            event, "`something is wrong. please try again later.`", 5
        )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"LMGTFY query `{input_str}` was executed successfully",
        )


CMD_HELP.update(
    {
        "memes": "**Memes**\
        \n\n  •  **Syntax :** `.slap`\
        \n  •  **Function : **reply to slap them with random objects !!\
        \n\n  •  **Syntax :** `.yes` ,`.no` , `.maybe` , `.decide`\
        \n  •  **Function : **Sends you the respectively gif of command u used\
        \n\n  •  **Syntax :** `.shout text`\
        \n  •  **Function : **shouts the text in a fun way\
        \n\n  •  **Syntax :** `.owo`\
        \n  •  **Function : **UwU\
        \n\n  •  **Syntax :** `.clap`\
        \n  •  **Function : **Praise people!\
        \n\n  •  **Syntax :** `.smk <text/reply>`\
        \n  •  **Function : **A shit module for ツ , who cares.\
        \n\n  •  **Syntax :** `.ftext <emoji/character>`\
        \n  •  **Function : **Pay Respects.\
        \n\n  •  **Syntax :** `.wish <reply/text>`\
        \n  •  **Function : **Shows the chance of your success inspired from @CalsiBot.\
        \n\n  •  **Syntax :** `.lfy <query>`\
        \n  •  **Function : **Let me Google that for you real quick !!\
"
    }
)
