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

                if data['presentation']['item']['index'] != 4294967295:
                    sequence = data['presentation']['item']['index']

                else:

                    sequence = await get_index_by_name(data['presentation']['item']['name'], data['presentation']['playlist']['index'])

                status = {
                    "sequence": sequence,
                    "name": data['presentation']['item']['name'],
                    "playlist_name": data['presentation']['playlist']['name'],
                    "playlist_index": data['presentation']['playlist']['index'],
                    "date": date
                }
        return status

    except ConnectionRefusedError as e:
        logger.info("Connection Refused Check ProPresenter")
        return None
    except Exception as e:
        return None


async def get_index_by_name(name, index):
    ip, port = get_propresenter_config()
    url = f"http://{ip}:{port}/v1/playlist/{index}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                items = data['items']
                for item in items:
                    if item['id']['name'] == name and item['is_pco']:
                        return item['id']['index']

        return None

    except ConnectionRefusedError as e:
        logger.info("Connection Refused Check ProPresenter")
        return None
    except Exception as e:
        return None


# if __name__ == "__main__":
#     while True:
        # print(asyncio.run(get_index_by_name("EagleEye in the sky", '4')))
        # print(asyncio.run(get_current_index()))
