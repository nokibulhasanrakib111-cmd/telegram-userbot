from telethon import TelegramClient, events

api_id = 38624628
api_hash = "92f2ad77b5e55c282bd82d5a252a8714"

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply(
            "Assalamu Alaikum 🙏\nআমি এখন অফলাইনে আছি। পরে রিপ্লাই দিব।"
        )

client.start()
print("Userbot Running...")
client.run_until_disconnected()
