import simplematrixbotlib as botlib
import nio
import os
import aiofiles
import aiofiles.os
from config import PREFIX, RESPONSES_FOLDER, creds

# Matrix Config
config = botlib.Config()
config.ignore_unverified_devices = True

# creds = botlib.Creds(HOMESERVER, USERNAME, PASSWORD, session_stored_file="session.txt")
bot = botlib.Bot(creds, config)

@bot.listener.on_message_event
async def message_event_handler(room: nio.rooms.MatrixRoom, message: nio.events.room_events.RoomMessageText):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    # ignore own messages
    if not match.is_not_from_this_bot():
        return

    # check for prefix
    if not match.prefix():
        return

    print(f'Message in {room.display_name} from {message.sender}: {message.body}')

    # check for messing with prefix without specifying message
    if not len(match.args()):
        return
    
    # Function logic
    resp_id = match.args()[0]
    available_responses = await aiofiles.os.listdir(RESPONSES_FOLDER)

    # Alias support
    if f'{resp_id}.alias' in available_responses:
        async with aiofiles.open(os.path.join(RESPONSES_FOLDER, f'{resp_id}.alias')) as alias_file:
            resp_id = (await alias_file.read()).strip()

    # handle actual responses
    if f'{resp_id}.md' in available_responses:
        async with aiofiles.open(os.path.join(RESPONSES_FOLDER, f'{resp_id}.md')) as response_file:
            response = await response_file.read()
        response = response.format(*match.args()[1:])
        await bot.api.send_markdown_message(room.room_id, response)

    # Images
    if f'{resp_id}.jpg' in available_responses:
        await bot.api.send_image_message(room.room_id, os.path.join(RESPONSES_FOLDER, f'{resp_id}.jpg'))

print('Starting bot...')
bot.run()