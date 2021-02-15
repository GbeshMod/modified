"""WikiMedia.ORG
Syntax: .wikimedia Query

WikiPedia.ORG
Syntax: .wikipedia Query

"""
import requests
import wikipedia




@modbot.on(modified_cmd(pattern="wikimedia (.*)"))
@modbot.on(sudo_cmd(pattern="wikimedia (.*)", allow_sudo=True))
async def _(event):
    wowsosmart = await edit_or_reply(event, "Wait Finding This Bleeding Media xD")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://commons.wikimedia.org/w/api.php?action={}&generator={}&prop=imageinfo&gimlimit={}&redirects=1&titles={}&iiprop={}&format={}".format(
        "query",
        "images",
        "5",
        input_str,
        "timestamp|user|url|mime|thumbmime|mediatype",
        "json",
    )
    r = requests.get(url).json()
    result = ""
    results = r["query"]["pages"]
    for key in results:
        current_value = results[key]
        pageid = current_value["pageid"]
        title = current_value["title"]
        imageinfo = current_value["imageinfo"][0]
        timestamp = imageinfo["timestamp"]
        user = imageinfo["user"]
        descriptionurl = imageinfo["descriptionurl"]
        mime = imageinfo["mime"]
        mediatype = imageinfo["mediatype"]
        result += """\n
        pageid: {}
        title: {}
        timestamp: {}
        user: [{}]({})
        mime: {}
        mediatype: {}
        """.format(
            pageid, title, timestamp, user, descriptionurl, mime, mediatype
        )
    await wowsosmart.edit(
        "**Search** ➻  {} \n\n **Results** ➻  {}".format(input_str, result)
    )


@modbot.on(modified_cmd(pattern="wikipedia (.*)"))
@modbot.on(sudo_cmd(pattern="wikipedia (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit(
        "WikiPedia **Search** ➻  {} \n\n **Result** ➻  \n\n{}".format(input_str, result)
    )


CMD_HELP.update(
    {
        "wiki": "**Wiki media**\
\n\n**Syntax : **`.wikimedia <query>`\
\n**Usage :** Searches for media from wikipedia with your query.\
\n\n**Syntax : **`.wikipedia <query>`\
\n**Usage :** get Wikipedia link instantly just with a query"
    }
)
