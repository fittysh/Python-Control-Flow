def ground_rate(weight):
    if weight <= 2:
        return 1.50
    elif weight <= 6:
        return 3.00
    elif weight <= 10:
        return 4.00
    return 4.75


def drone_rate(weight):
    if weight <= 2:
        return 4.50
    elif weight <= 6:
        return 9.00
    elif weight <= 10:
        return 12.00
    return 14.25


weight = 4.8
GROUND_FLAT = 20.00
PREMIUM_GROUND = 125.00

ground_total = (weight * ground_rate(weight)) + GROUND_FLAT
premium_total = PREMIUM_GROUND
drone_total = weight * drone_rate(weight)

print(f"Weight: {weight:.1f} lb")
print(f"Ground Shipping: ${ground_total:.2f}")
print(f"Premium Ground Shipping: ${premium_total:.2f}")
print(f"Drone Shipping: ${drone_total:.2f}")

cheapest_name, cheapest_cost = min(
    [
        ("Ground Shipping", ground_total),
        ("Premium Ground Shipping", premium_total),
        ("Drone Shipping", drone_total),
    ],
    key=lambda x: x[1],
)

print(f"Cheapest option: {cheapest_name} (${cheapest_cost:.2f})")