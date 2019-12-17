Instructions to run the web server:

- Make the folder as the working directory and 
  run "pip install -r requirements.txt" to install the required packages.
------------------------------------

Running the web server:

- If using the existing database skip this section
	- If database connection is changed Run the following commands
		python manage.py makemigrations
		python manage.py migrate
		python manage.py loaddata locations #To populate the location data
	
- Run the server
	use "python manage.py" runserver to start the server
	The weather app can be found at localhost:port/weather
	with default settings "http://127.0.0.1:8000/weather/"



--------------------------------------
Sending emails:

- In settings.py add your email and password
- Add you OpenWeatherMap api and SendGrid api in keys.py or import them from Environment varibales
- then run 
	python manage.py sendmail
- Done!



-------------------------------------

Weather Function
weather/utils/weatherEmailHelper.py
get_temps:

- Grabs current temperature
- And grabs temp for 24 hours(84000secs) from reception time.

------------------------------------

Mail subject generator:

if status == 'Clear' or diff > 5:
    subject = "It's nice out! Enjoy a discount on us."
elif status in ('Rain', 'Thunderstorm', 'Drizzle') or diff <= 5:
    subject =  "Not so nice out? That's okay, enjoy a discount on us."
else:
    subject = "Enjoy a discount on us." 

--------------------------------------

