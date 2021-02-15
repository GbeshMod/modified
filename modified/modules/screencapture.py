"""Take screenshot of any website
Syntax: .screenc or screens <Website URL>"""

import io
import requests
import traceback
from re import match
from asyncio import sleep
from datetime import datetime
from selenium import webdriver
from modified.utils import chrome, options




@modbot.on(modified_cmd("screenc (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        await event.edit(
            "Need to get an API key from https://screenshotlayer.com/product \nModule stopping!"
        )
        return
    await event.edit("Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, input_str, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id,
                )
                await event.delete()
            except Exception as e:
                await event.edit(str(e))
    else:
        await event.edit(response_api.text)


@modbot.on(modified_cmd("screens (.*)"))
async def capture(url):
    """For .ss command, capture a website's screenshot and send the photo."""
    await url.edit("`Processing...`")
    chrome_options = await options()
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.arguments.remove("--window-size=1920x1080")
    driver = await chrome(chrome_options=chrome_options)
    input_str = url.pattern_match.group(1)
    link_match = match(r"\bhttps?://.*\.\S+", input_str)
    if link_match:
        link = link_match.group()
    else:
        return await url.edit("`I need a valid link to take screenshots from.`")
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await url.edit(
        "`Generating screenshot of the page...`"
        f"\n`Height of page = {height}px`"
        f"\n`Width of page = {width}px`"
        f"\n`Waiting ({int(wait_for)}s) for the page to load.`"
    )
    await sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    # saves screenshot of entire page
    driver.quit()
    message_id = url.message.id
    if url.reply_to_msg_id:
        message_id = url.reply_to_msg_id
    with io.BytesIO(im_png) as out_file:
        out_file.name = "screencnap.png"
        await url.edit("`Uploading screenshot as file..`")
        await url.client.send_file(
            url.chat_id,
            out_file,
            caption=input_str,
            force_document=True,
            reply_to=message_id,
        )


CMD_HELP.update(
    {
        "screencapture": "**Screen Capture**\
\n\n**Syntax : **`.screenc <website URL>`\
\n**Usage :** Gets website screenshot.\
\nUsage: Takes a screenshot of a website and sends the screenshot.\
\nExample of a valid URL :`.screens <url>` `https://www.google.com`"
    }
)
