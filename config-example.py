import simplematrixbotlib as botlib

# Application options
PREFIX = ';prefix' # can be any valid string
RESPONSES_FOLDER = './responses/' # application needs read access

# Login Info
HOMESERVER = 'https://matrix.org'
USERNAME = 'exampleuser'
PASSWORD = 'password'

creds = botlib.Creds(HOMESERVER, USERNAME, PASSWORD, session_stored_file="session.txt")
