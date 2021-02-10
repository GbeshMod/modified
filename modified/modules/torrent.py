"""
Torrent all in one

"""
import os
import json
import aria2p
import codecs
import asyncio
import cfscrape
import requests
from telethon import events
from datetime import datetime
from ..utils import humanbytes
from bs4 import BeautifulSoup as bs
TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY




cmd = "aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800  --max-connection-per-server=10 --rpc-max-request-size=1024M --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=10 --daemon=true --allow-overwrite=true"
EDIT_SLEEP_TIME_OUT = 5
aria2_is_running = os.system(cmd)

aria2 = aria2p.API(
		aria2p.Client(
			host="http://localhost",
			port=6800,
			secret=""
		)
	)





@borg.on(admin_cmd(pattern=r"tmagnet"))
async def magnet_download(event):
	if event.fwd_from:
		return
	var = event.text
	var = var[8:]
	
	magnet_uri = var
	magnet_uri = magnet_uri.replace("`","")
	logger.info(magnet_uri)
	try: #Add Magnet URI Into Queue
		download = aria2.add_magnet(magnet_uri)
	except Exception as e:
		logger.info(str(e))
		await event.edit("Error :\n{}".format(str(e)))
		return
	gid = download.gid
	await progress_status(gid=gid,event=event,previous=None)
	await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
	new_gid = await check_metadata(gid)
	await progress_status(gid=new_gid,event=event,previous=None)

@borg.on(admin_cmd(pattern=r"tor"))
async def torrent_download(event):
	if event.fwd_from:
		return
	var = event.text[5:]
	torrent_file_path = var	
	torrent_file_path = torrent_file_path.replace("`","")
	logger.info(torrent_file_path)
	try: #Add Torrent Into Queue
		download = aria2.add_torrent(torrent_file_path, uris=None, options=None, position=None)
	except Exception as e:
		await event.edit("Error :\n`{}`".format(str(e)))
		return
	gid = download.gid
	await progress_status(gid=gid,event=event,previous=None)

@borg.on(admin_cmd(pattern=r"turl"))
async def magnet_download(event):
	if event.fwd_from:
		return
	var = event.text[5:]
	print(var)	
	uris = [var]
	try: # Add URL Into Queue
		download = aria2.add_uris(uris, options=None, position=None)
	except Exception as e:
		logger.info(str(e))
		await event.edit("Error :\n`{}`".format(str(e)))
		return
	gid = download.gid
	await progress_status(gid=gid,event=event,previous=None)
	file = aria2.get_download(gid)
	if file.followed_by_ids:
		new_gid = await check_metadata(gid)
		await progress_status(gid=new_gid,event=event,previous=None)

@borg.on(admin_cmd(pattern=r"tremove"))
async def remove_all(event):
	if event.fwd_from:
		return
	try:
		removed = aria2.remove_all(force=True)	
		aria2.purge_all()
	except:
		pass
	if removed == False:  #If API returns False Try to Remove Through System Call.
		os.system("aria2p remove-all")
	await event.edit("`Removed All Downloads.`")  

@borg.on(admin_cmd(pattern=r"tshow"))
async def show_all(event):
	if event.fwd_from:
		return
	output = "output.txt"
	downloads = aria2.get_downloads() 
	msg = ""
	for download in downloads:
		msg = msg+"File: `"+str(download.name) +"`\nSpeed: "+ str(download.download_speed_string())+"\nProgress: "+str(download.progress_string())+"\nTotal Size: "+str(download.total_length_string())+"\nStatus: "+str(download.status)+"\nETA:  "+str(download.eta_string())+"\n\n"
	if len(msg) <= 4096:
		await event.edit("`Current Downloads: `\n"+msg)
	else:
		await event.edit("`Output is huge. Sending as a file...`")
		with open(output,'w') as f:
			f.write(msg)
		await asyncio.sleep(2)	
		await event.delete()	
		await borg.send_file(
			event.chat_id,
			output,
			force_document=True,
			supports_streaming=False,
			allow_cache=False,
			reply_to=event.message.id,
			)				

async def check_metadata(gid):
	file = aria2.get_download(gid)
	new_gid = file.followed_by_ids[0]
	logger.info("Changing GID "+gid+" to "+new_gid)
	return new_gid	

async def progress_status(gid,event,previous):
	try:
		file = aria2.get_download(gid)
		if not file.is_complete:
			if not file.error_message:
				msg = "Downloading File: `"+str(file.name) +"`\nSpeed: "+ str(file.download_speed_string())+"\nProgress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nStatus: "+str(file.status)+"\nETA:  "+str(file.eta_string())+"\n\n"
				if previous != msg:
					await event.edit(msg)
					previous = msg
			else:
				logger.info(str(file.error_message))
				await event.edit("Error : `{}`".format(str(file.error_message)))		
				return
			await asyncio.sleep(EDIT_SLEEP_TIME_OUT)	
			await progress_status(gid,event,previous)
		else:
			await event.edit("File Downloaded Successfully: `{}`".format(file.name))
			return
	except Exception as e:
		if " not found" in str(e) or "'file'" in str(e):
			await event.edit("Download Canceled :\n`{}`".format(file.name))
			return
		elif " depth exceeded" in str(e):
			file.remove(force=True)
			await event.edit("Download Auto Canceled :\n`{}`\nYour Torrent/Link is Dead.".format(file.name))
		else:
			logger.info(str(e))
			await event.edit("Error :\n`{}`".format(str(e)))
			return			


def dogbin(magnets):
    counter = 0
    urls = []
    while counter != len(magnets):
        message = magnets[counter]
        url = "https://del.dog/documents"
        r = requests.post(url, data=message.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        urls.append(url)
        counter += 1
    return urls


@bot.on(admin_cmd(pattern="tsearch ?(.*)"))
async def tor_search(event):
    if event.fwd_from:
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    search_str = event.pattern_match.group(1)
    await event.edit("Searching for " + search_str + ".....")
    if " " in search_str:
        search_str = search_str.replace(" ", "+")
        print(search_str)
        res = requests.get(
            "https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="
            + search_str,
            headers,
        )
    else:
        res = requests.get(
            "https://www.torrentdownloads.me/search/?search=" + search_str, headers
        )
    source = bs(res.text, "lxml")
    urls = []
    magnets = []
    titles = []
    counter = 0
    for div in source.find_all("div", {"class": "grey_bar3 back_none"}):
        # print("https://www.torrentdownloads.me"+a['href'])
        try:
            title = div.p.a["title"]
            title = title[20:]
            titles.append(title)
            urls.append("https://www.torrentdownloads.me" + div.p.a["href"])
        except KeyError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        if counter == 15:
            break
        counter += 1
    if not urls:
        await event.edit("Either the Keyword was restricted or not found..")
        return
    for url in urls:
        res = requests.get(url, headers)
        # print("URl: "+url)
        source = bs(res.text, "lxml")
        for div in source.find_all("div", {"class": "grey_bar1 back_none"}):
            try:
                mg = div.p.a["href"]
                magnets.append(mg)
            except Exception:
                pass
    shorted_links = dogbin(magnets)
    msg = ""
    try:
        search_str = search_str.replace("+", " ")
    except BaseException:
        pass
    msg = "**Torrent Search Query**\n`{}`".format(search_str) + "\n**Results**\n"
    counter = 0
    while counter != len(titles):
        msg = (
            msg
            + "⁍ [{}]".format(titles[counter])
            + "({})".format(shorted_links[counter])
            + "\n\n"
        )
        counter += 1
    await event.edit(msg, link_preview=False)

@bot.on(admin_cmd(pattern=r"tmovie (tor|ido) (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Processing ...")
    input_type = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    search_results = []
    if input_type == "tor":
        search_results = search_torrentz_eu(input_str)
    elif input_type == "ido":
        search_results = search_idop_se(input_str)
    logger.info(search_results)
    output_str = ""
    i = 0
    for result in search_results:
        if i > 10:
            break
        message_text = (
            "👉 <a href=https://t.me/TorrentSearchRoBot?start="
            + result["hash"]
            + ">"
            + result["title"]
            + ": "
            + "</a>"
            + " \r\n"
        )
        message_text += " FILE SIZE: " + result["size"] + "\r\n"
        # message_text += " Uploaded " + result["date"] + "\r\n"
        message_text += (
            " SEEDS: " + result["seeds"] + " PEERS: " + result["peers"] + " \r\n"
        )
        message_text += "===\r\n"
        output_str += message_text
        i += 1
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"Scrapped {input_type} for {input_str} in {ms} seconds. Obtained Results: \n {output_str}",
        link_preview=False,
        parse_mode="html",
    )

def search_idop_se(search_query):
    r = []
    url = "https://idope.se/search/{}/".format(search_query)
    raw_json = requests.get(url).json()
    results = raw_json["result"]["items"]
    for item in results:
        # The content scrapped on 24.09.2018 22:56:45
        title = item["name"]
        t_hash = item["info_hash"]
        age = item["create_time"]
        size = item["length"]
        seeds = str(item["seeds"])
        r.append(
            {
                "title": title,
                "hash": t_hash,
                "age": age,
                "size": humanbytes(size),
                "seeds": seeds,
                "peers": "NA",
            }
        )
    return r

def search_torrentz_eu(search_query):
    r = []
    url = "https://torrentz2eu.org/searchA?safe=1&f=" + search_query + ""
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    raw_html = scraper.get(url).content
    # print(raw_html)
    soup = bs(raw_html, "html.parser")
    results = soup.find_all("div", {"class": "results"})
    # print(results)
    if len(results) > 0:
        results = results[0]
        for item in results.find_all("dl"):
            # print(item)
            # The content scrapped on 23.06.2018 15:40:35
            dt = item.find_all("dt")[0]
            dd = item.find_all("dd")[0]
            #
            try:
                link_and_text = dt.find_all("a")[0]
                link = link_and_text.get("href")[1:]
                title = link_and_text.get_text()
                span_elements = dd.find_all("span")
                date = span_elements[1].get_text()
                size = span_elements[2].get_text()
                seeds = span_elements[3].get_text()
                peers = span_elements[4].get_text()
                #
                r.append(
                    {
                        "title": title,
                        "hash": link,
                        "date": date,
                        "size": size,
                        "seeds": seeds,
                        "peers": peers,
                    }
                )
            except BaseException:
                pass
    return r

@borg.on(admin_cmd(pattern=r"torrent1 (?: |$)(.*)"))
async def torrent(event):
    await event.edit("**Searching...**")
    query = event.pattern_match.group(1)
    response = requests.get(
        f"https://sjprojectsapi.herokuapp.com/torrent/?query={query}")
    try:
        ts = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        return await event.edit(
            "**Error: API is down right now, try again later.**")
    if ts != response.json():
        return await event.edit(
            "**Error: API is down right now, try again later.**")
    listdata = ""
    run = 0
    while True:
        try:
            run += 1
            r1 = ts[run]
            list1 = "<-----{}----->\nName: {}\nSeeders: {}\nSize: {}\nAge: {}\n<--Magnet Below-->\n{}\n\n\n".format(
                run, r1["name"], r1["seeder"], r1["size"], r1["age"], r1["magnet"]
            )
            listdata = listdata + list1
        except BaseException:
            break

    if not listdata:
        return await e.edit("`Error: No results found`")

    tsfileloc = f"{TEMP_DOWNLOAD_DIRECTORY}/{query}.txt"
    with open(tsfileloc, "w+", encoding="utf8") as out_file:
        out_file.write(str(listdata))
    fd = codecs.open(tsfileloc, "r", encoding="utf-8")
    data = fd.read()
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/raw/{key}"
    caption = (
        f"`Here the results for the query: {query}`\n\nPasted to: [Nekobin]({url})"
    )
    os.remove(tsfileloc)
    await e.edit(caption, link_preview=False)

@borg.on(admin_cmd(pattern=r"torrent +(.*)"))
async def torr_search(event):
    await event.edit("`Sailing the Pirateship!`")
    input_ = event.pattern_match.group(1)
    max_limit = 10
    get_limit = re.compile(r"-l\d*[0-9]")
    query = re.sub(r"-\w*", "", input_).strip()
    r = requests.get("https://torrent-paradise.ml/api/search?q=" + query)
    if get_limit.search(input_) is not None:
        max_limit = int(get_limit.search(input_).group().strip("-l"))
    try:
        torrents = r.json()
        reply_ = ""
        torrents = sorted(torrents, key=lambda i: i["s"], reverse=True)
        for torrent in torrents[: min(max_limit, len(torrents))]:
            if len(reply_) < 4096 and torrent["s"] > 0:
                try:
                    reply_ = (
                        reply_ + f"\n\n<b>{torrent['text']}</b>\n"
                        f"<b>Size ➻ </b> {humanbytes(torrent['len'])}\n"
                        f"<b>Seeders ➻ </b> {torrent['s']}\n"
                        f"<b>Leechers ➻ </b> {torrent['l']}\n"
                        f"<code>magnet:?xt=urn:btih:{torrent['id']}</code>"
                    )
                except Exception:
                    pass
        if reply_ == "":
            await event.edit(f"`Pirates were unsuccesful in finding {query}!`")
        else:
            await event.edit(text=reply_, parse_mode="html")
    except Exception:
        await event.edit("`Pirates are tired!\nAsk them later!`")




CMD_HELP.update(
    {
        "torrent": """**Torrent**

  •  **Syntax : **`.torrent <query>`
  •  **Function : **__Fetches torrent frome https://torrent-paradise.ml/api__

  •  **Syntax : **`.tsearch <query>`
  •  **Syntax : **`.torrent1 <query>`
  •  **Function : **__Fetches torrent links of given <query>__

  •  **Syntax : **`.tmovie ido <query>`
  •  **Function : **__Fetches torrent links of given <query> https://idope.se/search/__
  
  •  **Syntax : **`.tmovie tor <query>`
  •  **Function : **__Fetches torrent links of given <query> https://torrentz2eu.org/searchA__
  
  A Torrent Client Plugin Based On Aria2 for Userbot

cmds: `` Magnet link : .tmagnet magnetLink
	  Torrent file from local: .tor file_path
    Show Downloads: .tshow
	  Remove All Downloads: .tremove ``
	  
"""
    }
)
