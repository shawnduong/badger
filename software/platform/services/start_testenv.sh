#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

echo "WARNING: THIS WILL DELETE ANY EXISTING INSTANCES AND THEIR DATA."
read -p "Press ENTER to acknowledge and proceed." </dev/tty

rm -rf */instance/

source admin/env/bin/activate
python3 admin/main.py &

source public/env/bin/activate
python3 public/main.py
