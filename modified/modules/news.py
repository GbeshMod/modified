# Copyright (C) By Gβε₷Ἥ [@GneshMod]
# Don't edit credits
# Works On Bases Of Cyberboysumanjay's Inshorts News Api
# Test
import requests





newslog = Var.NEWS_CHANNEL_ID


@modbot.on(modified_cmd("news (.*)"))
@modbot.on(sudo_cmd("news (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Var.NEWS_CHANNEL_ID is None:
        await edit_or_reply(
            event, "`Please ADD NEWS_CHANNEL_ID For This Module To Work`"
        )
        return
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    stuber = await edit_or_reply(
        event,
        f"Ok ! Fectching {infintyvar} From inshortsapi Server And Sending To News Channel",
    )
    await stuber.edit("All News Has Been Sucessfully Send To News Channel")
    starknews = requests.get(main_url).json()
    for item in starknews["data"]:
        sedlyf = item["content"]
        img = item["imageUrl"]
        writter = item["author"]
        dateis = item["date"]
        readthis = item["readMoreUrl"]
        titles = item["title"]
        sed1 = img
        sedm = f"**Title ➫  {titles}** \n{sedlyf} \nDate ➫  {dateis} \nAuthor ➫  {writter} \nReadMore ➫  {readthis}\n Provided by {newslog}"
        await borg.send_file(sed1, caption=sedm)


CMD_HELP.update(
    {
        "news": "**News**\
\n\n**Syntax : **`.news <type of news>`\
\n**Usage :** Get latest news instantly to your private group"
    }
)
