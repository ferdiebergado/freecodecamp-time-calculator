def add_time(start: str, duration: str, fow: str = "Sunday"):

    [start_time, meridian] = start.split()
    [start_hr, start_mins] = start_time.split(":")

    start_hr = int(start_hr)
    start_mins = int(start_mins)

    meridian = meridian.lower()

    [dur_hr, dur_mins] = duration.split(":")

    dur_hr = int(dur_hr)
    dur_mins = int(dur_mins)

    if meridian == "pm":
        start_hr = start_hr + 12

    h = (start_hr + dur_hr) % 24
    days = (start_hr + dur_hr) // 24
    m = (start_mins + dur_mins) % 60
    days += (start_mins + dur_mins) // 60

    new_meridian = "am"

    if h > 12:
        h = h - 12
        new_meridian = "pm"

    print(h, m, new_meridian, days)
    # return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
