### Script for test task
#### development of a script for classifying voice messages



### Files structure
* db
  * request.sql
    ###### SQL-script for second half of task
* logs
  * errors.log
    ###### logfile for error-logs
  * messages.log
    ###### logfile for info-logs
* upload
  * files
    ###### directory with task document
  * sounds
    ###### directory with test sounds


### Requirements modules
* tinkoff_voicekit_client
> pip install tinkoff-voicekit-client

* psycopg2
> pip install psycopg2

* pymorphy2
> pip install pymorphy2  
> pip install -U pymorphy2-dicts-ru

* dostoevsky
> pip install dostoevsky  
> python -m dostoevsky download fasttext-social-network-model


### Command for starting script
> python3 main.py -p <PATH> -ph <PHONE>  -d <DB_LOG>  -s <STAGE>


### Arguments
* -p, --path
> description: path to sound-file  
> values:      absolute or relative  
> valid:       required

* -ph, --phone
> description: value for phone value  
> values:      string in format {XXXXXXXXXX}
> valid:       required

* -d, --database
> description: value for checking the need for logging to the database  
> values:      0 or 1  
> valid:       not required

* -s, --stage
> description: value to check the classification step  
> values:      1 or 2  
> valid:       required
