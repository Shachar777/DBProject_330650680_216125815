import random

# Define possible values
regions = ["North America", "Europe", "Asia", "Australia", "South America", "Africa"]
plan_types = ["Basic", "Standard", "Premium"]
durations = ["Monthly", "Half-Year", "Yearly"]

# Open the file to write SQL script
with open("insertSubscriptionPlans.sql", "w", encoding="utf-8") as f:
    f.write("-- Insert 1000 rows into Subscription_Plans\n")

    for plan_id in range(1, 1001):
        region = random.choice(regions)
        plan_type = random.choice(plan_types)
        duration = random.choice(durations)
        monthly_cost = round(random.uniform(5, 50), 2)  # Random cost between $5.00 and $50.00

        plan_name = f"{region} {plan_type} {duration}"
        sql = f"INSERT INTO Subscription_Plans (plan_id, plan_name, monthly_cost) VALUES ({plan_id}, '{plan_name}', {monthly_cost});\n"
        f.write(sql)

print("✅ SQL script 'insertSubscriptionPlans.sql' has been generated!")
