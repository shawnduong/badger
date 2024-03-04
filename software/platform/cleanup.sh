#!/bin/bash
# Clean up the processes generated from the test script.

workdir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

pkill -f ${workdir}/services/admin/main.py
pkill -f ${workdir}/services/manage/main.py
pkill -f ${workdir}/services/public/main.py
pkill -f ${workdir}/services/user/main.py
pkill -f ${workdir}/main/main.py
