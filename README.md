# checkIP
This simple script will request it's public IP from the internet and store it locally in a text file. Subsequent executions will compare the current IP with the stored IP. If different, it will send an email notification to the listed recipient.

## Config.ini
Update the included config.ini template file with the sender email address, associated password, and recipient email address. By defualt, script will look for the config.ini file int he c:\ directory.

## Install dependencies
    pip install -r requirements.txt
    
## Usage
    checkIP.py
    
It is suggested to schedule a cron job to run the script, periodically checking for a new IP. 
    0 * * * * python /bin/checkIP.py 
