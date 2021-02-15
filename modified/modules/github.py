"""
Get information about an user on GitHub
Syntax: .github USERNAME

GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. 
.commitgit
Instructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First
"""


from github import Github
import aiohttp
import asyncio
import os
import time
import requests
from userbot import CMD_HELP
from datetime import datetime
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from modified.util import admin_cmd, humanbytes, progress, time_formatter


GIT_TEMP_DIR = "./github/"
BRANCH = "test"

@borg.on(admin_cmd(pattern="gitcommit ?(.*)", allow_sudo=True))
async def download(event):
	if event.fwd_from:
		return	
	if Config.GITHUB_ACCESS_TOKEN is None:
		await event.edit("`Please ADD Proper Access Token from github.com`") 
		return   
	if Config.GIT_REPO_NAME is None:
		await event.edit("`Please ADD Proper Github Repo Name of your userbot`")
		return 
	mone = await event.reply("Processing ...")
	input_str = event.pattern_match.group(1)
	if not os.path.isdir(GIT_TEMP_DIR):
		os.makedirs(GIT_TEMP_DIR)
	start = datetime.now()
	reply_message = await event.get_reply_message()
	try:
		c_time = time.time()
		downloaded_file_name = await borg.download_media(
			reply_message,
			GIT_TEMP_DIR,
			progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
			progress(d, t, mone, c_time, "trying to download")
			)
		)
	except Exception as e: 
		await mone.edit(str(e))
	else:
		end = datetime.now()
		ms = (end - start).seconds
		await event.delete()
		await mone.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
		await mone.edit("Committing to Github....")
		await git_commit(downloaded_file_name,mone)

async def git_commit(file_name,mone):        
	content_list = []
	access_token = Config.GITHUB_ACCESS_TOKEN
	g = Github(access_token)
	file = open(file_name,"r",encoding='utf-8')
	commit_data = file.read()
	repo = g.get_repo(Config.GIT_REPO_NAME)
	print(repo.name)
	create_file = True
	contents = repo.get_contents("")
	for content_file in contents:
		content_list.append(str(content_file))
		print(content_file)
	for i in content_list:
		create_file = True
		if i == 'ContentFile(path="'+file_name+'")':
			return await mone.edit("`File Already Exists`")
			create_file = False
	file_name = "stdplugins/"+file_name		
	if create_file == True:
		file_name = file_name.replace("./temp/","")
		print(file_name)
		try:
			repo.create_file(file_name, "Uploaded New Plugin", commit_data, branch=BRANCH)
			print("Committed File")
			await mone.edit("`Committed on Your Github Repo.`")
		except:
			print("Cannot Create Plugin")
			await mone.edit("Cannot Upload Plugin")
	else:
		return await mone.edit("`Committed Suicide`")


	@borg.on(admin_cmd("github (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://api.github.com/users/{}".format(input_str)
    r = requests.get(url)
    if r.status_code != 404:
        b = r.json()
        avatar_url = b["avatar_url"]
        html_url = b["html_url"]
        gh_type = b["type"]
        name = b["name"]
        company = b["company"]
        blog = b["blog"]
        location = b["location"]
        bio = b["bio"]
        created_at = b["created_at"]
        await borg.send_file(
            event.chat_id,
            caption="""👤 Name: [{}]({})
✍️ Type: {}
🏢 Company: {}
🎖 Blog: {}
🌍 Location: {}
🌬 Bio: {}
⏳ Profile Created: {}""".format(name, html_url, gh_type, company, blog, location, bio, created_at),
            file=avatar_url,
            force_document=False,
            allow_cache=False,
            reply_to=event
        )
        await event.delete()
    else:
        await event.edit("`{}`: {}".format(input_str, r.text))

CMD_HELP.update(
    {
        "github": "**GitHub**\
\n\n**Syntax : **`.github <username>`\
\n**Usage :** Get information about an user on GitHub...\n\n **Syntax : ** .gitcommit file \n GITHUB File Uploader Plugin for userbot.. "
    }
)
