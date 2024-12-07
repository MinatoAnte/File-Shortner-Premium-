from aiohttp import web
from plugins import web_server

from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCESUB_CHANNEL, FORCESUB_CHANNEL2, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.uptime = None
        self.invitelink1 = None
        self.invitelink2 = None
        self.db_channel = None
        self.username = None

    async def get_invite_link(self, channel_id):
        """Helper function to get or create an invite link for a channel."""
        try:
            chat = await self.get_chat(channel_id)
            link = chat.invite_link
            if not link:
                link = await self.export_chat_invite_link(channel_id)
            return link
        except Exception as e:
            self.LOGGER(__name__).warning(f"Failed to get invite link for {channel_id}: {e}")
            raise

    async def start(self):
        await super().start()
        self.uptime = datetime.now()

        # Get bot username
        usr_bot_me = await self.get_me()
        self.username = usr_bot_me.username

        # Force Sub Channels Handling
        if FORCESUB_CHANNEL:
            try:
                self.invitelink1 = await self.get_invite_link(FORCESUB_CHANNEL)
            except Exception as e:
                self.LOGGER(__name__).error(f"Force Sub Channel 1 Error: {e}")
                self.LOGGER(__name__).info("Bot stopped. Please check your settings.")
                sys.exit()

        if FORCESUB_CHANNEL2:
            try:
                self.invitelink2 = await self.get_invite_link(FORCESUB_CHANNEL2)
            except Exception as e:
                self.LOGGER(__name__).error(f"Force Sub Channel 2 Error: {e}")
                self.LOGGER(__name__).info("Bot stopped. Please check your settings.")
                sys.exit()

        # Database Channel Test
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test_message = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test_message.delete()
        except Exception as e:
            self.LOGGER(__name__).error(f"Database Channel Error: {e}")
            self.LOGGER(__name__).info("Bot stopped. Please check your settings.")
            sys.exit()

        # Set parse mode
        self.set_parse_mode(ParseMode.HTML)

        # Log Bot Info
        self.LOGGER(__name__).info(f"Bot @{self.username} is running!")
        self.LOGGER(__name__).info("""
███████╗ █████╗ ██╗   ██╗████████╗██╗ ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██║   ██║╚══██╔══╝██║██╔════╝██║ ██╔╝
███████╗██   ██║██║   ██║   ██║   ██║██║     █████╔╝
╚════██║██╔══██║██║   ██║   ██║   ██║██║     ██╔═██╗
███████║ █████║╚██████╔╝   ██║   ██║╚██████╗██║  ██╗
╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝
        """)

        # Start web server
        try:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", PORT).start()
        except Exception as e:
            self.LOGGER(__name__).error(f"Web Server Error: {e}")
            sys.exit()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
