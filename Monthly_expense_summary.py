import pandas as pd
from datetime import datetime

# Sample list of expense records
expense_records = [
    {"department": "HR", "date": "2025-08-01", "amount": 1500.00},
    {"department": "IT", "date": "2025-08-12", "amount": 3000.00},
    {"department": "Finance", "date": "2025-08-25", "amount": 2200.00},
    {"department": "HR", "date": "2025-07-14", "amount": 1800.00},
    {"department": "IT", "date": "2025-07-30", "amount": 2500.00},
    {"department": "Finance", "date": "2025-07-05", "amount": 1000.00},
]

# Convert to DataFrame
df = pd.DataFrame(expense_records)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract Year-Month (e.g., '2025-08')
df['month'] = df['date'].dt.to_period('M')

# Group by department and month, then sum the expenses
monthly_summary = df.groupby(['department', 'month'])['amount'].sum().reset_index()

# Optional: Format 'month' back to string for better display
monthly_summary['month'] = monthly_summary['month'].astype(str)

# Sort the result
monthly_summary = monthly_summary.sort_values(by=['month', 'department'])

# Display the summary
print(monthly_summary)