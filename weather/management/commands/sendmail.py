from weather.utils.weatherEmailHelper import get_temps, send_email
from django.core.management.base import BaseCommand, CommandError
from weather.models import Email, Location


class Command(BaseCommand):
    help = 'Sends email to all subscribers based on their weather condition'
    email_dict = {}
    
    def handle(self,*args,**options):
        emails = Email.objects.all()
        for email in emails:
            self.get_and_send_email(email)
    

    def get_and_send_email(self,email,email_dict=email_dict):
        location = email.location
        loc_str = location.city + ',' + location.state + ',' + location.country
        if loc_str not in email_dict:
            status, temp, diff = get_temps(loc_str)
            body =  "%d degrees, %s" % (temp, status)
            if status == 'Clear' or diff > 5:
                subject = "It's nice out! Enjoy a discount on us."
            elif status in ('Rain', 'Thunderstorm', 'Drizzle') or diff < 5:
                subject =  "Not so nice out? That's okay, enjoy a discount on us."
            else:
                subject = "Enjoy a discount on us." 

            email_dict[loc_str] = [subject,body]
        else:
            subject = email_dict[loc_str][0]
            body = email_dict[loc_str][1]
        
        return send_email(email.email_address,subject,body)
