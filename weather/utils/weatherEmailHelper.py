from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pyowm
from weather.utils.keys import WEATHER_KEY, MAIL_KEY, FROM_ADDRESS


def get_temps(loc_str,key=WEATHER_KEY):
    owm = pyowm.OWM(key)
    now = owm.weather_at_place(loc_str)
    current_temp = now.get_weather().get_temperature('fahrenheit')['temp']
    current_status = now.get_weather().get_status()
    current_time = now.get_reception_time()
        
    forecast = owm.three_hours_forecast(loc_str)
    tomorrow_temp = forecast.get_weather_at(current_time+84000).get_temperature('fahrenheit')['temp']
    return current_status, current_temp, round(current_temp-tomorrow_temp)


def send_email(email_address,subject,body,mail_api=MAIL_KEY,from_address=FROM_ADDRESS):
    message = Mail(from_email = from_address, to_emails = email_address,
                    subject = subject,html_content = body)
    try:
        sg = SendGridAPIClient(mail_api)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print("Sending email for %s failed reason:" % email_address )
        print(e.message)