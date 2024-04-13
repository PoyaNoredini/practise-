from decouple import config 
from pyrogram import Client , filters
from pyrogram.types import Message  

app = Client(
    name=config("app_name"),
    api_id=config("api_id", cast=int),
    api_hash=config("api_hash"),
    bot_token=config("bot_token"),
)

@app.on_message(filters.private & (filters.text | filters.photo ))
def main(client: Client , messsage):
    #print(messsage)
   # if messsage.chat.id  == 557488233:
    #    client.send_message("ha ha ha")
    messsage.reply("salam azizam")


app.run()