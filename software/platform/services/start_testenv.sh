#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

echo "WARNING: THIS WILL DELETE ANY EXISTING INSTANCES AND THEIR DATA."
read -p "Press ENTER to acknowledge and proceed." </dev/tty

rm -rf */instance/

source admin/env/bin/activate
./admin/main.py &

source manage/env/bin/activate
./manage/main.py &

source public/env/bin/activate
./public/main.py
