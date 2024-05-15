import aiohttp
import re


def get_url(key: str):
    return f"https://sourceb.in/{key}"


def get_key(url):
    a = re.findall('https?://(sourceb\.in|srcb\.in)\/(.+)', url)
    return a[0][1]


async def create(name: str, code: str, title="None", description="None"):
    async with aiohttp.ClientSession() as session:
        res = await session.post(
            "https://sourceb.in/api/bins/",
            json={
                'title': title,
                'description': description,
                'files': [
                    {
                        "name": name,
                        "content": code
                    }
                ],
            })
        data = await res.json()
        return get_url(data['key'])


async def read_key(key: str):
    async with aiohttp.ClientSession() as session:
        main = await session.get(f"https://sourceb.in/api/bins/{key}", headers={ "ACCEPT": 'application/json'})
        if not main.ok:
            raise NameError("key must be a key to an existing sourcebin")
        else:
            answer: list[str] = []
            main_data = await main.json()
            size: int = len(main_data['files'])
            for i in range(size):
                res = await session.get(f"https://cdn.sourceb.in/bins/{key}/{i}")
                answer.append((await res.text()))
            return {
                'code': answer,
                'fileCount': size,
                'createdAt': main_data['created'],
                'key': main_data['key']
            }


async def read_url(url: str):
    key = get_key(url)
    async with aiohttp.ClientSession() as session:
        main = await session.get(f"https://sourceb.in/api/bins/{key}", headers={ "ACCEPT": 'application/json'})
        if not main.ok:
            raise NameError("key must be a key to an existing sourcebin")
        else:
            answer: list[str] = []
            main_data = await main.json()
            size: int = len(main_data['files'])
            for i in range(size):
                res = await session.get(f"https://cdn.sourceb.in/bins/{key}/{i}")
                answer.append((await res.text()))
            return {
              'code': answer,
              'fileCount': size,
              'createdAt': main_data['created'],
              'key': main_data['key']
              }
