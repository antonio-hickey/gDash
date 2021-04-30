# Automating the data collection for gDash

Unix machines can use crontab jobs:
    - First open a terminal and use the following command:
   
        - `crontab -e`
   
   - Now that we are in crontab we need to create the jobs:
  
        - The data miner runs every hour and the data handler runs every hour and 1 minute 
        
        - ```
            #--------------
            # gDash Jobs
            #--------------
            0 * * * * /usr/bin/env python3 /YOURFILEPATH/gDash/data/events/micro_miner.py
            1 * * * * /usr/bin/env python3 /YOURFILEPATH/gDash/data/events/handler.py
            #--------------
          ```

Windows machines can use task scheduler:

    [Tutorial](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
