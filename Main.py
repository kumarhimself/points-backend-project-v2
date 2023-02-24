import sys
import pandas as pd  # pip install pandas
from datetime import datetime

from paymentqueue.PaymentNode import PaymentNode
from paymentqueue.PaymentQueue import PaymentQueue

points_to_spend = int(sys.argv[1])
filename = sys.argv[2]

transactions_df = pd.read_csv(filename)

for index in range(len(transactions_df)):
    transactions_df.loc[index, "timestamp"] = datetime.strptime(
        transactions_df.loc[index, "timestamp"][:-4], '%Y-%m-%dT%H:%M')

transactions_df = transactions_df.sort_values(by="timestamp", ascending=True)

payment_queue = PaymentQueue()

for index in range(len(transactions_df)):
    name = transactions_df.iloc[index]["payer"]
    points = transactions_df.iloc[index]["points"]
    timestamp = transactions_df.iloc[index]["timestamp"]

    payment_queue.enqueue(PaymentNode(name, points, timestamp))

payment_queue.spend_points(points_to_spend)
print(payment_queue.get_user_balances())
