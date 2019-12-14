from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pyowm
from weather.utils.keys import WEATHER_KEY, MAIL_KEY, FROM_ADDRESS


def get_temps(loc_str,key=WEATHER_KEY):
    """ 
        params
        ------
        loc_str: location for which we need the outputs
                 eg.format loc_str = "Boston,MA,US"

        key:     openweathermap api key


        returns
        -------
        current weather status, current temperature
        and difference of current temperature and tomorrows temperature(24 hrs from now)
    """
    owm = pyowm.OWM(key)
    now = owm.weather_at_place(loc_str)
    current_temp = now.get_weather().get_temperature('fahrenheit')['temp']
    current_status = now.get_weather().get_status()
    current_time = now.get_reception_time()
        
    forecast = owm.three_hours_forecast(loc_str)
    tomorrow_temp = forecast.get_weather_at(current_time+84000).get_temperature('fahrenheit')['temp']
    return current_status, current_temp, round(current_temp-tomorrow_temp)


def send_email(email_address,subject,body,mail_api=MAIL_KEY,from_address=FROM_ADDRESS):
    """
        sends email via sendgrid uses smtp gmail

        params
        -------
        email_address: Recipients email address
        subject: Subject of the email we wanna send
        body: Body of the email can be a string or a html file
        mail_api: sendgrid api key
        from_address: from_address that we authorised in settings. 

        returns
        --------
        prints Email if email is sussefully send
        else prints the error code/ exception message
    """

    message = Mail(from_email = from_address, to_emails = email_address,
                    subject = subject,html_content = body)
    try:
        sg = SendGridAPIClient(mail_api)
        response = sg.send(message)
        print("Email Sent" if response.status_code==202 else response.status_code)
    except Exception as e:
        print("Sending email for %s failed reason:" % email_address )
        print(e.message)
