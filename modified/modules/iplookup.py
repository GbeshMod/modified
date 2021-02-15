import json
import urllib.request
from uniborg.util import admin_cmd
from userbot import CMD_HELP





@borg.on(modified_cmd(pattern="ip (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "a8ebc29386300d2ab541027247a2eb6a"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    a = result["type"]
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    g = result["longitude"]
    await event.edit(
        f"<b><u>📸INFORMATION GATHERED SUCCESSFULLY📸</b></u>\n\n<b>Ip type ➠ </b><code>{a}</code>\n<b>Country code ➠ </b> <code>{b}</code>\n<b>State name ➠ </b><code>{c}</code>\n<b>City name  ➠  </b><code>{d}</code>\n<b>zip  ➠ </b><code>{e}</code>\n<b>Latitude ➠  </b> <code>{f}</code>\n<b>Longitude  ➠  </b><code>{g}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "iplookup": "**IP LOOKUP**\
\n\n**Syntax : **`.ip <ip address>`\
\n**Usage :** Gives details about the ip address."
    }
)
