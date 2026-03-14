# Displaying weather and time (real time)

import datetime, subprocess

# Function to get weather (using wttr.in service)
def getWeather():
    try:
        return subprocess.getoutput("curl -s wttr.in/?format=3")
    except:
        return "Weather unavailable"

# Get current time
now = datetime.datetime.now()

# Get weather once
weather = getWeather()

# Display once
print(now.strftime("%d %B %Y  %I:%M:%S %p"))
print(weather)
