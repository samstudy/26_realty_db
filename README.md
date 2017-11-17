# Real Estate Site


### According a scenario we are helped the company migrate from excell db to DBMS


### The tasks what have been done
  - Connect to DBMS
  - Prepare the script for migrate from JSON to DB,expired advertisement should be deleted,but must be hidded
  - Include functionality such filter by price,by new building,location
  - Pagination


### The steps how to use:
- Create a sample json file
- Create DB
- Insert into DB information from sample file
- Push the server


### Deploy on localhost

Example of frontend launch on Linux, Python 3.5:

```bash

python3 create_sample_json.py
python3 create_db.py
python3 insert_into_db.py
python3 server.py

```

Open page [localhost:5000](http://localhost:5000) in browser.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)