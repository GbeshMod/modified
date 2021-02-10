"""Check your internet speed powered by speedtest.net
Syntax: .speedtest
Available Options: image, file, text"""
import os
import wget
import speedtest
from datetime import datetime
from modified.utils import humanbytes



def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "kilobytes", 2: "megabytes", 3: "gigabytes", 4: "terabytes"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

@modbot.on(modified_cmd("speedtest ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    input_str == "text":
        as_text = True
    await edit_or_reply(
        event, "`Calculating my internet speed. Please wait!`"
    )
    await event.edit("`Running speed test . . .`")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        await event.edit("`Performing download test . . .`")
        test.download()
        await event.edit("`Performing upload test . . .`")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await event.edit(text=e)
        return
    path = wget.download(result['share'])
    output = f"""** ⚡--{BOT_LIN}  took {result['timestamp']}-- ⚡

🛰 Server:

👤 Name ➺ `{result['server']['name']}`
🌍Country ➺ `{result['server']['country']}, {result['server']['cc']}`
🗃 ISP ➺ `{result['client']['isp']}`
💼 Sponsor ➺ `{result['server']['sponsor']}`
📊 Latency ➺ `{result['server']['latency']}`

📡 Ping ➺ `{result['ping']}`
📈 Sent ➺ `{humanbytes(result['bytes_sent'])}`
📉 Received ➺ `{humanbytes(result['bytes_received'])}`
📤 Upload ➺ `{humanbytes(result['upload'] / 8)}/s`
📥 Download ➺ `{humanbytes(result['download'] / 8)}/s`**"""
    await borg.send_file(event.chat_id, photo=path, caption=output)
    os.remove(path)
    await event.delete()


CMD_HELP.update(
    {
        "speedtest": "**Speedtest**\
\n\n**Syntax : **`.speedtest`\
\n**Usage :** check your userbot's internet speed"
    }
)
