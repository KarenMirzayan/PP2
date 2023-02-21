import datetime
x1 = datetime.datetime(2020, 5, 17, 1, 1, 1)
x2 = datetime.datetime(2020, 5, 17, 0, 0, 0)
x = x1 - x2
print(x.days * 24 * 3600 + x.seconds)