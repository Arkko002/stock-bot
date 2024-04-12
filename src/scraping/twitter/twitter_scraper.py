import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level


async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`
    # TODO:


if __name__ == "__main__":
    asyncio.run(main())
