import sys
from tempYear import tempYear
from temp10Years import temp10Years
from snowfall import snowfall
from rain import rain

# Valid command line arguments: tempYear - temp10Years - rain - snowfall

#I used OpenMeteo's free to use Historical Weather API ---> https://open-meteo.com/en/docs/historical-weather-api
#Navigate to the site, enter your preferred timezone and copy and paste the produced url and also change the coordinates to 
#the location of your choosing. Lastly, include in the url the quantity you want to measure etc: rain, snowfall.

if len(sys.argv) > 1:
	arg = sys.argv[1]
else:
	arg = None

if __name__ == "__main__":
	if arg == "tempYear":
		tempYear()
	elif arg == "temp10Years":
		temp10Years()
	elif arg == "rain":
		rain()
	elif arg == "snowfall":
		snowfall()
	else:
		"exit"
		exit()