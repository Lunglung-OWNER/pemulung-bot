import asyncio

from . import catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="me$",
    command=("me", plugin_category),
    info={
        "header": "animation lunglung",
        "usage": "{tr}me",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1.5
    animation_ttl = range(14)
    event = await edit_or_reply(event, "me")
    animation_chars = [
        "Processing . . .",
        "Processing . . ",
        "Processing .",
        "l",
        "lu",
        "lun",
        "lung",
        "lungl",
        "lunglu",
        "lunglun",
        "lunglung",
        "😈",
        "**LUNGLUNG NI BOSHHH**",
        "😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 14])
        await asyncio.sleep(animation_interval)