def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit not in ("packets", "grams", "area"):
        print("Unknown unit type")
        return
    print(f"{seed_type}".capitalize(), f"seeds: {quantity} {unit} available")
