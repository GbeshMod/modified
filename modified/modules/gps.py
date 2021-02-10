"""
Syntax : .gps <location name>
Syntax : .gpx <location name>
"""


from geopy.geocoders import Nominatim
from telethon.tl import types
import requests
import urllib.parse


@modbot.on(modified_cmd(pattern="gps ?(.*)"))
@modbot.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    starkislub = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    address = event.pattern_match.group(1)
    if not address:
        return await starkislub.edit("`Give Input Location.`")
    await starkislub.edit("`Searching..`")
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    try:
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        await reply_to_id.reply(
            address, file=types.InputMediaGeoPoint(types.InputGeoPoint(float(lat), float(lon)))
        )
        await event.delete()
    except:
        await starkislub.edit("Location not found. Please try giving input with country.")


@modbot.on(modified_cmd(pattern="gpx ?(.*)"))
@modbot.on(sudo_cmd(pattern="gpx ?(.*)", allow_sudo=True))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("What should i find? Give me location🙄")

    await event.edit("Finding😁")

    geolocator = Nominatim(user_agent="Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("I coudn't find it😫")


CMD_HELP.update(
    {
        "gps": "**Gps**\
\n\n**Syntax : **`.gps <location>`\
\n**Usage :** this plugin gives gps to the location. or     .gpx"
    }
)
