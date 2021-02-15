""" Google Translate and voice  .ttv
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import requests
from datetime import datetime
from langdetect import detect
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator
from google_trans_new import google_translator



@modbot.on(modified_cmd("tr ?(.*)"))
@modbot.on(sudo_cmd("tr ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(event, "`.tr LanguageCode` as reply to a message")
        return

    lan = lan.strip()
    try:
        translator = google_translator()
        translated = translator.translate(text ,lang_tgt=lan)
        lmao_bruh = text
        lmao = detect(text)
        after_tr_text = lmao
        source_lan = LANGUAGES[after_tr_text]
        transl_lan = LANGUAGES[lan]
        output_str = f"""**ᴛʀᴀɴsʟᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**
**Source ({source_lan})**:
`{text}`

**Translation ({transl_lan})**:
`{translated}`"""
      
        if len(output_str) >= 4096:
            out_file = output_str
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url2 = f"https://del.dog/{r['key']}"
            starky = f"Translated Text Was Too Big, Never Mind I Have Pasted It [Here]({url2})"
        else:
            starky = output_str
        await edit_or_reply(event, starky)
    except Exception as e:
      print(e)



import os
import asyncio
import subprocess
from gtts import gTTS


@modbot.on(modified_cmd("ttv ?(.*)"))
@modbot.on(sudo_cmd("ttv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("Invalid Syntax. Module stopping.")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "voice.ogg"
    try:
        # https://github.com/SpEcHiDe/UniBorg/commit/17f8682d5d2df7f3921f50271b5b6722c80f4106
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            required_file_name + ".opus",
        ]
        try:
            t_response = subprocess.check_output(
                command_to_execute, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await event.edit(str(exc))
            # continue sending required_file_name
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await borg.send_file(
            event.chat_id,
            required_file_name,
            # caption="Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms),
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True,
        )
        os.remove(required_file_name)
        await event.edit("Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms))
        await asyncio.sleep(5)
        await event.delete()
    except Exception as e:
        await event.edit(str(e))



CMD_HELP.update(
    {
        "translate": "**Translate**\
\n\n**Syntax : **`.tr <language Code> <reply to text>`\
\n**Usage :** Translates the given text into your language.\
.ttv Google Text to Speech\
\nAvailable Commands:\
\n.ttv LanguageCode as reply to a message\
\n\n.ttv LangaugeCode | text to speak\"
    }
)
