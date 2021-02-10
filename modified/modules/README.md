## Mandatory Imports
```python3
None
```
There is None Mandatory Imports. Because Config, bot and command are already automatically imported.

## Explanation
The Mandatory Imports are now automatically imported.

### Formation
Now I will show a short script to show the formation of the desired script.
```python3

@modbot.on(modified_cmd(pattern="hello"))
@modbot.on(sudo_cmd(pattern="hello", outgoing=True))
async def hello_world(event):
    if event.fwd_from:
        return
    await edit_or_reply(event , "**HELLO WORLD**\n\nThe following is controlling me too!\n" + Config.HELLO_PIC)
```
