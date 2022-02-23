import asyncio

from monitoring import append_measurement
from ping import ping_servers, pretty_output
from settings import settings


async def main_loop():
    while True:
        results = await ping_servers(settings.SERVERS)
        await append_measurement(results)
        print(pretty_output(results))
        await asyncio.sleep(5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())
    loop.run_forever()
