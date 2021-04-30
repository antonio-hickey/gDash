# Current Event's Data Collection & Handling

### Automation:
- UNIX:
	- Crontab Job every 1 hour
		- Open a terminal
		- `crontab -e`
		- `0 * * * * /usr/bin/env python3 /YOUR PATH/gDash/data/events/usEvents_Miner.py`
		- `ctrl + x`
- WINDOWS:
	- Task Scheduler
		- https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10
