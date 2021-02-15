
import requests
from telethon import events
from datetime import datetime
from iplookup import iplookup
from selenium import webdriver
from youtube_search import YoutubeSearch



@modbot.on(sudo_cmd(pattern="ahelp ?(.*)"))
@modbot.on(modified_cmd(pattern="ahelp ?(.*)"))
async def _(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"Here is some help for the {CMD_HELP[args]}")
        else:
            await event.edit(
                f"Help string for {args} not found! Type `.help` to see valid module names."
            )
    else:
        string = ""
        for i in CMD_HELP.values():
            string += f"`{str(i[0])}`, "
        string = string[:-2]
        await event.edit(
            "Please specify which module you want help for!\n\n" f"{string}"
        )


import requests

@friday.on(friday_on_cmd(pattern="runcode ?(.*)"))
@friday.on(sudo_cmd(pattern="runcode ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await edit_or_reply(event, "Reply To The Code 💥.")
        return
    input_str = event.pattern_match.group(1)
    if input_str == None:
      ommhg = await edit_or_reply(event, "Which Language is That? select a language from here. c#, vb.net, f#, java, python, c (gcc), c++ (gcc), php, pascal, objective-c, haskell, ruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, scheme, node.js, python 3, octave, c (clang), c++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, bash, ada, erlang, elixir, ocaml, kotlin, brainfuck, fortran")
      return
    langs = ["c#", "vb.net", "f#", "java", "python", "c (gcc)", "c++ (gcc)", "php", "pascal", "objective-c", "haskell", "ruby", "perl", "lua", "nasm", "sql server", "javascript", "lisp", "prolog", "go", "scala", "scheme", "node.js", "python 3", "octave", "c (clang)", "c++ (clang)", "c++ (vc++)", "c (vc)", "d", "r", "tcl", "mysql", "postgresql", "oracle", "swift", "bash", "ada", "erlang", "elixir", "ocaml", "kotlin", "brainfuck", "fortran"]
    
    input_st = input_str
    credits = f"{BOT_N_N} is the best. By {DEFAULTUSER}.."
    
    reply_message = await event.get_reply_message()
    co = credits
    input_str = co[0]
    if input_st.lower() in langs:
      pass
    else:
      ommhg = await edit_or_reply(event, "Language Not Found. select a language from here. c#, vb.net, f#, java, python, c (gcc), c++ (gcc), php, pascal, objective-c, haskell, ruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, scheme, node.js, python 3, octave, c (clang), c++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, bash, ada, erlang, elixir, ocaml, kotlin, brainfuck, fortran")
      return
    
    kl = "flow language"
    if kl[0] == input_str:
      token = "5b5f0ad8-705a-4118-87d4-c0ca29939aed"
    else:
      token = "5b5f0ad8-705a-4118-87d4-c0ca29939aeb"
    dat = {
      "code":reply_message.text,
      "lang":input_st,
      "token":token
    }

    r = requests.post("https://peaceapi.herokuapp.com/compiler", data = dat).json()
    
    if r.get("reason") !=None:
      a = r
      result = a.get("results")
      error = a.get("errors")
      stats = a.get("stats")
      success = a.get("success")
      warnings = a.get("warnings")
      rn = a.get("reason")
      Bobby = f"""
Results ➼ {result}
Errors ➼ {error}
Stats ➼ {stats}
Success ➼ {success}
warnings ➼ {warnings}
Reason ➼ {rn}
"""
    
      ommhg = await edit_or_reply(event, Bobby)
      return
    
    
    a = r
    result = a.get("results")
    error = a.get("errors")
    stats = a.get("stats")
    success = a.get("success")
    warnings = a.get("warnings")
    Bobby = f"""
Results ➼ {result}
Errors ➼ {error}
Stats ➼ {stats}
Success ➼ {success}
warnings ➼ {warnings}
"""
    
    ommhg = await edit_or_reply(event, Bobby)



@modbot.on(modified_cmd(pattern="xtools ?(.*)"))
@modbot.on(sudo_cmd(pattern="xtools ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        username = previous_message.message
        sub_domain = input_str
    else:
        sub_domain, username = input_str.split("|")
    final_url = "https://xtools.wmflabs.org/api/user/simple_editcount/{}.wikipedia.org/{}".format(sub_domain, username)
    json_string = requests.get(final_url).json()
    result_text = json_string["liveEditCount"]
    end = datetime.now()
    ms = (end - start).seconds
    output_str = "edit count of {} ({}) in {} seconds. \n {}".format(
        username, sub_domain, str(ms), result_text)
    await event.edit(output_str)



@modbot.on(modified_cmd(pattern="webshot ?(.*)"))
@modbot.on(sudo_cmd(pattern="webshot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    sedlyfpeacey = await edit_or_reply(event, "Capturing Webshot, Stay Tuned.")
    driver = webdriver.Chrome()
    driver.get(urlissed)
    driver.get_screenshot_as_file("Webshot.png")
    imgpath = "Webshot.png"
    await sedlyfpeacey.edit("Completed. Uploading in Telegram..")
    await borg.send_file(
        event.chat_id,
        file=imgpath,
        caption=f"**WEBSHOT OF** `{urlissed}` \n**Powered By {BOT_LIN}**",
    )
    
    
@modbot.on(modified_cmd(pattern="rmeme$"))
@modbot.on(sudo_cmd(pattern="rmeme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    hmm_s = 'https://some-random-api.ml/meme'
    r = requests.get(url=hmm_s).json()
    image_s = r['image']
    await borg.send_file(event.chat_id, file=image_s, caption=r['caption'])
    

@modbot.on(modified_cmd(pattern="whoiz ?(.*)"))
@modbot.on(sudo_cmd(pattern="whoiz ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfbro = await edit_or_reply(event, "Wait Fetching Website Info")
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain=" + gone
        await event.edit(
            "Fecthing Website Info ! Stay Tuned. This may take some time ;)"
        )
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (
            f'Domain Name ⪼⪼ {sed["domain"]} \nCreated On ⪼⪼ {sed["create_date"]} \nDomain ID ⪼⪼ {sed["domain_id"]} \nHosted ON ⪼⪼ {kek["url"]}'
            f'\nLast updated ⪼⪼ {sed["update_date"]} \nExpiry Date ⪼⪼ {sed["expire_date"]} \nDomain Age ⪼⪼ {sed["domain_age"]}'
            f'\nOwner ⪼⪼ {km["name"]} \nCountry ⪼⪼ {km["country"]} \nState ⪼⪼ {km["region"]}'
            f'\nPhone Number ⪼⪼ {km["phone"]} \nDomain Ip ⪼⪼ {okthen}'
        )
        await tfbro.edit(sedlyf)
    except Exception:
        await tfbro.edit(f"Something Went Wrong. MayBe Website Wrong... I forgot to tell you.. this is for web🌐.➠➠ ")


@modbot.on(modified_cmd(pattern="bin ?(.*)"))
@modbot.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfsir = await edit_or_reply(event, "Wait Fetching Bin Info")
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (
            f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
            f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
            f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
            f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
            f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n"
        )
        await tfsir.edit(data_is, parse_mode="HTML")
    except:
        await tfsir.edit("Not a Valid Bin Or Don't Have Enough Info.")


@modbot.on(modified_cmd(pattern="iban ?(.*)"))
@modbot.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        tfhm = await edit_or_reply(event, "Wait Fetching IBAN Info")
        banks = lol["bankData"]
        kek = (
            f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
            f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
            f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
            f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
            f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
            f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
            f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n"
        )
        await tfhm.edit(kek, parse_mode="HTML")
    except:
        await tfhm.edit(f"Invalid IBAN Or Doesn't Have Enough Info")


@modbot.on(modified_cmd(pattern="gitdl ?(.*)"))
@modbot.on(sudo_cmd(pattern="gitdl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        kekman = await edit_or_reply(event, "Fetching Repo")
        inputs = event.pattern_match.group(1)
        sed = event.pattern_match.group(1)
        if sed:
            if " " in sed:
                peace = inputs.split(" ", 2)
        gitusername = peace[0]
        gitrepo = peace[1]
        gitbranch = peace[2]
        link = f"https://github.com/{gitusername}/{gitrepo}/archive/{gitbranch}.zip"
        await kekman.edit("Uploading... peace Tuned.")
        await event.delete()
        await borg.send_file(event.chat_id, file=link, caption="You Repo Achieve File.")
    except:
        await borg.send_message(
            event.chat_id, "**Usage** ➼ `.gitdl <gitusername> <gitrepo> <gitbranch>`"
        )




CMD_HELP.update(
    {
        "webtools": "**Web Tools**\
\n\n**Syntax : **`.webshot <website URL>`\
\n**Usage :** takes screenshot of webpage.\
\n\n**Syntax : **`.whoiz <URL link>`\
\n**Usage :** Gives whois information about website.\
\n\n**Syntax : **`.bin <bin>`\
\n**Usage :** Provides information about bin.\
\n\n**Syntax : **`.iban <iban>`\
\n**Usage :** Provides information about IBAN.\
\n\n**Syntax : **`.gitdl <repository name>`\
\n**Usage :** Gets repository link. try  .runcode   .xtools"
    }
)
