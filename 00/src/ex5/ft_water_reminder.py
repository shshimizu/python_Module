def ft_water_reminder()->None:
    passed_days = int(input("Days since last watering: "))
    if passed_days >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
