import random
import requests
from quote import quote





@bot.on(admin_cmd(pattern="quotee (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    result = quote(input_str, limit=3)
    sed = ""

    for quotes in result:
        sed += str(quotes["quote"]) + "\n\n"

    await event.edit(
        f"<b><u>Quotes of this ➲ </b></u><code>{input_str}</code>\n\n\n<code>{sed}</code>",
        parse_mode="HTML",
    )



@bot.on(admin_cmd(pattern="quote ?(.*)"))
@bot.on(sudo_cmd(pattern="quote ?(.*)", allow_sudo=True))
async def quote_search(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`Processing...`")
    input_str = event.pattern_match.group(1)
    if not input_str:
        api_url = "https://quotes.cwprojects.live/random"
        try:
            response = requests.get(api_url).json()
        except:
            response = None
    else:
        api_url = f"https://quotes.cwprojects.live/search/query={input_str}"
        try:
            response = random.choice(requests.get(api_url).json())
        except:
            response = None
    if response is not None:
        await catevent.edit(f"`{response['text']}`")
    else:
        await edit_delete(catevent, "`Sorry Zero results found`", 5)



@borg.on(admin_cmd(pattern="quotes ?(.*)"))
async def quote_search(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    search_string = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/Telegram/GoodReadsQuotesBot/?q={}".format(search_string)
    headers = {"USER-AGENT": "MODIFIED"}
    try:
        response = requests.get(input_url, headers=headers).json()
    except:
        response = None
    if response is not None:
        result = random.choice(response).get("input_message_content").get("message_text")
    else:
        result = None
    if result:
        await event.edit(result.replace("<code>", "`").replace("</code>", "`"))
    else:
        await event.edit("Nothing was found🚶🏾")




CMD_HELP.update(
    {
        "quotes": "**Quotes**\
\n\n**Syntax : **`.quotee <text>` or `.quotes <text>` \
\n**Usage :** Automatically gets quotes for given plugin.\
\n\n**Syntax : **`.quote <category>`\
\n**Function : **__An api that Fetchs random Quote from `goodreads.com`__"
    }
)
