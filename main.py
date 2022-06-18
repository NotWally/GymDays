import webbrowser
from datetime import date

f = open("totaltime.txt", "r")
cur_total_time_s = int(f.read())
f.close

time_in_m = int(cur_total_time_s / 60)
time_in_h = int(time_in_m / 60)

d1 = date.today()
d2 = date(2022, 5, 19)
dayssince = d1-d2

now = str(d1.strftime("%d/%m/%Y"))
start = str(d2.strftime("%d/%m/%Y"))
line = str(dayssince.days) + " Days"

print("Start Date: 19/05/2022")
print("Todays Date:", d1.strftime("%d/%m/%Y"))
print("It has been", dayssince.days, "days!")

htmlcont = f'<html><head> <link rel="icon" type="image/x-icon" href="https://cdn.discordapp.com/attachments/872212099848368140/986938739865559050/arm_muscle_male_body_icon_143229.ico"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet"><title>GymDays</title><link rel="stylesheet" href="style.css"></head> <body> <div id="container"> <h1>{line}</h1> <p id="start">Start Date: {start}</p> <p id="today">Todays Date: {now}</p> <p id="ttltime">Total Time @ Gym: {time_in_h} Hours {time_in_m} Minutes {cur_total_time_s} Seconds</p> </div> <script src="app.js"> </body></html>'

with open ("index.html", "w") as html_file:
    html_file.write(htmlcont)
    print("good")

webbrowser.open_new_tab("index.html")
