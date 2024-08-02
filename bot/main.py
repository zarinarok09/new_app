import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import aiohttp

API_TOKEN = '<Your_Telegram_API_Token>'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

BASE_URL = "http://web:8000/api/v1"

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm MessageBot!\nUse /messages to see all messages or /new to create a new one.")

@dp.message_handler(commands=['messages'])
async def get_messages(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/messages/") as response:
            if response.status == 200:
                messages = await response.json()
                if messages:
                    await message.reply("\n".join([f"{m['author']}: {m['content']}" for m in messages]))
                else:
                    await message.reply("No messages found.")
            else:
                await message.reply("Failed to retrieve messages.")

@dp.message_handler(commands=['new'])
async def new_message(message: types.Message):
    await message.reply("Please send your message in the format: /msg <author> <content>")

@dp.message_handler(commands=['msg'])
async def create_message(message: types.Message):
    try:
        _, author, content = message.text.split(" ", 2)
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{BASE_URL}/message/", json={"id": str(message.message_id), "author": author, "content": content}) as response:
                if response.status == 200:
                    await message.reply("Message created successfully!")
                else:
                    await message.reply("Failed to create message.")
    except ValueError:
        await message.reply("Invalid format. Use /msg <author> <content>")

if name == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)