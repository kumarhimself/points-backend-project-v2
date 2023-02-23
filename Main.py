from paymentqueue.PaymentNode import PaymentNode
from paymentqueue.PaymentQueue import PaymentQueue

node_one = PaymentNode("Paul Dasika", 32, "2020-10-31T4:00:00Z")
node_two = PaymentNode("Paul Dasika", 93, "2020-10-31T11:00:00Z")
node_three = PaymentNode("Paul Dasika", 28, "2020-10-31T15:00:00Z")
node_four = PaymentNode("Paul Dasika", 64, "2020-10-31T16:00:00Z")

node_one.set_next_payment(node_two)
node_two.set_next_payment(node_three)
node_three.set_next_payment(node_four)
node_four.set_next_payment()

queue = PaymentQueue("Paul Dasika")

queue.enqueue(node_one)
queue.enqueue(node_two)
queue.enqueue(node_three)
queue.enqueue(node_four)

print(queue.peek())
print(queue)
