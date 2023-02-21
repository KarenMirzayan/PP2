import datetime
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(1)
tomorrow = datetime.date.today() + datetime.timedelta(1)
print("Today:", today)
print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)