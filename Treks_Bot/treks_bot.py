import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from lxml import html
import requests


mock_booking_paths = {

    'booking_day_path':'//*[@id="start_date_calendar"]/div/table/tbody/tr[3]/td[4]',
    "booking_time_path" : '//*[@id="offering-page-select-events-table"]/tbody/tr[2]/td[4]/a',
    "bmonth_path" : '//*[@id="participant-birth-pindex-1month"]/option[5]',
    "bday_path" : '//*[@id="participant-birth-pindex-1day"]/option[19]',
    "byear_path" : '//*[@id="participant-birth-pindex-1year"]/option[32]',
    "gym_url" : 'https://app.rockgympro.com/b/widget/?a=offering&offering_guid=d9a768a045814f56a9fa79de9af419bf&random=5fce726e16a35&iframeid=&mode=p'
    }

def main():
    
    member_button_path = '//*[@id="theform"]/div[6]/div/fieldset/table/tbody/tr[1]/td[1]/a[2]'
    first_name_path = '//*[@id="pfirstname-pindex-1-1"]'
    last_name_path = '//*[@id="plastname-pindex-1-1"]'
    birth_month_path = '//*[@id="participant-birth-pindex-1month"]'
    roped_policy = '//*[@id="theform"]/fieldset[2]/div[2]/span/input'
    cancel_policy = '//*[@id="theform"]/fieldset[3]/div[2]/span/input'
    belay_check = '//*[@id="p1e3439023311f43c5aed076213a64e47b"]/option[3]'
    lead_check =  '//*[@id="p10a0c36e929a24acfa25acf66ac5b5331"]/option[3]'
    continue_ = '//*[@id="theform"]/a[2]'
    email_path = '//*[@id="customer-email"]'
    phone_path = '//*[@id="customer-phone"]'
    confirm_button = '//*[@id="confirm_booking_button"]'
    agree_box = '//*[@id="theform"]/fieldset[5]/div[2]/input'
    cancel_box = '//*[@id="theform"]/fieldset[5]/div[3]/strong[8]/span/input'



    #sets variables from the input
    gym_url = mock_booking_paths["gym_url"]
    booking_day_path = mock_booking_paths["booking_day_path"]
    booking_time_path = mock_booking_paths["booking_time_path"]
    bmonth_path = mock_booking_paths["bmonth_path"]
    bday_path = mock_booking_paths["bday_path"]
    byear_path = mock_booking_paths["byear_path"]
    



    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disachble-gpu')
        driver = webdriver.Chrome(options=options)
        driver.get(gym_url)
        web = webdriver.Chrome()
        web.get(gym_url)
    except:
        print("issue with web driver or gym url")
        

    try:
        calendar_button = web.find_element_by_xpath(booking_day_path)
        calendar_button.click()
    except:
        print("issue with calendar selection xpath")


    try:
        member_button = web.find_element_by_xpath(member_button_path)
        member_button.click()
    except:
        print("issue with the 'how many members button?' xpath")
        
    try:
        time_button = web.find_element_by_xpath(booking_time_path)
        time_button.click()
    except:
        print("script ran too early or there's issue with the booking_time_path xpath")

    try:
        first = web.find_element_by_xpath(first_name_path)
        first.send_keys(first_name)
    except:
        print("issue with first name path")

    try:
        last = web.find_element_by_xpath(last_name_path)
        last.send_keys(last_name)
    except:
        print("issue with last name path")

    try:
        bmonth_button = web.find_element_by_xpath(bmonth_path)
        bmonth_button.click()
    except:
        print("issue with bmonth path")

    try:

        bday_button = web.find_element_by_xpath(bday_path)
        bday_button.click()
    except:
        print("issue with bday path")

    try:
        byear_button = web.find_element_by_xpath(byear_path)
        byear_button.click()
    except:
        print("issue with byear_path path")

        
    try:
        roped_climbing_box = web.find_element_by_xpath(roped_policy)
        roped_climbing_box.click()
    except:
        print("issue with byear_path path")

    try:
        cancellation_policy = web.find_element_by_xpath(cancel_policy)
        cancellation_policy.click()
    except:
        print("issue with byear_path path")

    try:
        belay_box = web.find_element_by_xpath(belay_check)
        belay_box.click()
    except:
         print("issue with belay check path")

    try:    
        lead_box = web.find_element_by_xpath(lead_check)
        lead_box.click()
    except:
        print("issue with lead check path")
        
    try:
        continue_button = web.find_element_by_xpath(continue_)
        continue_button.click()
    except:
        print("issue with continue_ path")

    try:    
        email_input = web.find_element_by_xpath(email_path)
        email_input.send_keys(email)
    except:
        print("issue with email_path path")

    try:    
        phone_input = web.find_element_by_xpath(phone_path)
        phone_input.send_keys(phone_number)
        
    except:
        print("issue with phone_path path")

    try:    

        noshow_box = web.find_element_by_xpath(noshow_box_path)
        noshow_box.click()
        
    except:
        print("issue with noshow_box_path")

    try:
        complete_button = web.find_element_by_xpath(complete_button_path)
        complete_button.click()
    except:
        print("issue with complete_button_path")

    try:
        complete_button = web.find_element_by_xpath(agree_box)
        complete_button.click()
    except:
        print("issue with agree_box path")

    try:
        complete_button = web.find_element_by_xpath(cancel_box)
        complete_button.click()
    except:
        print("issue with cancel_box path")

    try:
        complete_button = web.find_element_by_xpath(confirm_button)
        complete_button.click()
        
    except:
        print("issue with confirm_button path")    
        
if __name__ == "__main__":
    main()
