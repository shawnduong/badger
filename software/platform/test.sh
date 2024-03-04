#!/bin/bash
# You must have all the dependencies installed or have created a venv with the
# dependencies installed before running this script.

echo "WARNING: THIS WILL DELETE ANY EXISTING INSTANCES AND THEIR DATA."
read -p "Press ENTER to acknowledge and proceed." </dev/tty

workdir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

pkill -f ${workdir}/services/admin/main.py
pkill -f ${workdir}/services/manage/main.py
pkill -f ${workdir}/services/public/main.py
pkill -f ${workdir}/services/user/main.py
pkill -f ${workdir}/main/main.py

tmux new-session \; \
	split-window -v \; \
	attach \; \
	select-pane -t 0 \; \
	send-keys -t 0 \
		"
		clear
		trap 'trap - SIGTERM && kill -- -$$' SIGINT SIGTERM EXIT
		source ${workdir}/env/bin/activate
		rm -f ${workdir}/services/*/instance/*.sqlite
		rm -f ${workdir}/services/*/*.sqlite
		rm -f ${workdir}/main/instance/*.sqlite
		rm -f ${workdir}/main/*.sqlite
		${workdir}/services/admin/main.py &
		${workdir}/services/manage/main.py &
		${workdir}/services/public/main.py &
		${workdir}/services/user/main.py &
		${workdir}/main/main.py &
		" \; \
	send-keys -t 1 \
		"
		clear
		source ${workdir}/env/bin/activate
		sleep 1
		pytest
		";

