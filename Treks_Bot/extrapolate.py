import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from lxml import html
import requests

    #this file derives the xpaths from the input data

#sample input data

booking_input = {

      'first_name': 'Daniel',
      'last_name': 'Ford',
      'phone_number': '303-264-8871',
      'email':'dannyford11@me.com',
      'bday_month': 'Apr',   #last 6 inputs require looking up urls or xpaths
      'bday_day': '18',
      'bday_year': '1990',
      'gym': 'Rino',
      'booking_time': "8 AM to 9:50 AM",
      'day_selection': "20",

    }

def main():

        #Creates Dataframe with gym urls
        gyms = ['Rino', 'Baker', 'Englewood']
        gym_paths = ['https://app.rockgympro.com/b/widget/?a=offering&offering_guid=d9a768a045814f56a9fa79de9af419bf&random=5fce726e16a35&iframeid=&mode=p','https://app.rockgympro.com/b/widget/?a=offering&offering_guid=f730839bccf84809803c7dc955064c3d&random=5fce73321cfec&iframeid=&mode=p','https://app.rockgympro.com/b/widget/?a=offering&offering_guid=0077362cf5a04cfc9150386cfc7e6c03&random=5fce7342e5974&iframeid=&mode=p']
        gym_options = {"gyms": gyms, "gym_paths": gym_paths}
        gym_options = pd.DataFrame(gym_options)
        gym_options = gym_options.set_index("gyms")
        gym_options = gym_options.T


        #Generates variables from the input
        gym_url = gym_options[booking_input['gym']][0]
        first_name = booking_input["first_name"]
        last_name = booking_input["last_name"]
        phone_number = booking_input["phone_number"]
        email = booking_input["email"]




        #sets up scraper to pull calendar xpaths

        try:

            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(gym_url)
            time.sleep(3)
            page = driver.page_source
            tree = html.fromstring(page)
            driver.quit()
        except:
            print("the scraper failed to initiate")


        #scrapes selected gym's calendar for days and cooresponding xpaths


        xpaths = []
        days = []

        for i in range(5):
            for j in range(7):
                text_xpath = f'//*[@id="start_date_calendar"]/div/table/tbody/tr[{i+1}]/td[{j+1}]/a'
                button_xpath = f'//*[@id="start_date_calendar"]/div/table/tbody/tr[{i+1}]/td[{j+1}]'
                xpaths.append(button_xpath)
                day = tree.xpath(text_xpath)

                try:
                    days.append(day[0].text)
                except:
                    days.append('none')


        #creates dataframe of calendar days and xpaths

        calendar_xpaths = {"days":days, "xpaths":xpaths}
        calendar_xpaths = pd.DataFrame(calendar_xpaths)
        calendar_xpaths = calendar_xpaths.set_index("days")
        calendar_xpaths = calendar_xpaths.T




        #creates dataframe of booking times and xpaths
        times = ["6 AM to 7:50 AM", "8 AM to 9:50 AM", "10 AM to 11:50 AM", "12 PM to 1:50 PM", "2 PM to 3:50 PM", "4 PM to 5:50 PM", "6 PM to 7:50 PM", "8 PM to 10 PM"]
        time_paths = ['//*[@id="offering-page-select-events-table"]/tbody/tr[1]/td[4]/a', '//*[@id="offering-page-select-events-table"]/tbody/tr[2]/td[4]/a', '//*[@id="offering-page-select-events-table"]/tbody/tr[3]/td[4]/a','//*[@id="offering-page-select-events-table"]/tbody/tr[4]/td[4]/a','//*[@id="offering-page-select-events-table"]/tbody/tr[5]/td[4]/a','//*[@id="offering-page-select-events-table"]/tbody/tr[6]/td[4]/a','//*[@id="offering-page-select-events-table"]/tbody/tr[7]/td[4]/a','//*[@id="offering-page-select-events-table"]/tbody/tr[8]/td[4]/a']
        booking_time = {"times": times, "time_paths": time_paths}
        booking_time = pd.DataFrame(booking_time)
        booking_time = booking_time.set_index("times")
        booking_time = booking_time.T


        #creates dataframe of birth month xpaths
        birth_month_paths = ['//*[@id="participant-birth-pindex-1month"]/option[2]', '//*[@id="participant-birth-pindex-1month"]/option[3]', '//*[@id="participant-birth-pindex-1month"]/option[4]', '//*[@id="participant-birth-pindex-1month"]/option[5]', '//*[@id="participant-birth-pindex-1month"]/option[6]','//*[@id="participant-birth-pindex-1month"]/option[7]','//*[@id="participant-birth-pindex-1month"]/option[8]', '//*[@id="participant-birth-pindex-1month"]/option[9]', '//*[@id="participant-birth-pindex-1month"]/option[10]', '//*[@id="participant-birth-pindex-1month"]/option[11]', '//*[@id="participant-birth-pindex-1month"]/option[12]','//*[@id="participant-birth-pindex-1month"]/option[13]']
        birth_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        bmonth_options = {"bmonths": birth_months, "bmonth_paths": birth_month_paths}
        bmonth_options = pd.DataFrame(bmonth_options)
        bmonth_options = bmonth_options.set_index("bmonths")
        bmonth_options = bmonth_options.T



        #creates dataframe of birth day day xpaths
        birthday_path = ['//*[@id="participant-birth-pindex-1day"]/option[2]','//*[@id="participant-birth-pindex-1day"]/option[3]','//*[@id="participant-birth-pindex-1day"]/option[4]','//*[@id="participant-birth-pindex-1day"]/option[5]','//*[@id="participant-birth-pindex-1day"]/option[6]','//*[@id="participant-birth-pindex-1day"]/option[7]','//*[@id="participant-birth-pindex-1day"]/option[8]','//*[@id="participant-birth-pindex-1day"]/option[9]','//*[@id="participant-birth-pindex-1day"]/option[10]','//*[@id="participant-birth-pindex-1day"]/option[11]','//*[@id="participant-birth-pindex-1day"]/option[12]','//*[@id="participant-birth-pindex-1day"]/option[13]','//*[@id="participant-birth-pindex-1day"]/option[14]','//*[@id="participant-birth-pindex-1day"]/option[15]','//*[@id="participant-birth-pindex-1day"]/option[16]','//*[@id="participant-birth-pindex-1day"]/option[17]','//*[@id="participant-birth-pindex-1day"]/option[18]','//*[@id="participant-birth-pindex-1day"]/option[19]','//*[@id="participant-birth-pindex-1day"]/option[20]','//*[@id="participant-birth-pindex-1day"]/option[21]','//*[@id="participant-birth-pindex-1day"]/option[22]','//*[@id="participant-birth-pindex-1day"]/option[23]','//*[@id="participant-birth-pindex-1day"]/option[24]','//*[@id="participant-birth-pindex-1day"]/option[25]','//*[@id="participant-birth-pindex-1day"]/option[26]','//*[@id="participant-birth-pindex-1day"]/option[27]','//*[@id="participant-birth-pindex-1day"]/option[28]','//*[@id="participant-birth-pindex-1day"]/option[29]','//*[@id="participant-birth-pindex-1day"]/option[30]','//*[@id="participant-birth-pindex-1day"]/option[31]','//*[@id="participant-birth-pindex-1day"]/option[32]']
        b_days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        bday_options = {"days": b_days, "bday_paths": birthday_path}
        bday_options = pd.DataFrame(bday_options)
        bday_options = bday_options.set_index("days")
        bday_options = bday_options.T




        #creates dataframe of birth year xpaths
        byear_paths= ['//*[@id="participant-birth-pindex-1year"]/option[22]','//*[@id="participant-birth-pindex-1year"]/option[23]','//*[@id="participant-birth-pindex-1year"]/option[24]','//*[@id="participant-birth-pindex-1year"]/option[25]','//*[@id="participant-birth-pindex-1year"]/option[26]','//*[@id="participant-birth-pindex-1year"]/option[27]','//*[@id="participant-birth-pindex-1year"]/option[28]','//*[@id="participant-birth-pindex-1year"]/option[29]','//*[@id="participant-birth-pindex-1year"]/option[30]','//*[@id="participant-birth-pindex-1year"]/option[31]','//*[@id="participant-birth-pindex-1year"]/option[32]','//*[@id="participant-birth-pindex-1year"]/option[33]','//*[@id="participant-birth-pindex-1year"]/option[34]','//*[@id="participant-birth-pindex-1year"]/option[35]','//*[@id="participant-birth-pindex-1year"]/option[36]','//*[@id="participant-birth-pindex-1year"]/option[37]','//*[@id="participant-birth-pindex-1year"]/option[38]','//*[@id="participant-birth-pindex-1year"]/option[39]','//*[@id="participant-birth-pindex-1year"]/option[40]','//*[@id="participant-birth-pindex-1year"]/option[41]','//*[@id="participant-birth-pindex-1year"]/option[42]']
        byears = ['2020', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980']
        byear_options = {"years": byears, "byear_paths": byear_paths}
        byear_options = pd.DataFrame(byear_options)
        byear_options = byear_options.set_index("years")
        byear_options = byear_options.T


        #creates variables for the required paths

        try:
            booking_day_path = calendar_xpaths[booking_input["day_selection"]][0]
        except:
            print("the selected day isn't bookable")

        booking_time_path = booking_time[booking_input["booking_time"]][0]
        bmonth_path = bmonth_options[booking_input["bday_month"]][0]
        bday_path = bday_options[booking_input['bday_day']][0]
        byear_path = byear_options[booking_input['bday_year']][0]

        print(f'''

        booking_day_path = {booking_day_path}
        booking_time_path = {booking_time_path}
        bmonth_path = {bmonth_path}
        bday_path = {bday_path}
        byear_path =  {byear_path}
        gym_url = {gym_url}
        first_name = {first_name}
        last_name = {last_name}
        phone_number = {phone_number}
        email = {email}
            ''')

            #payload
        booking_paths = {

            "booking_day_path" : booking_day_path,
            "booking_time_path" : booking_time_path,
            "bmonth_path" : bmonth_path,
            "bday_path" : bday_path,
            "byear_path" : byear_path,
            "gym_url" : gym_url,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email':email,
            }

        return booking_paths


if __name__ == "__main__":
    main()
