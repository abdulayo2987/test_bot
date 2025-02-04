import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

def get_response(user_inputs: str)-> str:
    lowered: str = user_inputs.lower()
    if lowered == '':
        return 'Well your quiet'
    elif 'hello' in lowered:
        return 'Hello there'
    else:
        return 'message'

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('message empty')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: Message) -> None:
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    if message.author == client.user:
        return
    await send_message(message, user_message)

def main() -> None:
    client.run(str(TOKEN))

if __name__ == '__main__':
    main()

