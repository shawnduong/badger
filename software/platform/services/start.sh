#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

source env/bin/activate

./admin/main.py &
./manage/main.py &
./public/main.py &
./user/main.py
