from time import time
from os import remove

from uvloop import install

install()
from pyrogram import Client

nameofclient = str(time()))
pbot = Client(
    nameofclient,
    api_id=int(input("Enter an API ID: ")),
    api_hash=input("Enter an API HASH: "),
    no_updates=True,
)
pbot.start()
print(pbot.export_session_string())
pbot.stop(True)
remove(f"{nameofclient}.session-journal")
remove(f"{nameofclient}.session")
