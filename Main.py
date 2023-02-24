# Used to read command-line arguments
import sys

# Used to import and transform CSV file
import pandas as pd

# Used to transform CSV timestamp into more readable format
from datetime import datetime

# Each payment record will be stored in a PaymentNode
from paymentqueue.PaymentNode import PaymentNode

# Data structure where all PaymentNodes will be stored
from paymentqueue.PaymentQueue import PaymentQueue

# Reading command-line arguments
points_to_spend = int(sys.argv[1])
filename = sys.argv[2]

# Reading CSV file into Pandas dataframe using filename provided by command-line arguments
transactions_df = pd.read_csv(filename)

# Converting dataframe timestamps to a more readable format
for index in range(len(transactions_df)):
    transactions_df.loc[index, "timestamp"] = datetime.strptime(
        transactions_df.loc[index, "timestamp"][:-4], '%Y-%m-%dT%H:%M')

# Sorting dataframe by timestamp in ascending order
transactions_df = transactions_df.sort_values(by="timestamp", ascending=True)

# Created a new PaymentQueue
payment_queue = PaymentQueue()

# Adding transaction records from dataframe into PaymentQueue
for index in range(len(transactions_df)):
    name = transactions_df.iloc[index]["payer"]
    points = transactions_df.iloc[index]["points"]
    timestamp = transactions_df.iloc[index]["timestamp"]

    payment_queue.enqueue(PaymentNode(name, points, timestamp))

# Spending points using points provided by command-line arguments
payment_queue.spend_points(points_to_spend)

print(payment_queue.get_user_balances())
