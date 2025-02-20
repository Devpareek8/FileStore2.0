# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8013104178:AAEvKsqk6JRKtKdp91xZMLKimzqwRByfXws")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24942826"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e3e2f3b65ef58634139ccd27d6b7d8cb")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002191230586"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Morning006")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6914788581"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mrnoffice692:PsO4VGHI9heKd7WA@cluster0.o1vcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "3000"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002469127707"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Morning006 \n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Morning006>Dev</a></blockquote></b>"


ABOUT_TXT = """<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
 
 🤖 ᴍʏ ɴᴀᴍᴇ : {}
 👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/Morning006'>Ⱡʉ₵ł₣ɇɽ 🇮🇳</a>
 📚 ʟɪʙʀᴀʀʏ : Who Care 
 📝 ʟᴀɴɢᴜᴀɢᴇ : Hindi
 ♻️ ᴅᴀᴛᴀ ʙᴀsᴇ : Free wala
 📡 ʜᴏsᴛᴇᴅ ᴏɴ  : My PC
 🥶 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : Offline</b>"""


START_MSG = os.environ.get("START_MESSAGE", """<b>ʜᴇʏ {}, ᴍʏ ɴᴀᴍᴇ {} ☺️\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ  ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs  !! 😍\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Morning006">Dev</a> </blockquote></b>")

try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6914788581").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, "False"
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @OtakuFlix_Network</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6914788581)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
