#!/bin/bash
# Start the primary process and put it in the background
set -m

# Start the primary process and put it in the background
python app.py &
BOT_PID=$!

# Start the helper process
./pkiller $BOT_PID

# the helper process might need to know how to wait on the
# primary process to start before it does its work and returns


# now we bring the primary process back into the foreground
# and leave it there
# fg %1