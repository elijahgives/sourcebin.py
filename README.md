# Sourcebin.py
Sourcebin.py is a simple Python API wrapper for https://sourceb.in/.


# Installation
```
pip install sourcebin
```

# Examples

### Creating a paste
```py
import asyncio
import sourcebin

async def main():
    code = "console.log('Hello World')"
    paste = await sourcebin.create(
        name="example.js", 
        code=code, 
        title="Example Paste"
    )
    print(paste)  # https://sourceb.in/ooPp0TSrpv

asyncio.run(main())
```
