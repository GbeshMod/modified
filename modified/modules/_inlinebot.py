# from modified import @GbeshMod as ©copyright
import os
import re
import urllib
import requests
from math import ceil
from re import findall
from urllib.parse import quote
from pornhub_api import PornhubApi
from modified.function import _ytdl
from modified.modules import inlinestats
from youtube_search import YoutubeSearch
from search_engine_parser import GoogleSearch
from youtubesearchpython import VideosSearch

from modified.function import _ytdl, fetch_json, _deezer_dl, all_pro_s
from modified import ALIVE_NAME, CMD_HELP, CMD_LIST, BOT_N_N, BOT_LIN, client2 as client1, client3 as client2, bot as client3
from telethon import Button, custom, events, functions
from telethon.tl.types import BotInlineResult, InputBotInlineMessageMediaAuto, DocumentAttributeImageSize, InputWebDocument, InputBotInlineResult
from telethon.tl.functions.messages import SetInlineBotResultsRequest






PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/66b907a1ccd4ca09f6177.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Modified"

@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    B = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id in B and query.startswith("Modified"):
        rev_text = query[::-1]
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = builder.article(
            "© ᖇOᗷOT Help",
            text="{}\nCurrently Loaded Plugins ➻ {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query == "stats":
        result = builder.article(
            title="Stats",
            text= f"**⎉ Showing Stats For {DEFAULTUSER}'s Robot ⎉** \nNote --> Only Owner Can Check This \n©͙{BOT_LIN} ",
            buttons=[
                [custom.Button.inline("sʜᴏᴡ sᴛᴀᴛs ?", data="terminator")],
                [Button.url("♨sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/GbeshMod/modified")],
                [Button.url("☬мy creaтor☬", "t.me/GbeshMod")],
            ],
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query.startswith("**Hello"):
        result = builder.photo(
            file=WARN_PIC,
            text=query,
            buttons=[
                [custom.Button.inline("Spamming", data="dontspamnigga")],
                [
                    custom.Button.inline(
                        "Casual Talk",
                        data="whattalk",
                    )
                ],
                [custom.Button.inline("Requesting", data="askme")],
            ],
        )
        await event.answer([result])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backxm")))
async def sed(event):
    sedm = int(event.data_match.group(1).decode("UTF-8"))
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        oops = "ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 千ㄩ匚Ҝ 卂尺乇 ㄚㄖㄩ..."
        await event.answer(oops, cache_time=0, alert=True)
        return
    await event.answer("Back", cache_time=0, alert=False)
    gith = paginate_help(0, CMD_HELP, "helpme")
    sed = f"""Modified ᖇOᗷOT Modules Are Listed Here !\nCurrently Loaded Plugins ➻ {len(CMD_LIST)}"""
    await event.edit(message=sed, buttons=gith)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"openx")))
async def opner(event):
  B = await all_pro_s(Config, client1, client2, client3)
  if event.query.user_id in B :
    current_page_number=0
    modxt = paginate_help(current_page_number, CMD_LIST, "helpme")
    txmm = f"📝{BOT_N_N} ʜᴇʟᴘᴇʀ ᴛᴏ ʀᴇᴠᴇᴀʟ ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs📝\n\n🔑 You opened THE MAIN MENU  🔓"
    await event.edit(txmm, buttons=modxt)
    else:
      oops = "ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 ғᴜᴄᴋ ᴀʀᴇ ʏᴏᴜ. ρℓ૯αઽ૯ Բષ૮ઝ ѳԲԲ"
    await event.answer(oops, cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"closex")))
async def on_plug_in_callback_query_handler(event):
  B = await all_pro_s(Config, client1, client2, client3)
  if event.query.user_id in B:
    moddd = custom.Button.inline("⚛ ᴏᴘᴇɴ 🔓🔑 ᴀɢᴀɪɴ ⚛", data="openx")
    txt = f"🔐 CLOSED {BOT_N_N} ᴍᴀɪɴ ᴍᴇɴᴜ 🔐"
    await event.edit(txt, buttons=moddd)
    else:
      reply_popp = "Who the Բષ૮ઝ is This... CAN'T YOU SEE IT CLOSED 🔐 "
      await event.answer(reply_popp, cache_time=0, alert=True)


# "❃.👉🏽✮:▹"
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"helpme_next\((.+?)\)")))
async def on_plug_in_callback_query_handler(event):
  B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_popp_up_alert = "ԹӀҽɑՏҽ ցҽԵ վօմɾ օաղ ʍօժíƒíҽժ ҍօԵ, ɑղժ ժօղ'Ե մՏҽ ʍíղҽ!"
        await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

# "◃:✮👈🏽.❃"
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"helpme_prev\((.+?)\)")))
async def on_plug_in_callback_query_handler(event):
  B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
        )
        await event.edit(buttons=buttons)
    else:
        oops = "℘ɭεศรε ɢεt ყσนг σшŋ ɱσɖıʄıεɖ ๖σt, ศŋɖ ɖσŋ't นรε ɱıŋε!"
        await event.answer(oops, cache_time=0, alert=True)

# 🐍🐍🐍
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"us_plugin_(.*)")))
async def on_plug_in_callback_query_handler(event):
      B = await all_pro_s(Config, client1, client2, client3)
    if not event.query.user_id in B:
        oops = "ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 千ㄩ匚Ҝ 卂尺乇 ㄚㄖㄩ.."
        await event.answer(oops, cache_time=0, alert=True)
        return
    plugin_name, page_number = event.data_match.group(1).decode("UTF-8").split("|", 1)
    if plugin_name in CMD_HELP:
      help_string = f"**🎖️P͙L͙U͙G͙I͙N͙ ͙N͙A͙M͙E͙🎖️ ➫ ** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
    oops = help_string
    oops += "\n Use .unload {} to disable this plugin\n\n\n**©͙{} ** ".format(plugin_name, BOT_LIN)
        if len(oops) >= 4096:
        crackexy = "`Pasting Your Help Menu.`"
        await event.answer(crackexy, cache_time=0, alert=True)
        out_file = oops
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        await event.edit(
            f"Pasted {plugin_name} to {url}",
            link_preview=False,
            buttons=[[custom.Button.inline("⚜️ ʙᴀᴄᴋ ᴛᴏ ᴍᴇɴᴜ ⚜️", data="backxm")]],
        )
    else:
        await event.edit(
            message=oops,
            buttons=[[custom.Button.inline("⚜️ ʙᴀᴄᴋ ᴛᴏ ᴍᴇɴᴜ ⚜️", data="backxm")]],
        )


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    emojj = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [custom.Button.inline(
        "{} {} {}".format(random.choice(list(emojj)), xx, random.choice(list(emojj))),
        data="us_plugin_{}|{}".format(xx, page_number))
        for xx in helpable_modules]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("◃:✮👈🏽.❃", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⋇⋆⚚🔐⚚⋆⋇", data="closex"),
             custom.Button.inline("❃.👉🏽✮:▹", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
async def rip(event):
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        text = inlinestats
        await event.answer(text, alert=True)
    else:
        txt = "Sorry 🙏  You Can't View My Masters Stats.. ઽѳ Բષ૮ઝ ѳԲԲ"
        await event.answer(txt, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
async def rip(event):
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        oops = "Master, You Don't Need To Use This."
        await event.answer(oops, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    text1 = "**You Have Chosed A Probhited Option. Therefore, You Have Been Blocked By ᖇOᗷOT.**"
    await event.edit("Choice Not Accepted ❌")
    await event.edit(text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    PM_E = f"**卩爪乇ᐯ乇几ㄒ** \nUser ID ➻ {him_id} \n**This User Choose Probhited Option, So Has Been Blocked !** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(
        LOG_CHAT,
        message=PM_E)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
async def rip(event):
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        oops = "Master, You Don't Need To Use This."
        await event.answer(oops, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✔️")
    await event.edit("Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything f͜͡u͜͡n͜͡n͜͡y͜͡. \nThank You For Contacting Me.")
    PM_E = f"**卩爪乇ᐯ乇几ㄒ** \nUser ID ➻ {him_id} \n**This User Wanted To Talk To You.** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
async def rip(event):
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in B:
        oops = "Master, You Don't Need To Use This."
        await event.answer(oops, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✔️")
    await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
    PM_E = f"**卩爪乇ᐯ乇几ㄒ** \nUser ID ➻ {him_id} \n**This User Wanted To Ask You Something** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_dla_(.*)")))
async def rip(event):
    B = await all_pro_s(Config, client1, client2, bot)
    yt_dl_data = event.data_match.group(1).decode("UTF-8")
    link_s = yt_dl_data
    if event.query.user_id not in B:
        text = f"ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 千ㄩ匚Ҝ 卂尺乇 ㄚㄖㄩ.."
        await event.answer(text, alert=True)
        return
    is_it = True
    ok = await _ytdl(link_s, is_it, event, tgbot)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deezer_dl_(.*)")))
async def rip(event):
  sun = event.data_match.group(1).decode("UTF-8")
  B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        text = f"ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 千ㄩ匚Ҝ 卂尺乇 ㄚㄖㄩ.."
        await event.answer(text, alert=True)
        return
    ok = await _deezer_dl(sun, event, tgbot)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_vid_(.*)")))
async def rip(event):
  yt_dl_data = event.data_match.group(1).decode("UTF-8")
  B = await all_pro_s(Config, client1, client2, client3)
    link_s = yt_dl_data
    if event.query.user_id not in B:
        text = f"ᴀᴍ sᴏʀʀʏ😕 ᴛᴏ ᴀsᴋ... ʙᴜᴛ ᴡʜᴏ ᴛʜᴇ 😠 千ㄩ匚Ҝ 卂尺乇 ㄚㄖㄩ.."
        await event.answer(text, alert=True)
        return
    is_it = False
    ok = await _ytdl(link_s, is_it, event, tgbot)


@tgbot.on(events.InlineQuery(pattern=r"torrent (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        resultm = builder.article(
            title="Not Allowded",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    testinput = event.pattern_match.group(1)
    peaceisnub = urllib.parse.quote_plus(testinput)
    results = []
    sedlyf = "https://api.sumanjay.cf/torrent/?query=" + peaceisnub
    try:
        okpro = requests.get(url=sedlyf, timeout=10).json()
    except:
        pass
    sed = len(okpro)
    if sed == 0:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [
                    Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    )
                ],
            ],
        )
        await event.answer([resultm])
        return
    if sed > 30:
        for i in range(30):
            seds = okpro[i]["age"]
            okpros = okpro[i]["leecher"]
            sadpeace = okpro[i]["magnet"]
            okiknow = okpro[i]["name"]
            peacesize = okpro[i]["size"]
            peacey = okpro[i]["type"]
            seeders = okpro[i]["seeder"]
            okayz = f"**Title ➻ ** `{okiknow}` \n**Size ➻ ** `{peacesize}` \n**Type ➻ ** `{peacey}` \n**Seeder ➻ ** `{seeders}` \n**Leecher ➻ ** `{okpros}` \n**Magnet ➻ ** `{sadpeace}` "
            sedme = f"Size ➻ {peacesize} Type ➻ {peacey} Age ➻ {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    ),
                )
            )
    else:
        for sedz in okpro:
            seds = sedz["age"]
            okpros = sedz["leecher"]
            sadpeace = sedz["magnet"]
            okiknow = sedz["name"]
            peacesize = sedz["size"]
            peacey = sedz["type"]
            seeders = sedz["seeder"]
            okayz = f"**Title ➻** `{okiknow}` \n**Size ➻** `{peacesize}` \n**Type ➻** `{peacey}` \n**Seeder ➻** `{seeders}` \n**Leecher ➻** `{okpros}` \n**Magnet ➻** `{sadpeace}` "
            sedme = f"Size ➻ {peacesize} Type ➻ {peacey} Age ➻ {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="torrent ", same_peer=True
                        )
                    ],
                )
            )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    B = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    if event.query.user_id not in B:
        resultm = builder.article(
            title="Not Allowded",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    testinput = event.pattern_match.group(1)
    urllib.parse.quote_plus(testinput)
    results = []
    moi = YoutubeSearch(testinput, max_results=9).to_dict()
    if not moi:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
            ],
        )
        await event.answer([resultm])
        return
    for moon in moi:
        hmm = moon["id"]
        mo = f"https://www.youtube.com/watch?v={hmm}"
        kek = f"https://www.youtube.com/watch?v={hmm}"
        peace_name = moon["title"]
        peace_chnnl = moon["channel"]
        total_peace = moon["duration"]
        peace_views = moon["views"]
        lol_desc = moon["long_desc"]
        kekme = f"https://img.youtube.com/vi/{hmm}/hqdefault.jpg"
        okayz = f"**Title ➻** `{peace_name}` \n**Link ➻** `{kek}` \n**Channel ➻** `{peace_chnnl}` \n**Views ➻** `{peace_views}` \n**Duration ➻** `{total_peace}`"
        hmmkek = f"Video Name ➻ {peace_name} \nChannel ➻ {peace_chnnl} \nDuration ➻ {total_peace} \nViews ➻ {peace_views}"
        results.append(
            await event.builder.document(
                file=kekme,
                title=peace_name,
                description=hmmkek,
                text=okayz,
                include_media=True,
                buttons=[
                [custom.Button.inline("Download Video - mp4", data=f"yt_vid_{mo}")],
                [custom.Button.inline("Download Audio - mp3", data=f"yt_dla_{mo}")],
                [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ]
              )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"jm (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    B = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    if event.query.user_id not in B:
        resultm = builder.article(
            title="Not Allowded",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    testinput = event.pattern_match.group(1)
    peaceisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = f"http://peacemusic.herokuapp.com/result/?query={peaceisnub}"
    seds = requests.get(url=search).json()
    for okz in seds:
        okz["album"]
        okmusic = okz["music"]
        hmmstar = okz["perma_url"]
        singer = okz["singers"]
        hmm = okz["duration"]
        langs = okz["language"]
        hidden_url = okz["media_url"]
        okayz = (
            f"**Song Name ➻** `{okmusic}` \n**Singer ➻** `{singer}` \n**Song Url ➻** `{hmmstar}`"
            f"\n**Language ➻** `{langs}` \n**Download Able Url ➻** `{hidden_url}`"
            f"\n**Duration ➻** `{hmm}`"
        )
        hmmkek = (
            f"Song ➻ {okmusic} Singer ➻ {singer} Duration ➻ {hmm} \nLanguage ➻ {langs}"
        )
        results.append(
            await event.builder.article(
                title=okmusic,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline(
                    "Search Again", query="jm ", same_peer=True
                ),
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"google (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    results = []
    match = event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            okiknow = f"**GOOGLE - SEARCH** \n[{title}]({link})\n\n`{desc}`"
            results.append(
                await event.builder.article(
                    title=title,
                    description=desc,
                    text=okiknow,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="google ", same_peer=True
                        )
                    ],
                )
            )
        except IndexError:
            break
    await event.answer(results)

@tgbot.on(events.InlineQuery(pattern=r"ph (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(
    input_str,
    ordering="mostviewed"
    )
    ok = 1
    oik = ""
    for vid in data.videos:
      if ok <= 5:
        lul_m = (f"**PORN-HUB SEARCH** \n**Video title ➻** `{vid.title}` \n**Video link ➻** `https://www.pornhub.com/view_video.php?viewkey={vid.video_id}`")
        results.append(
                await event.builder.article(
                    title=vid.title,
                    text=lul_m,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="ph ", same_peer=True
                        )
                    ],
                )
            )
      else:
        pass
    await event.answer(results)

@tgbot.on(events.InlineQuery(pattern=r"xkcd (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(input_str)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """
[XKCD]({})
Title ➻ {}
Alt ➻ {}
Day ➻ {}
Month ➻ {}
Year ➻ {}""".format(
            xkcd_link, safe_title, alt, day, month, year
        )
        lul_k = builder.photo(
            file=img,
            text=output_str
        )
        await event.answer([lul_k])
    else:
        resultm = builder.article(
            title="- No Results :/ -",
            text=f"No Results Found !"
        )
        await event.answer([resultm])

@tgbot.on(events.InlineQuery(pattern=r"deezer ?(.*)"))
async def inline_id_handler(event):
  builder = event.builder
  B = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in B:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy Modified To Get Your Own Assistant, Repo Link [Here 🚪](https://github.com/GbeshMod /modified)",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    link = f"https://api.deezer.com/search?q={input_str}&limit=7"
    dato = requests.get(url=link).json()
    #data_s = json.loads(data_s)
    for match in dato.get("data"):
            ro = str(match.get("id"))
            hmm_m = (f"Title ➻ {match['title']} \nLink ➻ {match['link']} \nDuration ➻ {match['duration']} seconds \nBy ➻ {match['artist']['name']}")
            results.append(
                await event.builder.document(
                    file=match["album"]["cover_big"],
                    title=match["title"],
                    text=hmm_m,
                    description=f"Artist ➻ {match['artist']['name']}\nAlbum ➻ {match['album']['title']}",
                    buttons=[
                       [custom.Button.inline("Download Audio - mp3", data=f"deezer_dl_{ro}")],
                    ]
                ),
            )
    if results:
        try:
            await event.answer(results)
        except TypeError:
            pass
