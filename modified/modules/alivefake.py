"""Preview alive as friday, cat, hell etc."""
import time
from telethon import __version__ as tv
import sys
import platform
from git import repo
from datetime import datetime
from telethon import events, __version__, version
from platform import python_version, uname
from telethon.tl.types import ChannelParticipantsAdmins
from modified import ALIVE_NAME, CMD_HELP, Lastupdate


global ghanti
ghanti = borg.uid
mention = f"[{DEFAULTUSER}](tg://user?id={ghanti})"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else BOT_N_N
def check_data_b():
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from modified.modules.sql_helper import SESSION
    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
uptime = get_readable_time((time.time() - Lastupdate))

    repo = Repo()
    branch_name = repo.active_branch.name





@bot.on(admin_cmd(pattern="alivef$"))
async def friday(alivef):
    await alivef.get_chat()
    FD_IMG = "https://telegra.ph/file/22535f8051a58af113586.jpg"
    f_msg = ("➥ **FRIDAY IS:** `ONLINE`\n\n"
                  "➥ **SYSTEMS STATS**\n"
                  f"➥ **Telethon Version:** `{tv}` \n"
                  f"➥ **Python:** `{platform.python_version()}` \n"
                  f"➥ **Uptime** : `{uptime}` \n"
                  "➥ **Database Status:**  `Functional`\n"
                  f"➥ **Current Branch** : `{branch_name}`\n"
                  f"➥ **Version** : `6.5`\n"
                  f"➥ **My Boss** : {DEFAULTUSER} \n"
                  "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
                  "➥ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
                  "➥ **Copyright** : By [StarkGang@Github](GitHub.com/StarkGang)\n"
                  "➥ **Check Stats By Doing** `.stat`. \n\n"
                  "[🏁 Deploy FridayUserbot 🏁](https://telegra.ph/FRIDAY-06-15)")

    await borg.send_file(alivef.chat_id, FD_IMG, caption=f_msg)
    await alivef.delete()


@bot.on(admin_cmd(pattern="alivej$"))
async def jv_alive(alivej):
        jv_logs = "Enabled"
        dbstats = "All Fine 😉👍🏻"
        PM_IMG = "https://telegra.ph/file/d61452c69b961e794eedd.jpg"
        jv_msg = "**Master JARVIS AT YOU SERVICE 🤗 **\n"
        jv_msg += f"**••Mу Bσѕѕ••**           {DEFAULTUSER}\n"
        jv_msg += " **✓ JARVIS STATS ✓** \n"
        jv_msg += "  🔸 ➣**Pутнση Vєяѕιση**    `3.8.5`\n"
        jv_msg += f"  🔸 ➣**Bσт Vєяѕιση**        `1.6` \n"
        jv_msg += f"  🔸 ➣**Dαтαвαѕє**    `{dbstats}` \n"
        jv_msg += f"  🔸 ➣**Sυ∂σ**               `{BOT_LIN}` \n"
        jv_msg += f"  🔸 ➣**Pм Lσgѕ**        `{jv_logs}` \n"
        jv_msg += f"  🔸 ➣**Hєяσкυ**          `{jv_logs}` \n"
        jv_msg += f"  🔸 ➣**UρTιмє**           `{uptime}`\n\n"
        jv_msg += "[☆ Git Repo ☆](https://jarvisworks.ga/userjbot)"

    await borg.send_file(alivej.chat_id, jv_pic, caption=jv_msg)
    await alivej.delete()


@bot.on(admin_cmd(pattern="alivec$"))
async def cat_alive(alivec):
    catversion = "2.10.1"
    cat_atxt = Config.CUSTOM_ALIVE_TEXT
    cat_pic = "https://telegra.ph/file/3d60313110c58684b31ea.jpg"
    EMOJI = Config.CUSTOM_ALIVE_EMOJI or "✥"
    cat_msg = f"**{cat_atxt}**\n\n"
    cat_msg += f"**   {EMOJI}  Database :** `{check_data_b}`\n"
    cat_msg += f"**   {EMOJI}  Telethon version :** `{version.__version__}\n`"
    cat_msg += f"**   {EMOJI}  Catuserbot Version :** `{catversion}`\n"
    cat_msg += f"**   {EMOJI}  Python Version :** `{python_version()}\n`"
    cat_msg += f"**   {EMOJI}  Uptime :** `{uptime}\n`"
    cat_msg += f"**   {EMOJI}  Master:** {mention}\n"
    await borg.send_file(alivec.chat_id, cat_pic, caption=cat_msg)
    await alivec.delete()


@bot.on(admin_cmd(pattern="alivewv$"))
async def wvn_alive(alivewv):
    wvn_v = "2.10.1"
    wvn_pic = "https://telegra.ph/file/vdhdjhdhfhhfh.jpg"
     wvn_msg = (
        "**MADE IN 🏁,MADE WITH😻**\n"
        f"**•••••••••••••••••••••••••••••••**\n"
        f"🔹 `Fork By`      :  **{DEFAULTUSER}**\n"
        f"🔸 `Python`       : **v{python_version()}**\n"
        f"🔹`Telethon`      : **v{version.__version__}**\n"
        f"🔸 `WolveRine`    : **v{wvn_v}**\n"
        f"🔹`Bot Plugins`   : **{len(modules)}**\n"
        f"🔸 `Wolve UpTime` : **{uptime} **\n"
        f"🔹**Join @WolveRineChat For Help**\n"
        f"🔸`WolveRineRepo` :**[Deploy✔️](https://github.com/ShadoWClub/WolverineUserbot)**\n"
    )

    await borg.send_file(alivewv.chat_id, wvn_pic, caption=wvn_msg)
    await alivewv.delete()


@bot.on(admin_cmd(pattern="aliveh$"))
async def hell_alive(aliveh):
    hell_pic = "https://telegra.ph/file/80e5200c615cf0cb57aa9.mp4"
    hell_msg = "__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"
    hell_msg += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『{mention}』**\n\n"
    )
    hell_msg += "🛡️TELETHON🛡️ : `1.15.0` \n"
    hell_msg += f"😈Hêllẞø†😈       : __**v2.1**__\n"
    hell_msg += f"⚜️Sudo⚜️            : `{BOT_LIN}`\n"
    hell_msg += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"
    hell_msg += "🔥CREATOR🔥    : [Nub Here](https://t.me/kraken_the_badass)\n\n"
    hell_msg += "    [✨REPO✨](https://github.com/hellboy-op/hellbot) 🔹 [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"

    await borg.send_file(aliveh.chat_id, hell_pic, caption=hell_msg)
    await aliveh.delete()


@borg.on(admin_cmd(pattern=r"alivel"))
@borg.on(sudo_cmd(pattern=r"alivel", allow_sudo=True))
async def aliveleg(yes):
    chat = await yes.get_chat()
    edit_time = 5
    """ ========IMAGE========= """
    file1 = "https://telegra.ph/file/a44f1363bddbba84a2b98.jpg"
    file2 = "https://telegra.ph/file/b635b26bcb08c7fe705c9.jpg"
    file3 = "https://telegra.ph/file/e027c90d03bae039ab58e.jpg"
    file4 = "https://telegra.ph/file/21e8ba90ef8b22fa6a864.jpg"
    """ ========IMAGE========= """
    lgd_msg = " LEGEND BOT IS ONLINE\n\n"
    lgd_msg += "Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...\n\n"
    lgd_msg += "✘ About My System ✘\n\n"
    lgd_msg += "➾ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ ☞ 1.17.5\n"
    lgd_msg += "➾ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ☞ [ᴊᴏɪɴ](https://t.me/hackerget0)\n"
    lgd_msg += "➾ ʟɪᴄᴇɴꜱᴇ  ☞ [TEAM LEGEND](https://github.com/legendx22)\n"
    lgd_msg += "➾ group ☞ [LEGEND TEAM](https://t.me/teamishere)\n\n"
    lgd_msg += f"➾ ᴍʏ ᴍᴀsᴛᴇʀ ☞ {DEFAULTUSER}\n"

    on = await borg.send_file(yes.chat_id, file=file1,caption=lgd_msg)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()


@borg.on(admin_cmd(pattern=r"alivesr"))
async def sanalive(ssr_alive):
    chat = await ssr_alive.get_chat()
    await ssr_alive.delete()
    ssr_pic = "https://telegra.ph/file/2f25e6c3b9fa244bee26f.jpg"
    ssr_msg = "**𝚂𝙰𝙽𝚂𝙺𝙰𝚁𝙸 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n"
    ssr_msg += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"
    ssr_msg += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"
    ssr_msg += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n"
    ssr_msg += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support_group)\n"
    ssr_msg += "ʟɪᴄᴇɴꜱᴇ                 : [𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈 𝐁𝐎𝐓](https://github.com/THESANSKARILADKA/SANSKARI-USERBOT/blob/master/LICENSE)\n"
    ssr_msg += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [sᴀɴsᴋᴀʀɪ ʟᴀᴅᴋᴀ](https://github.com/THESANSKARILADKA)\n"

    await borg.send_file(ssr_alive.chat_id, ssr_pic, caption=ssr_msg)
    await ssr_alive.delete() 


@borg.on(admin_cmd(pattern=r"aliveez"))
async def elizalive(aliveez):
    await aliveez.get_chat()
    await aliveez.delete()
    ez_img = "https://telegra.ph/file/ced30b3600c5a4e6b2d8a.jpg"
    ez_msg = " Eliza is Ready to Rock \n\n"
    ez_msg += "System Status\n"
    ez_msg += f" **••Mу Bσѕѕ••**      :   {DEFAULTUSER}\n"
    ez_msg += " **тєℓєтнσи νєяѕισи**  :   1.18.2 \n"
    ez_msg += " **σffι¢ιαℓ ¢нαииєℓ**  :   [ᴊᴏɪɴ](https://t.me/Eliza_Userbot_Support)\n"
    ez_msg += " σffι¢ιαℓ gяσυρ        :   [ᴊᴏɪɴ](https://t.me/Eliza_userbot_group)\n"
    ez_msg += " ℓι¢єиѕє               :   [ӀíϲҽղՏҽ](https://github.com/suhaash02/Eliza/blob/master/LICENSE)\n"

    await borg.send_file(aliveez.chat_id, ez_img, caption=ez_msg)
    await aliveez.delete()


@bot.on(admin_cmd(pattern="alivep$"))
async def pj_alive(alivepj):
        PROJECTDILS_VERSION = "2.9"
        pjd_pic = "https://telegra.ph/file/36df725e1554826a2dfda.png"
      pjd_msg = (
        "`ProjectDils is running...`\n"
        f"`•••••••••••••••••••••••••••••••••••••`\n"
        f"👤 `User           :`  {DEFAULTUSER}\n"
        f"🐍 `Python         : v{python_version()}`\n"
        f"⚙️ `Telethon       : v{version.__version__}`\n"
        f"🤖 `ProjectDils    : v{PROJECTDILS_VERSION}`\n"
        f"🧩 `Loaded Modules : {len(modules)}`\n"
        f"🕒 `Bot Uptime     : {uptime} `\n"
        f"`•••••••••••••••••••••••••••••••••••••`\n"
    )

    await borg.send_file(alivepj.chat_id, pjd_pic, caption=pjd_msg)
    await alivepj.delete()


@bot.on(admin_cmd(pattern="aliver$"))
async def rgr_alive(alivergr):
        rgr_pic = "https://telegra.ph/file/feadbe63818bc695c0417.jpg"
    rgr_msg = "**🔱Ɽǟɢǟռօʀӄɮð† Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
    rgr_msg += "`My Bot Status \n\n\n`"
    rgr_msg += f"`Kernel Type: Monolithic(linux) \n\n`"
    rgr_msg += f"`Kernel: 2.2.9  \n\n`"
    rgr_msg += f"`KDE: 1.1(Red Hat)  \n\n`"
    rgr_msg += "`Default User Interface: KDE Plasma \n\n`"
    rgr_msg += "`Support Channel` : @Raganork_Official \n\n"
    rgr_msg += f"`ᎷᎽ ᏰᏫᏕᏕ`: {DEFAULTUSER} \n\n "

    await borg.send_file(alivergr.chat_id, rgr_pic, caption=rgr_msg)
    await alivergr.delete()


@bot.on(admin_cmd(pattern="alivet$"))
async def tb_alive(alivetb):
    tb_pic = None
    tb_msg = (
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█ \n█░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**TeleBot is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Aditya 🏁](tg://user?id=719195224) \n\n**More help -** @TeleBotHelpChat \n\n           [🚧 GitHub Repository 🚧](https://github.com/xditya/TeleBot)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to TeleBot**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @TeleBotHelpChat \n\n✔️ Created by: [Aditya 🏁](tg://user?id=719195224) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/xditya/TeleBot)"
    )

    await borg.send_file(alivetb.chat_id, tb_pic, caption=tb_msg)
    await alivetb.delete()



CMD_HELP.update(
    {
        "alivefake": "**Alive Fake**\
\n\n**Syntax : **`.alivef`\
\n**Usage :** fake Alive to Friday-USERBOT \
\n\n**Syntax : **`.alivej`\
\n**Usage :** fake Alive to JARVIS-USERBOT\
\n\n**Syntax : **`.alivel`\
\n**Usage :** fake Alive to LEGEND-USERBOT\
\n\n**Syntax : **`.alivec`\
\n**Usage :** fake Alive to Cat-USERBOT\
\n\n**Syntax : **`.alivep`\
\n**Usage :** fake Alive to ProjectDils-USERBOT\
\n\n**Syntax : **`.aliveh`\
\n**Usage :** fake Alive to Hell-USERBOT\
\n\n**Syntax : **`.alivewv`\
\n**Usage :** fake Alive to Wolverine-USERBOT\
\n\n**Syntax : **`.aliveez`\
\n**Usage :** fake Alive to Eliza-USERBOT\
\n\n**Syntax : **`.alivesr`\
\n**Usage :** fake Alive to SANSKARI-USERBOT\
\n\n**Syntax : **`.alivet`\
\n**Usage :** fake Alive to Tele-USERBOT\
\n\n**Syntax : **`.alivesr`\
\n**Usage :** fake Alive to SANSKARI-USERBOT"
    }
)
