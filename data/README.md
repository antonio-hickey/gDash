# Automating the data collection for gDash

Unix machines can use crontab jobs:
    - First open a terminal and use the following command:
        - `crontab -e`
    - Now that we are in crontab we need to create the jobs:
        - ```
            #--------------
            # gDash Jobs
            #--------------
            0 * * * * /usr/bin/env python3 /YOURFILEPATH/gDash/data/events/micro_miner.py
            1 * * * * /usr/bin/env python3 /YOURFILEPATH/gDash/data/events/handler.py
            #--------------
          ```
    - Our data will now be collected and updated every hour

Windows machines can use task scheduler:
    - [Tutorial](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
