from datetime import datetime
import pandas as pd
import random
import smtplib

EMAIL = "abc@gmail.com"
PASS = "abcd"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthday.csv")
birthdays_dict = {(data_row["Month"], data_row["Day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file = f"letter_{random.randint(1,3)}.txt"
    with open(file, 'r') as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["Name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
