
Monthly Expense Tracker (Pandas Version)

A Python-based tool using Pandas to group and summarize departmental expenses by month.

 Features

-  Load expenses data from CSV or manually-defined lists
- Group expenses by **month (YYYY-MM)** and department
- Generate clear summaries of total expenses
- Easy to integrate with monthly reports or dashboards

Technologies Used

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [datetime](https://docs.python.org/3/library/datetime.html)

Sample Code

```python
import pandas as pd
from datetime import datetime

# Sample data
expenses = [
    {"department": "HR", "date": "2025-07-10", "amount": 120.00},
    {"department": "IT", "date": "2025-07-15", "amount": 300.00},
    {"department": "HR", "date": "2025-08-01", "amount": 150.00},
]

# Convert to DataFrame
df = pd.DataFrame(expenses)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

# Group and summarize
summary = df.groupby(['month', 'department'])['amount'].sum().unstack(fill_value=0)
print(summary)
