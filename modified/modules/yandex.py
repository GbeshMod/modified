import os
import json
import requests
from modified.function import convert_to_image


sedpath = "./yandex/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

@modbot.on(modified_cmd(pattern=r"yandex"))
@modbot.on(sudo_cmd(pattern=r"yandex", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.reply("hmm... Reverse Searching The Image On Yandex...🚶")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    filePath = img
    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    caption = f"""<b>Reverse Search Conpleted!</b>

Reverse Searched Link:- {img_search_url}

Note:- Yandex is a Russian search engine, so better open link in chrome with auto-translate.

Another Note:- Don't Use This Command continually, Yandex Will Block Your Request.


<u><b>Reverse Search Completed By Friday.
Get Your Own Friday From @FRIDAYCHAT.</b></u>

"""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )
    await event.delete()
    

CMD_HELP.update(
    {
        "yandex_reverse_img": "**Yandex Reverse Image search**\
\n\n**Syntax : **`.yandex <reply to image>`\
\n**Usage :** Reverse Searches The Image on yandex."
    }
)

