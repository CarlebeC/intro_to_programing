count = 0
total_rain = 0
total_wind = 0
while True:
    line = input()
    parts = line.split()
    rain = float(parts[0])
    if rain == -1.0:
        break
    wind = float(parts[1])
    total_rain += rain
    total_wind += wind
    count += 1
average_rain = total_rain / count
average_wind = total_wind / count
severity = (average_rain * 10) + average_wind
print("The average rain is", average_rain, "inches")
print("The average wind is", average_wind, "mph")
print("The weather severity for these", count, "readings is:", severity)