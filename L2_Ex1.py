from datetime import datetime

try:
    f = open("D:\\Anna\\Bootcamp exercises\\python\\Python_Anna_Lebed\\ITC-Python-AnnaLebed\\L2\\my_log.txt", "a")
except Exeption as e:
    print(e)

date_time_obj = datetime.now()
message = " This is a test message"
timestamp_str_message = date_time_obj.strftime("%d-%b-%Y %H:%M:%S:" + message + "\n")

f.write(timestamp_str_message)




