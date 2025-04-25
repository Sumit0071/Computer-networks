def print_color_code(title, end_a, end_b):
    print(f"\n{'='*10} {title} {'='*10}")
    print(f"{'Pin':<5} {'End A':<20} {'End B'}")
    print("-" * 40)
    for pin in range(1, 9):
        print(f"{pin:<5} {end_a[pin-1]:<20} {end_b[pin-1]}")
    print("=" * 40)

# T568A and T568B standard colors
T568A = [
    "White-Green",
    "Green",
    "White-Orange",
    "Blue",
    "White-Blue",
    "Orange",
    "White-Brown",
    "Brown"
]

T568B = [
    "White-Orange",
    "Orange",
    "White-Green",
    "Blue",
    "White-Blue",
    "Green",
    "White-Brown",
    "Brown"
]

# Straight-Through: T568B on both ends
print_color_code("Straight-Through Cable (T568B)", T568B, T568B)

# Crossover: T568A on one end, T568B on the other
print_color_code("Crossover Cable", T568A, T568B)
