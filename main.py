from telethon_client import client
from telethon import events


@client.on(events.NewMessage(incoming=True))
async def new_message(event):
    print(event.message)


async def main():
    me = await client.get_me()
    await client.send_message(729407135, 'Ну ти і глюпінька')
#    print(me.stringify())

if __name__ == '__main__':
    print('Starting...')
    client.start()
    client.run_until_disconnected()
    # with client:
    #     client.loop.run_until_complete(main())
