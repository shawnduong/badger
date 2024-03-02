#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

source admin/env/bin/activate
./admin/main.py &

source manage/env/bin/activate
./manage/main.py &

source public/env/bin/activate
./public/main.py
