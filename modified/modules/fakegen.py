
 """ **.fakegen :** Automatically generates fake information.➠➠  **.fakeimg** also available..."""
import os
import requests
from faker import Faker
from faker.providers import internet





@borg.on(admin_cmd(pattern=r"fakegen"))
async def hi(event):
    if event.fwd_from:
        return
    fake = Faker()
    print("GENERATED Fake ID\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.edit(
        f"<b><u>Information Generated🔖</b></u>\n<b>👤 Name ⪼⪼  </b><code>{name}</code>\n\n<b>🏰 Address ⪼⪼  </b><code>{address}</code>\n\n<b>🛰 IP ADDRESS ⪼⪼  </b><code>{ip}</code>\n\n<b>💳 credit card ⪼⪼  </b><code>{cc}</code>\n\n<b>📧 Email Id ⪼⪼  </b><code>{email}</code>\n\n<b>🏢 Job ⪼⪼  </b><code>{job}</code>\n\n<b>📱 android user agent ⪼⪼  </b><code>{android}</code>\n\n<b>💻 Pc user agent ⪼⪼  </b><code>{pc}</code>",
        parse_mode="HTML",
    )


@borg.on(admin_cmd(pattern="fakeimg"))
@borg.on(sudo_cmd(pattern="fakeimg", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("Creating fake Picture...")
    if response.status_code == 200:
      with open("imagesss.jpg", 'wb') as f:
        f.write(response.content)
    
    captin = f"Image Gernerated 📸."
    fole = "imagesss.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    if not os.path.isdir(Config.TRASH_DOWNLOAD_DIRECTORY):
  os.makedirs(Config.TRASH_DOWNLOAD_DIRECTORY)
    os.system("rm ./trash/imagesss.jpg")



CMD_HELP.update(
    {
        "fakegen": "**Fake information Generator**\
\n\n**Syntax : **`.fakegen`\
\n**Usage :** Automatically generates fake information.➠➠ .fakeimg also available..."
    }
)


CMD_HELP.update(
    {
        "fakeimg": "**Fake Picture**\
\n\n**Syntax : **`.fakeimg`\
\n**Usage :** Genetates Fake Image.\
\n\n**Note : **The Person In Picture Really Doesn't Exist."
    }
)
