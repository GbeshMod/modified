import asyncio
from collections import deque




@bot.on(admin_cmd(pattern="symbol"))
@bot.on(sudo_cmd(pattern="symbol", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Symbols")
    deq = deque(list("""๑•ิ.•ั๑ ๑۩۞۩๑ ♬✿.｡.:* ★ ☆ εїз℡❣·۰•●○●ōゃ ♥ ♡๑۩ﺴ ☜ ☞ ☎ ☏♡ ⊙◎ ☺ ☻✖╄ஐﻬ ► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ▪ ▫ ☼ ♦ ▀ ▄ █▌ ▐░ ▒ ▬♦ ◊ ◦ ☼ ♠♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ の ☆ → あ ぃ ￡ ❤＃ ＠ ＆ ＊ ❁ ❀ ✿ ✾ ❃ ✺ ❇ ❈ ❊ ❉ ✱ ✲ ✩ ✫ ✬ ✭ ✮ ✰ ☆ ★ ✪ ¤ ☼ ☀ ☽ ☾ ❤ ♡ ღ☻ ☺ ❂ ◕ ⊕ ☉ Θ o O ♋ ☯ ㊝ ⊙ ◎◑ ◐ ۰ • ● ▪ ▫ ｡ ﾟ ๑ ☜ ☞ ☂ ♨ ☎ ☏ × ÷ ＝ ≠ ≒ ∞ ˇ ± √ ⊥▶ ▷ ◀ ◁ ☀ ☁ ☂ ☃ ☄ ★ ☆ ☇ ☈ ☉ ☊ ☋ ☌ ☍ ☑ ☒☢ ☸ ☹ ☺ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁♝ ♞♯♩♪♫♬♭♮ ☎ ☏ ☪ ♈ ♨ ₪ ™ ♂✿ ♥ の ↑ ↓ ← → ↖ ↗ ↙ ↘ ㊣ ◎ ○ ● ⊕ ⊙ ○　 △ ▲ ☆ ★ ◇ ◆ ■ □ ▽ ▼ § ￥ 〒 ￠ ￡ ※ ♀ ♂ &⁂ ℡ ↂ░ ▣ ▤ ▥ ▦ ▧ ✐✌✍✡✓✔✕✖ ♂ ♀ ♥ ♡ ☜ ☞ ☎ ☏ ⊙ ◎ ☺ ☻ ► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ♥ ♡ ▪ ▫ ☼ ♦ ▀ ▄ █ ▌ ▐ ░ ▒ ▬ ♦ ◊ ◘ ◙ ◦ ☼ ♠ ♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ ✄☪☣☢☠░ ▒ ▬ ♦ ◊ ◦ ♠ ♣ ▣ ۰•● ❤ ●•۰► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ▪ ▫ ☼ ♦♧♡♂♀♠♣♥❤☜☞☎☏⊙◎ ☺☻☼▧▨♨◐◑↔↕▪ ▒ ◊◦▣▤▥ ▦▩◘ ◈◇♬♪♩♭♪の★☆→あぃ￡Ю〓§♤♥▶¤๑⊹⊱⋛⋌⋚⊰⊹ ๑۩۩.. ..۩۩๑ ๑۩۞۩๑ ✲ ❈ ✿ ✲ ❈ ➹ ~.~ ◕‿- ❣ ✚ ✪ ✣ ✤ ✥ ✦❉ ❥ ❦ ❧ ❃ ❂ ❁ ❀ ✄ ☪ ☣ ☢ ☠ ☭ღღღ ▶ ▷ ◀ ◁ ☀ ☁ ☂ ☃ ☄ ★ ☆ ☇ ☈ ⊙ ☊ ☋ ☌ ☍ⓛⓞⓥⓔ๑•ิ.•ั๑ ๑۩۞۩๑ ♬✿ ☉♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ❤ ❥ ❦❧ ➳ ➽ εїз℡❣·۰•●○●ゃōゃ♥ ♡๑۩ﺴ ☜ ☞ ☎ ☏♡ ⊙◎ ☺ ☻✖╄ஐﻬ ► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ▪ ▫ ☼ ♦ ▀ ▄ █▌ ▐░ ▒ ▬♦ ◊ ◦ ☼ ♠♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ の ☆ → あ ぃ ￡ ❤ ❁ ❀ ✿ ✾ ❃ ✺ ❇ ❈ ❊ ❉ ✱ ✲ ✩ ✫ ✬ ✭ ✮ ✰ ☆ ★ ✪ ¤ ☼ ☀ ☽ ☾ ❤ ♡ ღ☻ ☺ ❂ ◕ ⊕ ☉ Θ o O ♋ ☯ ㊝ ⊙ ◎ ◑ ◐ ۰ • ● ▪ ▫ ｡ ﾟ ๑ ☜ ☞ ☂ ♨ ☎ ☏▶ ▷ ◀ ◁ ☀ ☁ ☂ ☃ ☄ ★ ☆ ☇ ☈ ☉ ☊ ☋ ☌ ☍ ☑ ☒☢ ☸ ☹ ☺ ☻ ☼ ☽ ☾ ♠ ♝ ♞♯♩♪♫♬♭♮ ☎ ☏ ☪ ♈ ♨ ºº ₪ ¤ 큐 « »™ ♂✿ ♥ の ↑ ↓ ← → ↖ ↗ ↙ ↘ ㊣ ◎ ○ ● ⊕ ⊙ ○　 △ ▲ ☆ ★ ◇ ◆ ■ □ ▽ ▼ § ￥〒 ￠ ￡ ※ ♀ ♂ © ® ⁂ ℡ ↂ░ ▣ ▤ ▥ ▦ ▧ ✐✌✍✡✓✔✕✖ ♂ ♀ ♥ ♡ ☜ ☞ ☎ ☏ ⊙ ◎ ☺ ☻ ► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ♥ ♡ ▪ ▫ ☼ ♦ ▀ ▄ █ ▌ ▐ ░ ▒ ▬ ♦ ◊ ◘ ◙ ◦ ☼ ♠ ♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ ✄☪☣☢☠㊊㊋㊌㊍㊎㊏ ㊐㊑㊒㊓㊔㊕㊖㊗㊘㊜㊝㊞㊟㊠㊡㊢ ㊣㊤㊥㊦㊧㊨㊩㊪㊫㊬㊭㊮㊯㊰✗✘✚✪✣✤✥✦✧✩✫✬✭✮✯✰ ✱✲✳❃❂❁❀✿✾✽✼✻✺✹✸✷ ✶✵✴❄❅❆❇❈❉❊❋❖☀☂☁【】┱ ┲ ❣ ✪ ✣ ✤ ✥ ✦ ❉ ❥ ❦ ❧ ❃ ❂ ❁ ❀ ✄ ☪ ☣ ☢ ☠ ☭ ♈ ➸ ✓ ✔ ✕ ✖ .: ◢ ◣ ◥ ◤ ▽ ▧ ▨ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ▓ ▒ ░ ™ ℡ 凸 の ๑۞๑ ๑۩ﺴ ﺴ۩๑ o(‧”’‧)o ❆ べò⊹⊱⋛⋋ ⋌⋚⊰⊹ ⓛⓞⓥⓔ ☀ ☼ ☜ ☞ ⊙® ◈ ♦ ◊ ◦ ◇ ◆ εїз❃❂❁❀✿✾✽✼✻✺✹✸✷ ✶✵✴❄❅❆❇❈❉ ❊❋❖❤❥❦❧↔ ↕ ▪ → ︷╅╊✿ (¯`•._.• •._.•´¯)(¯`•¸•´¯) ❤`•.¸¸.•´´¯`•• .¸¸.•´¯`•.•●•۰• ••.•´¯`•.•• ••.•´¯`•.••—¤÷(`[¤* *¤]´)÷¤——(•·÷[ ]÷·•)— ①②③④⑤⑥⑦⑧⑨⑩ ⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ ⒶⒷⒸⒹⒺⒻ ⒼⒽⒾⒿⓀⓁ ⓂⓃⓄⓅⓆⓇ ⓈⓉⓊⓋⓌⓍ ⓎⓏ ⓐⓑⓒⓓⓔⓕ ⓖⓗⓘⓙⓚⓛ ⓜⓝⓞⓟⓠⓡ ⓢⓣⓤⓥⓦⓧ ⓨⓩ(⊙▂⊙✖ )(づ ￣ ³￣)づ ( c//”-}{-*\\x)(-’๏_๏’-)(◐ o ◑ )(⊙…⊙ )๏[-ิ_•ิ]๏(•ิ_•ิ)\(•ิ_•ิ\) (/•ิ_•ิ)(︶︹︺)"""))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)





@bot.on(admin_cmd(pattern="think$"))
@bot.on(sudo_cmd(pattern="think$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"lul$"))
@bot.on(sudo_cmd(pattern="lul$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "lul")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"nothappy$"))
@bot.on(sudo_cmd(pattern="nothappy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="clock$"))
@bot.on(sudo_cmd(pattern="clock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"muah$"))
@bot.on(sudo_cmd(pattern="muah$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="heart$"))
@bot.on(sudo_cmd(pattern="heart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="gym$"))
@bot.on(sudo_cmd(pattern="gym$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"earth$"))
@bot.on(sudo_cmd(pattern="earth$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="moon$"))
@bot.on(sudo_cmd(pattern="moon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"smoon$"))
@bot.on(sudo_cmd(pattern="smoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"tmoon$"))
@bot.on(sudo_cmd(pattern="tmoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(117)
    await event.edit("tmoon")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

@bot.on(admin_cmd(pattern=f"hart$"))
@bot.on(sudo_cmd(pattern=f"hart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await edit_or_reply(event, "❤️")
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=f"anim$"))
@bot.on(sudo_cmd(pattern=f"anim$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "😁",
        "😧",
        "😡",
        "😢",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=f"fnl$"))
@bot.on(sudo_cmd(pattern=f"fnl$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(6)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"monkey$"))
@bot.on(sudo_cmd(pattern=f"monkey$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"hand$"))
@bot.on(sudo_cmd(pattern=f"hand$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=f"gsg$"))
@bot.on(sudo_cmd(pattern=f"gsg$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(12)
    event = await edit_or_reply(event, "ContDown....")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"theart$"))
@bot.on(sudo_cmd(pattern=r"theart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


@borg.on(admin_cmd("bigoof"))
@bot.on(sudo_cmd(pattern=r"bigoof", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    await event.edit("┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛")
    animation_chars = [
            "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
            "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 40])

@borg.on(admin_cmd(pattern=r"fdance"))
@bot.on(sudo_cmd(pattern=r"fdance", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 5)
    await event.edit("Connecting..")
    animation_chars = [
        
            "⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣿⣿⣿⣀/n⠀⣀⣿⣿⣿⣿⣿⣿/n⣶⣿⠛⣭⣿⣿⣿⣿/n⠛⠛⠛⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣀⣭⣿⣿⣿⣿⣀/n⠀⠤⣿⣿⣿⣿⣿⣿⠉/n⠀⣿⣿⣿⣿⣿⣿⠉/n⣿⣿⣿⣿⣿⣿/n⣿⣿⣶⣿⣿/n⠉⠛⣿⣿⣶⣤/n⠀⠀⠉⠿⣿⣿⣤/n⠀⠀⣀⣤⣿⣿⣿/n⠀⠒⠿⠛⠉⠿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⣶⠿⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀/n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀/n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉/n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉/n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶/n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶/n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤/n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀/n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿/n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶/n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒/n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉/n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛/n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭/n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤/n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿/n⠀⠀⠀⠀⠀⠀⣿⠛/n⠀⠀⠀⠀⠀⠀⣭⣶/n",
            "⠀⠀⠀⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣤⣤⣤⣿⣿⣿/n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿/n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶/n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤/n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿/n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉/n⠀⠀⠀⣿⣿⣿⣿⣿⣶/n⠀⠀⠀⠀⣿⠉⠿⣿⣿/n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿/n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉/n",
            "⠀⠀⠀⠀⠀⠀⣤⣶⣶/n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀/n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿/n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿/n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿/n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿/n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿/n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛/n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀/n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿/n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿/n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿/n⠀⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⠤⣿⠿⠿⠿/n",    


 ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])



@bot.on(admin_cmd(pattern=f"source$"))
@bot.on(sudo_cmd(pattern=f"source$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    event = await edit_or_reply(event, "Hey There  Repository ....")
    animation_chars = [
      "https"
      "https://"
      "https://github"
      "https://github.com"
      "https://github.co"
      "https://github.c"
      "https://github.com"
      "https://github.com/Gbesh"
      "https://github.com/GbeshMod"
      "https://github.com"
      "https://githu"
      "https://github.com"
      "https://github.com/GbeshMod/"
      "https://github.com/GbeshMod/mode"
      "https://github.com/GbeshMod/mod"
      "https://github.com/GbeshMod/modi"
      "https://github.com/GbeshMod/modif"
      "https://github.com/GbeshMod/modifi"
      "https://github.com/GbeshMod/modifie"
      "🙄  ➠➠ https://github.com/GbeshMod/modified"
      f"🙄  ➠➠  Cick [here 🚪](https://github.com/GbeshMod/modified) to open this 🔥** LIT fix **🔥 __{BOT_N_N} BOT__ Repo...."
      ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 2])


CMD_HELP.update(
    {
        "source": "**Source Code**\
\n\n**Syntax : **`.source`\
\n**Usage :** Provides repository link."
    }
)


CMD_HELP.update(
    {
        "animation4": """**Animation4**
        
**Commands in animoji are **
  •  `.think`
  •  `.lul`
  •  `.nothappy`
  •  `.clock`
  •  `.muah`
  •  `.heart`
  •  `.gym`
  •  `.earth`
  •  `.moon`
  •  `.smoon`
  •  `.tmoon`
  •  `.hart`
  •  `.anim`
  •  `.fnl`
  •  `.monkey`
  •  `.hand`
  •  `.gsg   try   .symbol`
  •  `.theart .bigoof .fdance`
   Try .help source 
**Function : **__Different kinds of emoji animation commands check yourself for their animation .__"""
    }
)
