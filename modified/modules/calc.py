# credits to @GbeshMod 
import sys
import json
import io, os
import asyncio
import requests
import calendar
import traceback
from telethon import events
from datetime import datetime



@bot.on(admin_cmd(pattern="calc (.*)"))
@bot.on(sudo_cmd(pattern="calc (.*)", allow_sudo=True))
async def _(car):
    cmd = car.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(car, "Calculating ...")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sorry I can't find result for the given equation"
    final_output = "**EQUATION**: `{}` \n\n **SOLUTION**: \n`{}` \n".format(
        cmd, evaluation
    )
    await event.edit(final_output)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)


@bot.on(admin_cmd(pattern="cal (.*)"))
@bot.on(sudo_cmd(pattern="cal (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(".")
    if len(input_sgra) == 3:
        yyyy = input_sgra[0]
        mm = input_sgra[1]
        dd = input_sgra[2]
        required_url = "https://calendar.kollavarsham.org/api/years/{}/months/{}/days/{}?lang={}".format(yyyy, mm, dd, "en")
        headers = {"Accept": "application/json"}
        response_content = requests.get(required_url, headers=headers).json()
        a = ""
        if "error" not in response_content:
            current_date_detail_arraays = response_content["months"][0]["days"][0]
            a = json.dumps(current_date_detail_arraays, sort_keys=True, indent=4)
        else:
            a = response_content["error"]
        await event.edit(str(a))
    else:
        await event.edit("SYNTAX: .calendar YYYY.MM.DD")
    end = datetime.now()
    ms = (end - start).seconds



CMD_HELP.update(
    {
        "calc": "**Calculator**\
        \n\n**Syntax : **`.calc expression` \
        \n**Function : **solves the given maths equation by BODMAS rule. \
        \n\n**Syntax : **`.cal year ; month`\
        \n**Function : **__Shows you the calendar of given month and year__\"
    }
)
