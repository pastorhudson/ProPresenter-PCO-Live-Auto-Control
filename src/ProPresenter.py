import aiohttp
import asyncio
from utils import get_propresenter_config, setup_logger

import aiohttp

logger = setup_logger(__name__)


async def get_current_index():
    """Retrieve the current index information from the active playlist.

    :param ip: The IP address of the server.
    :param port: The port number of the server.
    :return: The current index information, including index of the current PCO Plan Item starting at 0
    Headers count!, name, and playlist name.

    Example usage:
        ip = "127.0.0.1"
        port = 8080
        result = await get_current_index(ip, port)
        print(result)
    """
    ip, port = get_propresenter_config()
    url = f"http://{ip}:{port}/v1/playlist/active"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                try:
                    date = data['presentation']['playlist']['name'].split('-')[1].strip()
                except Exception as e:
                    date = data['presentation']['playlist']['name']

                status = {
                    "sequence": data['presentation']['item']['index'],
                    "name": data['presentation']['item']['name'],
                    "playlist_name": data['presentation']['playlist']['name'],
                    "date": date
                }

                return status

    except ConnectionRefusedError as e:
        logger.info("Connection Refused Check ProPresenter")
        return None
    except Exception as e:
        return None


if __name__ == "__main__":
    print(asyncio.run(get_current_index()))
