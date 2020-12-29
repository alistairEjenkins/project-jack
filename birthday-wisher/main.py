
import datetime as dt
import pandas
from random import choice
import smtplib

day_today = dt.date.today().day
month_today = dt.date.today().month
letters = ['letter_1.txt','letter_2.txt','letter_3.txt']

with open('birthdays.csv', 'r') as data_file:
    data = pandas.read_csv(data_file)
    data = data.to_dict(orient='records')
    for person in data:
        if person['day'] == day_today and person['month'] == month_today:
            letter = choice(letters)
            with open(f'letter_templates/{letter}', 'r') as letter_file:
                message = letter_file.read()
                message = message.replace('[NAME]', person["name"])

                my_email = 'jenkinsdummy72@gmail.com'
                password = 'AlexJackGeo3'

                with smtplib.SMTP('smtp.gmail.com') as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=person['email'],
                                        msg=f"Subject : IT'S YOUR BIRTHDAY\n\n{message}")





##################### Extra Hard Starting Project ######################





