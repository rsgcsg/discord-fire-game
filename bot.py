import os
import discord
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot 已登录为 {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('!ping'):
        await message.channel.send('Pong!')

keep_alive()  # 启动防止Render休眠的HTTP服务
client.run(TOKEN)