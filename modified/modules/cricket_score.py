import urllib.request
from bs4 import BeautifulSoup



@modex.on(modified_cmd(pattern="cs"))
async def _(event):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = ""
    for match in result:
        Sed += match.get_text() + "\n\n"
    await event.edit(
        f"<b><u>Match information gathered successful</b></u>\n\n\n<code>{Sed}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "cricket_score": "**Cricket Score**\
\n\n**Syntax : **`.cs`\
\n**Usage :** Gets Live cricket score automatically."
    }
)
