# Covid-19 Data Collection
### Collecting data from Our World In Data [Our World In Data](https://ourworldindata.org/)

To automate running the python script to collect data daily:

	- UNIX:
		- Crontab Job every day at 4:30pm
			- Open a terminal
			- `crontab -e`
			- `30 16 * * * /usr/bin/env python3 /YOUR PATH/gDash/data/covid/covid_miner.py`
			- `ctrl + x`
			
	- Windows:
		- https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10

