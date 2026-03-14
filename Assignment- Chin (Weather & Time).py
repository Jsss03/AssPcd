# Displaying weather and time (real time)

import datetime, subprocess, os

def getWeather():
    try:
        # wttr.in gives simple weather info
        return subprocess.getoutput("curl -s wttr.in/?format=3")
    except:
        return "Weather unavailable"

# Clear screen depending on OS
os.system("cls" if os.name == "nt" else "clear")

# Get current time
now = datetime.datetime.now()

# Get weather once
weather = getWeather()

# Display once
print(now.strftime("%d %B %Y  %I:%M:%S %p"))
print(weather)
