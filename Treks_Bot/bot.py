import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from lxml import html
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import psycopg2
import psycopg2.extras

today = date.today().day
today = str(today)


def main():

    def pull_requests():
        DB_HOST="treks-base.cjmt85ipuno1.us-west-2.rds.amazonaws.com"
        port="5432"
        DB_USER = "postgres"
        DB_NAME="bookings"
        connect_timeout="10"
        DB_PASS="place_holder"
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT * FROM booking_requests
    WHERE booking_id LIKE '%enriched%'
    """)
        global requests
        requests = cur.fetchall()

        return requests

        def execute_bot(requests):

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

            for i in range(len(requests)):
                if requests[i][10] == today:

                    first_name = requests[i][1]
                    last_name = requests[i][2]
                    email = requests[i][4]
                    phone_number = requests[i][3]
                    gym_url = requests[i][15]
                    booking_time_path = requests[i][11]
                    bmonth_path = requests[i][12]
                    bday_path = requests[i][13]
                    byear_path = requests[i][14]
                    booking_day_path = requests[i][16]

                    try:
                    options = Options()
                    options.add_argument('--headless')
                    options.add_argument('--disachble-gpu')
                    driver = webdriver.Chrome(options=options)
                    driver.get(gym_url)
                    driver.implicitly_wait(10)
                    web = webdriver.Chrome()
                    web.get(gym_url)
                    driver.quit()

                    except:
                        print("issue with web driver or gym url")


                    try:
                        time.sleep(3)
                        calendar_button = web.find_element_by_xpath(booking_day_path)
                        calendar_button.click()
                    except:
                        print("issue with calendar selection xpath")


                    try:
                        time.sleep(3)
                        member_button = web.find_element_by_xpath(member_button_path)
                        member_button.click()
                    except:
                        print("issue with the 'how many members button?' xpath")

                    try:
                        time.sleep(3)
                        time_button = web.find_element_by_xpath(booking_time_path)
                        time_button.click()
                    except:
                        print("script ran too early or there's issue with the booking_time_path xpath")

                    try:
                        time.sleep(3)
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
                        time.sleep(3)
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
                        time.sleep(3)
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
                        time.sleep(3)
                        complete_button = web.find_element_by_xpath(confirm_button)
                        complete_button.click()
                        time.sleep(10)

                    except:
                        print("issue with confirm_button path")
                else:
                    pass
            return

if __name__ == "__main__":
    main()
