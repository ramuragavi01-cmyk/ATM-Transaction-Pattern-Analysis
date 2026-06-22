import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("atm_transactions.csv")

# Count transaction types
transaction_type = df["Transaction_Type"].value_counts()

# Display counts
print(transaction_type)

# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(
    transaction_type,
    labels=transaction_type.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Transaction Type Distribution")
plt.show()

status = df["Status"].value_counts()

status.plot(kind="bar")

plt.title("Transaction Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()
plt.hist(df["Amount"], bins=10)

plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()
atm = df["ATM_ID"].value_counts()

atm.plot(kind="bar")

plt.title("Most Used ATM")
plt.xlabel("ATM ID")
plt.ylabel("Transactions")
plt.show()
avg = df.groupby("Location")["Amount"].mean()

avg.plot(kind="bar")

plt.title("Average Transaction Amount by Location")
plt.xlabel("Location")
plt.ylabel("Average Amount")
plt.show()

