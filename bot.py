import revolt
import asyncio
import random

# Токен бота
TOKEN = "TiWavYJ8IujxxOjJyDLtM1Oj17sH-FatgTpaF_plwBoX6MBrDP1SOh0fBBKvPWcu"

# Фразы для ответа
PHRASES = [
    "рудик абасрался",
    "белла пердулькинс",
    "фэээня 57 57",
    "юся какулькинс"
]

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        # Игнорируем сообщения от самого бота
        if message.author.bot:

            return

        # С вероятностью 34% отвечаем случайной фразой
        if random.random() < 0.34:
            response = random.choice(PHRASES)
            await message.channel.send(response)

async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, TOKEN)
        await client.start()

asyncio.run(main())
