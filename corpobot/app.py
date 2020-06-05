import aioconsole
import asyncio
from corpobot.logger import logger


class Application:
    def __init__(self):
        self.running = False

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run())
        loop.close()

    async def _run(self):
        self.running = True
        while self.running:
            _input = await aioconsole.ainput(prompt="Type command or `help` for list commands\n")

            await self.process_input(_input)
            await asyncio.sleep(0)

    async def process_input(self, _input):
        if _input == "help":
            await print_help()
        elif _input == "quit":
            self.running = False
        else:
            print(f"There is no command with name: {_input}")
            await print_help()

    async def stop(self):
        self.running = False
        await asyncio.sleep(0)


async def print_help():
    logger.info(f"Following commands are available: get_tasks")