import flag
import html
from fridaybot import sclient
from countryinfo import CountryInfo
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location



@modex.on(admin_cmd(pattern="country (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
	    a = country.info()
    except:
	    await event.edit("Country Not Avaiable Currently")
    name = a.get("name")
    bb= a.get("altSpellings")
    hu = ''
    for p in bb:
    	hu += p+",  "
	
    area = a.get("area")
    borders = ""
    hell = a.get("borders")
    for fk in hell:
	    borders += fk+",  "
	
    call = "" 
    WhAt = a.get("callingCodes")
    for what in WhAt:
	    call+= what+"  "
	
    capital = a.get("capital")
    currencies = ""
    fker = a.get("currencies")
    for FKer in fker:
	    currencies += FKer+",  "

    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR= PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
      po = iSo.get(hitler)
      iso += po+",  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)

    languages = a.get("languages")
    lMAO=""
    for lmao in languages:
	    lMAO += lmao+",  "

    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom =""
    for jerry in tik:
	    tom+=jerry+",   "

    GOT = a.get("tld")
    lanester = ""
    for targaryen in GOT:
	    lanester+=targaryen+",   "

    wiki = a.get("wiki")

    caption = f"""<b><u>information gathered successfully</b></u>
<b>
Country Name:- {name}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Country's Flag:- {okie}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
population:- {waste}
Region:- {reg}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}
wikipedia:- {wiki}</b>


<u><b>
Information Gathered By Modified.
Get Yours From {BOT_LIN}.</b></u>
"""
    
    
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )
    
    await event.delete()





CMD_HELP.update(
    {
        "countries": "**Countries**\
\n\n**Syntax : **`.country <country name>`\
\n**Usage :** Gives Information About Given Country.\
\n\n**Example : **`.country india`\
\nThis above syntax gives Information about India"
    }
)
