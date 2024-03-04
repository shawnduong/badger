#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

echo "WARNING: THIS WILL DELETE ANY EXISTING INSTANCES AND THEIR DATA."
read -p "Press ENTER to acknowledge and proceed." </dev/tty

rm -rf */instance/

source ../env/bin/activate

./admin/main.py &
./manage/main.py &
./public/main.py &
./user/main.py
