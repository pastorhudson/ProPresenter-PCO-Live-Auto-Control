import aiohttp
import asyncio


async def get_current_index(ip, port):
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
    url = f"http://{ip}:{port}/v1/playlist/active"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            status = {
                "index": data['presentation']['item']['index'],
                "name": data['presentation']['item']['name'],
                "playlist_name": data['presentation']['playlist']['name']
            }
            return status


if __name__ == "__main__":
    print(asyncio.run(get_current_index('192.168.1.140', 1025)))
