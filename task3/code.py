
packages = []
vehicles = []

n = int(input("Enter number of packages: "))

for i in range(n):
    print(f"\nPackage {i + 1}")
    pid = input("Package ID: ")
    weight = float(input("Weight (kg): "))
    zone = input("Destination zone: ").upper()
    priority = input("Priority (High/Medium/Low): ").capitalize()

    if weight <= 0 or priority not in ["High", "Medium", "Low"]:
        print("Invalid package details!")
        raise SystemExit

    packages.append({
        "id": pid,
        "weight": weight,
        "zone": zone,
        "priority": priority
    })

m = int(input("\nEnter number of vehicles: "))

for i in range(m):
    print(f"\nVehicle {i + 1}")
    vid = input("Vehicle ID: ")
    capacity = float(input("Capacity (kg): "))
    zone = input("Destination zone: ").upper()

    if capacity <= 0:
        print("Invalid vehicle capacity!")
        raise SystemExit

    vehicles.append({
        "id": vid,
        "capacity": capacity,
        "remaining": capacity,
        "zone": zone,
        "packages": []
    })

# High priority packages are processed first
priority_order = {"High": 1, "Medium": 2, "Low": 3}
packages.sort(key=lambda p: priority_order[p["priority"]])

undispatched = []

for package in packages:
    assigned = False

    for vehicle in vehicles:
        if (vehicle["zone"] == package["zone"]
                and vehicle["remaining"] >= package["weight"]):
            vehicle["packages"].append(package["id"])
            vehicle["remaining"] -= package["weight"]
            assigned = True
            break

    if not assigned:
        undispatched.append(package["id"])

# Display dispatch report
print("\n===== COURIER DISPATCH REPORT =====")

for vehicle in vehicles:
    print(f"\nVehicle: {vehicle['id']}")
    print(f"Destination Zone: {vehicle['zone']}")
    print("Packages:", ", ".join(vehicle["packages"])
          if vehicle["packages"] else "None")
    print(f"Remaining Capacity: {vehicle['remaining']:.2f} kg")

print("\nUndispatched Packages:",
      ", ".join(undispatched) if undispatched else "None")

