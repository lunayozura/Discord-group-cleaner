import asyncio
import random
import time
from typing import Union
import discord
client = discord.Client(self_bot=True)
token = input("Token : ")
group_id: Union[int, str] = input("Group ID: ")
@client.event
async def on_ready():
    print(f"Logged in as '{client.user}'")
    try:
        counter = 0
        print(f"Fetching group with ID '{group_id}'")
        await asyncio.sleep(random.uniform(0.4, 0.6))
        group_channel = await client.fetch_channel(group_id)
        if not isinstance(group_channel, discord.GroupChannel):
            raise Exception(f"Channel with ID '{group_id}' is not a group channel")
        print("Starting message deletion")
        async for msg in group_channel.history(limit=None):
            if msg.author.id == client.user.id:
                try:
                    await msg.delete()
                    counter += 1
                    print(f"Deleted message {counter}")
                    await asyncio.sleep(random.uniform(0.6, 0.9))
                    if counter % 10 == 0:
                        print("Pausing for 10 seconds...")
                        await asyncio.sleep(10)
                except discord.Forbidden as e:
                    print(f"Skipping message due to error: {e}")
        print(f"Finished deleting {counter} messages.")
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(50)
        exit()
    finally:
        print("Finished deleting all messages! The script will close in 10s")
        await asyncio.sleep(10)
        exit
if __name__ == '__main__':
    try:
        client.run(token)
    except discord.errors.LoginFailure:
        print("Login failure: improper token")
        time.sleep(50)
        exit()
