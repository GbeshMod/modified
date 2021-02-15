import os
from seoanalyzer import analyze




@modbot.on(admin_cmd(pattern="seo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("processing please wait ")
    site = input_str
    try:
      
      cmd = "seoanalyze " + site + " --output-format html > seo.html"
      os.system(cmd)
    
      await event.client.send_file(
        event.chat_id,
        "seo.html",
        caption=f"**Site SEO Analysed Successfully\n\nNote: Open This File With Chrome Or Any Browser\n\n\nSite Analysed By {BOT_N_N}",
      )
      com = "rm seo.html"
      os.system(com)
      await event.delete()
    except:
      await event.edit("Make Sure The Given Website URL is valid.")
    com = "rm seo.html"
    os.system(com)
    await event.delete()
    
    
    
    


CMD_HELP.update(
    {
        "seotools": "**Seo Tools**\
\n\n**Syntax : **`.seo <website URL>`\
\n**Usage :** Analyses SEO Of The Website.\
\n\n\n**Note : ** If The Website is too big, Userbot Crashes Because Of Insufficient Memory"
    }
)
