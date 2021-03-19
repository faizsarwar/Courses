# ju module import krwana huta hai us name say file nhi bnasktay wrna circular import error ata hai 
import datetime
import pytz

today= datetime.date.today() 
print(today,"      todays date !!!")
birthday = datetime.date(2000, 8, 7 )    #It is not a string it is an object here
print(birthday,"    my birthdy !!!")

day_from_birth= today - birthday                                        #calculating day from birthday 
print(day_from_birth.days,"         day from todays date !!!")          #converting into days wrna time bhi show huga

# adding days in today
tdelta= datetime.timedelta(days=10)
print(today+tdelta, "   10 days added from todays date")
# adding hours in today
today1=datetime.datetime.now()
hdelta= datetime.timedelta(hours=8)
print(today1, "<-   8 hours added from todays date    ->", today1+hdelta)

print(today-tdelta, "   10 days subtracted from todays date")
print(today.day,"       printing day")    #printing day 
print(today.month,"     printing month ")  #printing month
print(today.year,"      printing year")   #printing year
# monday = 0 , sunday = 6
print(today.weekday(), "      printing weekday like monday,teusday etc starting from 0 endng at 6")

# to set time   by defaut time is set at 00:00:00 we have to set time in our code
time=datetime.time(7, 55, 4,14)  # hours , minutes, seconds, microsecond
print(time)

#datetime.time( h, m, s, ms)
#datetime.date( y , M , D)
#datetime.datetime( y , M , D,   h, m, s, ms)

# setting timezone
today_time=datetime.datetime.now(tz=pytz.UTC)
# pehlay utc pe set krna huga phr timezone desktay hain
print(today_time) # UTC
# for tz in pytz.all_timezones:
#     print(tz)

# setting zone
today_time_karachi=today_time.astimezone(pytz.timezone("Asia/Karachi"))
print(today_time_karachi)   # time of karachi

# string formatting with dates(displaaing mane of the month instead of number)
#strftime -> (f= formating) string mai convert krnay k baad add subtract nhi kr sktay dates
print(today_time_karachi.strftime("%B %d, %Y"))  # %B for months full name %b for months short name

# convetring back nov04, 2020   -> datetime(2020-1-04)d
#strptime -> (p= parsing)
print(today_time_karachi.strptime("November 04, 2020","%B %d, %Y"))