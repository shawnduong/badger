#!/bin/bash
# You must have all the dependencies installed or have activated a venv with the
# dependencies installed before running this script.

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

workdir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

# Services.
${workdir}/services/admin/main.py &
${workdir}/services/manage/main.py &
${workdir}/services/public/main.py &
${workdir}/services/scanner/main.py &
${workdir}/services/user/main.py &

# Primary platform.
${workdir}/main/main.py
