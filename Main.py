from paymentqueue.PaymentNode import PaymentNode
from paymentqueue.PaymentQueue import PaymentQueue

node_one = PaymentNode("Paul Dasika", 32, "2020-10-31T4:00:00Z")
node_two = PaymentNode("Paul Dasika", 93, "2020-10-31T11:00:00Z")
node_three = PaymentNode("Paul Dasika", 28, "2020-10-31T15:00:00Z")
node_four = PaymentNode("Paul Dasika", 64, "2020-10-31T16:00:00Z")

queue = PaymentQueue("Paul Dasika")

queue.enqueue(node_one)
queue.enqueue(node_two)
queue.enqueue(node_three)
queue.enqueue(node_four)

print(queue.get_user_balances())

queue.spend_points(50)

print(queue.get_user_balances())
