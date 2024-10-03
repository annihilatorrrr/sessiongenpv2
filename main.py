from time import time

from uvloop import install

install()
from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

arg = input("Enter p for PyroV2 or t for Tele: ")

if arg == "p":
    nameofclient = str(time())
    pbot = Client(
        nameofclient,
        api_id=int(input("Enter an API ID: ")),
        api_hash=input("Enter an API HASH: "),
        no_updates=True,
        in_memory=True,
    )
    pbot.start()
    print(pbot.export_session_string())
    pbot.stop(True)
elif arg == "t":
    client = TelegramClient(StringSession(), int(input("Enter an API ID: ")), input("Enter an API HASH: "))
    client.start()
    print(client.session.save())
else:
    print("Start Again!\nInvalid Option.")
print("Bye!")
