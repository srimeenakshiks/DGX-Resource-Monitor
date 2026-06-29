from analytics import *

dashboard = get_dashboard_data()

print("=" * 60)

for key, value in dashboard.items():

    print(f"\n{key}")

    print("-" * 60)

    if hasattr(value, "head"):
        print(value.head())
    else:
        print(value)

print("\nEverything loaded successfully! 🚀")
