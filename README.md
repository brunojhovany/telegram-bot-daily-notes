# Telegram bot for daily notes

## Description
This bot is designed to create daily notes. It can be used to create a daily to-do list, a shopping list, or a list of tasks for the day. You can customize the bot to your needs.

## How it works
The bot sends a message to the chat every day at a specified time. The message contains a reminder of daily meet notes.

## Installation
1. Clone the repository
2. Install the requirements
``` bash
pip install -r requirements.txt
```
3. Create a file `.env` and add the following variables:
```
API_TOKEN=your-bot-token
CHAT_ID=your-chat-id
LOG_FILENAME=path-to-log-file

```
4. Run the bot
5. Enjoy!

## run with docker
1. Clone the repository
2. Create a file `.env` and add the following variables:
```
API_TOKEN=your-bot-token
CHAT_ID=your-chat-id
LOG_FILENAME=path-to-log-file

```
3. Build the image
``` bash
docker build -t daily_notes_bot .
```
4. Run the container
``` bash
docker run -v $(pwd)/notes:/notes --env-file=.env daily_notes_bot
```

5. Or do you can config an cron job to run the container every day at a specified time
``` bash
crontab -e

# put add this line to your crontab
0 8 * * * docker run -v $(pwd)/notes:/notes --env-file=.env daily_notes_bot
```

6. Enjoy!

## License
[MIT](https://choosealicense.com/licenses/mit/)
