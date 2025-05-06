import csv
import random

# Set seed for consistency
random.seed(42)

# List of about 100 countries
countries = [
    "USA", "Canada", "Mexico", "Brazil", "Argentina", "Chile", "UK", "France", "Germany", "Italy",
    "Spain", "Portugal", "Netherlands", "Belgium", "Switzerland", "Austria", "Poland", "Sweden", "Norway", "Denmark",
    "Finland", "Russia", "Ukraine", "Turkey", "Israel", "Egypt", "South Africa", "Nigeria", "Kenya", "Morocco",
    "China", "Japan", "South Korea", "India", "Pakistan", "Indonesia", "Vietnam", "Thailand", "Malaysia", "Australia",
    "New Zealand", "Philippines", "Saudi Arabia", "UAE", "Qatar", "Jordan", "Lebanon", "Iran", "Iraq", "Greece",
    "Hungary", "Czech Republic", "Slovakia", "Romania", "Bulgaria", "Croatia", "Serbia", "Slovenia", "Ireland", "Iceland",
    "Singapore", "Bangladesh", "Sri Lanka", "Nepal", "Afghanistan", "Kazakhstan", "Uzbekistan", "Georgia", "Armenia", "Azerbaijan",
    "Peru", "Colombia", "Venezuela", "Uruguay", "Paraguay", "Bolivia", "Ecuador", "Panama", "Costa Rica", "Cuba",
    "Dominican Republic", "Honduras", "El Salvador", "Guatemala", "Nicaragua", "Jamaica", "Trinidad and Tobago", "Bahamas", "Zimbabwe", "Ethiopia"
]

# Plan types
plan_types = ["basic", "standard", "premium", "student"]

# Build a dictionary country+type -> monthly_cost to ensure consistency
monthly_cost_lookup = {}
for country in countries:
    for plan_type in plan_types:
        if plan_type == "basic":
            cost = round(random.uniform(3.99, 7.99), 2)
        elif plan_type == "standard":
            cost = round(random.uniform(8.99, 12.99), 2)
        elif plan_type == "premium":
            cost = round(random.uniform(13.99, 18.99), 2)
        elif plan_type == "student":
            cost = round(random.uniform(1.99, 4.99), 2)
        monthly_cost_lookup[(country, plan_type)] = cost

# Now generate 1000 rows
rows = []
for plan_id in range(1, 1001):
    country = random.choice(countries)
    plan_type = random.choice(plan_types)
    monthly_cost = monthly_cost_lookup[(country, plan_type)]
    device_limit = random.randint(1, 10)
    rows.append([plan_id, country, plan_type, monthly_cost, device_limit])

# Write to CSV
with open('subscription_plans.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["plan_id", "country", "type", "monthly_cost", "device_limit"])
    writer.writerows(rows)

print("✅ CSV file 'subscription_plans.csv' created successfully!")
