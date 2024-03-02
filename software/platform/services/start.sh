#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

source admin/env/bin/activate
python3 admin/main.py &

source manage/env/bin/activate
python3 manage/main.py &

source public/env/bin/activate
python3 public/main.py
