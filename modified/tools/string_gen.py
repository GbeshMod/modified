# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.
#removed  This👉line if you are using terminal interface import os
#os.system('pip install telethon')👈


import os
os.system('pip install telethon')
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
ok = """ __  __  __  ___  __  ___  __  ___  ___    
(  \/  )/  \(   \(  )(  _)(  )(  _)(   \   
 )    (( () )) ) ))(  ) _) )(  ) _) ) ) )  
(_/\/\_)\__/(___/(__)(_)  (__)(___)(___/

"""
print(ok)
print("An online StringSession generator Made With ReplRun")
print("Telethon UserBot🤖")
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
	try:
		session = client.session.save()
		client.send_message("me",
		                    f"☣️String Session☣️\nTap To Copy. \n`{session}`")
		print("☣String Generated Sucessfully Check Your Saved Message.☣")
	except Exception as sed:
		print(f"Something Went Wrong While Generating String \nError : {sed}")
