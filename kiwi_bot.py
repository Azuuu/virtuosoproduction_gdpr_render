import guilded
import json

import bot_config
import data_stores_api
import message_parser

from flask import Flask

app = Flask(__name__)

@app.route('/')
def run():
    client = guilded.Client()

    @client.event
    async def on_ready():
        print(f"{client.user} is listening to Right to Erasure messages")

    """
    Handler for webhook messages from Roblox
    """
    @client.event
    async def on_message(message):
        # Parses and validates message
        user_id, start_place_ids = message_parser.parse_message(message)
        if not user_id or not start_place_ids:
            return

        # Deletes standard data stores user data
        [successes, failures] = data_stores_api.delete_standard_data_stores(user_id, start_place_ids)
        if successes:
            await message.reply(f"Deleted standard data stores data for " +
                               f"user ID: {user_id}, data: {dict(successes)}")
        if failures:
            await message.reply(f"Failed to delete standard data stores data for " +
                               f"user ID: {user_id}, data: {dict(failures)}")

        # Deletes ordered data stores user data
        [successes, failures] = data_stores_api.delete_ordered_data_stores(user_id, start_place_ids)
        if successes:
            await message.reply(f"Deleted ordered data stores data for " +
                               f"user ID: {user_id}, data: {dict(successes)}")
        if failures:
            await message.reply(f"Failed to delete ordered data stores data for " +
                               f"user ID: {user_id}, data: {dict(failures)}")

    client.run(bot_config.GUILDED_BOT_TOKEN)

if __name__ == '__main__':
    app.run()
# if __name__ == "__main__":
#     run()