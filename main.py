import asyncio
import logging

from app.bot import dispatcher, bot


async def main():
    logging.basicConfig(level=logging.INFO)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
