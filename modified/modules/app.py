"""Fetch App Details from Playstore.
.app <app_name> to fetch app details.
Credits @MrConfused
.appr <app_name>  to fetch app details with request link.
  © [cHAuHaN](http://t.me/amnd33p)"""

import bs4
import requests
from modified.functions import apk_dl


@modex.on(modified_cmd(pattern="app (.*)"))
@modex.on(sudo_cmd(pattern="app (.*)", allow_sudo=True))
async def apk(event):
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Searching!")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += f"\n\n===> {BOT_LIN}  <==="
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))


@modex.on(modified_cmd(pattern="appr (.*)"))
@modex.on(sudo_cmd(pattern="appr (.*)", allow_sudo=True))
async def apkr(event):
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "searching!")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += "\n\n<b>Download : </b> <a href='https://t.me/joinchat/JCu-H1NikiYDgNjpjPYd4A'>Request_Here</a>"
        app_details += f"\n\n===> {BOT_LIN}  <==="
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))



@modbot.on(modified_cmd(pattern="appd ?(.*)"))
@modbot.on(sudo_cmd(pattern="appd ?(.*)", allow_sudo=True))
async def _(event):
    app_name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    pathz, name = await apk_dl(app_name, Config.TEMP_DOWNLOAD_DIRECTORY, event)
    await borg.send_file(event.chat_id, pathz, caption='Uploaded By @Modifiedbot ')




CMD_HELP.update(
    {
        "app": ".app [app name]\
\nUsage: searches the app in the playstore and provides the link to the app in playstore and fetchs app details \
\n\n.appr [app name]\
\nUsage: searches the app in the playstore and provides the link to the app in playstore and fetchs app details with Xpl0iter request link. \
\n\n.appd [app name]\
\nUsage: searches the app in the apkpure and download 👇 . 
"
    }
)
