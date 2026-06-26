def ft_count_harvest_recursive() -> None:
    harvest_day = int(input("Days until harvest: "))
    def count_day(day=1) -> None:
        print(f"Day {day}")
        if day != harvest_day:
            count_day(day + 1)
        else:
            print("Harvest time!")
    count_day()
