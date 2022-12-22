def hours_to_minute(hours):
    minutes=hours*60
    seconds=hours*3600
    print("there are",minutes, "minutes in", hours,"hours")
    print("there are",seconds, "seconds in", hours,"hours")

hours=int(input("Enter the hour"))
hours_to_minute(hours)