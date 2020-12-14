# ETL-Project


This is a self serve automated form filler for my rock climbing gym Earth Treks. It allows a user to schedule and automated booking that executes right when they become available. (Reservation slots fill up too fast when they become available and I can never get a spot in time.)

I used lxml to scrape the required xpaths to inform selenium automation how to perform actions and navigate the page. The paths are then stored into pandas dataframes and are reference-able by name of the element they correspond to. E.G. "booking_time_path" = '//*[@id="offering-page-select-events-table"]/tbody/tr[2]/td[4]/a'


The user fills text fields and dropdowns  to enter their booking information and desired booking time. Then, the input data is used to index the pandas data frames and return the xpaths


This whole process is self contained in the Jupyter Notebook file as a POC (Careful executing is will  book a reservation at the gym if one is available during the selected time)

To implement so that it’s usable in real like I made an HTML/CSS form page and am working on a JS script to push the user inputed values as JSON. I’m either going to store the JSON files on an S3 or write them into AWS dynamodb

Then, the python is broken up into 2 scripts. One that handles translating the user inputs into the require xpaths needed to inform the automation (extrapolate.py) and one to execute the automation itself (treksbot.py)

The site will be hosted on AWS and as inputs come in it will schedules crons to execute the python scripts using AWS Lambda. The reservations are made available 2 days in advance at 11am everyday. The crons will be scheduled to reflect that
