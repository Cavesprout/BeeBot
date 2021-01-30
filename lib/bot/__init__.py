from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from datetime import datetime

PREFIX = "~"
OWNER_IDS = [482592062546378753]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS, 
            intents=Intents.all(),
        )

    def run(self, version, version_message):
        self.VERSION = version
        self.VERSION_MESSAGE = version_message

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            print("bot ready")
            self.ready = True

            channel = self.get_channel(805177594441629746)

            embed = Embed(title="Drone Dispatched", description="BeeBot is now online!")
            fields =    [("Version", f"{self.VERSION}", True),
                        ("Update:", f"{self.VERSION_MESSAGE}", True)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_footer(text=f"{datetime.utcnow()}")
            await channel.send(embed=embed)

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot = Bot()