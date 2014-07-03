#!/usr/bin/python

import json
import urllib2
import cgi
import cgitb

# Gives the error log on the web page itself if the script fails
cgitb.enable()

print "Content-type: text/html\n\n"
print

# Method to get and parse information from the weather API	
def weatherAPI(city):

# Will fetch data from the given URL and convert it to JSON
	r = urllib2.urlopen("http://openweathermap.org/data/2.1/find/name?q="+city).read().decode("utf-8")

# Converts the data from JSON to Python dictionary
	data = json.loads(r)

# We can access the data directly as Python dictionary
	print "Name of City: %s\n" %(data['list'][0]['name'])
	print '<br></br>'
	print "Latitude: %s" %(data['list'][0]['coord']['lat'])
	print '<br></br>'
	print "Longitude: %s" %(data['list'][0]['coord']['lon'])
	print '<br></br>'
	print "Current Temperature: %d degree C" %(float(data['list'][0]['main']['temp'])-274.15)
	print '<br></br>'
	print "Minimum Temperature: %d degree C" %(float(data['list'][0]['main']['temp_min'])-274.15)
	print '<br></br>'
	print "Maximum Temperature: %d degree C" %(float(data['list'][0]['main']['temp_max'])-274.15)
	print '<br></br>'
	print "General Weather: %s" %(data['list'][0]['weather'][0]['main'])
	print '<br></br>'
	print "Date: %s" %(data['list'][0]['date'])
	print '<br></br>'
	print
	print

def main():


# Title gives the name to the tab
	print '<title>Weather Station</title>'

# Gives a heading on the first line of the web page
	print '<h3> Weather Station </h3>'

	try:

# FieldStorage class in Pyton is used to implement forms in HTML
		form = cgi.FieldStorage()

		city = form.getvalue('city')

# Following statements are the actions to be performed in HTML
		print """

		<form action="/cgi-bin/sample.py" method="get">
		City: <input type="text" name="city">  

		<input type="submit" value="Submit" /><br />
		</form>
		"""

# Call the Weather function to get and parse data from Weatehr API
		weatherAPI(city)
		
# If the user enters an Invalid City name
	except KeyError:
		print "Not a valid city!"

main()
