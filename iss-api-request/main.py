import requests
import smtplib
from datetime import datetime
from time import sleep

MY_LAT = 52.456920
MY_LNG = -2.113090

MY_EMAIL = 'jenkinsdummy72@gmail.com'
PASSWORD = 'AlexJackGeo3'
RECIPIENT = 'jenkinsdummy01@yahoo.com'

def iss_close():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_lng = float(iss_data['iss_position']['longitude'])

    print(f'iss lat: {iss_lat}; iss lng: {iss_lng}')

    return (iss_lat >=MY_LAT - 5 and iss_lat <= MY_LAT + 5) and \
           (iss_lng >= MY_LNG - 5 and iss_lng <= MY_LNG + 5)

def is_night():

    parameters = {
        'lat' : MY_LAT,
        'lng' : MY_LNG,
        'formatted' : 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    hour = datetime.now().hour
    print(f'sunrise: {sunrise}; sunset: {sunset}; hour: {hour}')
    return (hour < sunrise) or (hour > sunset)

def send_email():

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT,
                            msg=f"Subject : ISS OVER LYE\n\n"
                                f"Look out of your window, the ISS is over"
                                f"the Lye tonight!")
    print('Email sent')

while True:
    print(f'my lat: {MY_LAT}; my lng: {MY_LNG}')
    if iss_close() and is_night():
        send_email()
    else:
        is_night()
        print('email not sent')
    sleep(10)
    print('slept\n')
    if (input('QUIT Y/n').lower() == 'y'): break




