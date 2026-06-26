def ft_count_harvest_iterative() -> None:
    harvest_day = int(input("Days until harvest: "))
    for day in range(0, harvest_day):
        print(f"Day {day + 1}")
    print("Harvest time!")
