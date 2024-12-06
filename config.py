#Recoded by @kakashi_13

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7898892707:AAF14P4XRyK0_Uo7WtTpFtIa3lAjV6ymU-0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20561711"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be67fa66bf79d732d799ed8fc7d54a16")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002453573874"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2052951004"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://pavanmanikanta72:aXPjJxiago4Rv3rb@cluster0.clwpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001800300325"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001800300325"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/510affa3d4b6c911c12e3.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/3b64224e127e8385f8c70-0e8d3b05d75da9ddb1.jpg")

#text
HELP_TXT = "<b>Hi Dude!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to open Link - <a href=https://t.me/AC_Linkzz/64>Clickhere</a></b>"
ABOUT_TXT = "<b><i>About Us..\n\n‣ Made for : @Ac_Linkzz\n‣ Owned by : @Kakashi_13\n‣ Maintained by : @Jakie_Spider_143\n‣ Developed by : @Obito_Uchiha_131\n\n Adios !!</i></b>"
SHORT_MSG = "👇 Click On Download Button"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href=https://t.me/AC_Linkzz>Team Ac Linkzz</a></b>")
try:
    ADMINS=[2052951004]
    for x in (os.environ.get("ADMINS", "2052951004").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "shortxlinks.com")
SHORT_API = os.environ.get("SHORTNER_API", "dac01a108e99f1d6b9502eec18705ce2c37da9eb")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>❗️️❗️❗️ɪᴍᴘᴏʀᴛᴀɴᴛ❗️️❗️❗️

ᴛʜᴇꜱᴇ ᴠɪᴅᴇᴏꜱ / ꜰɪʟᴇꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ 1 ᴍɪɴᴜᴛᴇꜱ (ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ).

📌 ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇꜱᴇ ᴠɪᴅᴇᴏꜱ / ꜰɪʟᴇꜱ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ.</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

LOG_FILE_NAME = "filesharingbot.txt"

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

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
