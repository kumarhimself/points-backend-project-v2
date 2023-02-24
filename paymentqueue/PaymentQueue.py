# Stores all the nodes in ascending order from oldest to newest transaction in a FIFO (first-in, first-out) fashion
class PaymentQueue:
    # Constructor
    def __init__(self):
        self.user_balances = {}  # Dictionary of all user's points
        self.oldestPayment = None  # First node in queue and has oldest timestamp
        self.newestPayment = None  # Last node in queue and has newest timestamp
        self.size = 0  # Initial size of queue is zero as there are no nodes in it yet

    # To string function
    def __str__(self):
        toString = ""
        currentPayment = self.oldestPayment

        for i in range(self.size):
            toString += currentPayment.__str__() + "\n"
            currentPayment = currentPayment.get_next_payment()

        return toString

    # Returns size of queue
    def get_size(self):
        return self.size

    # Checks if queue is empty
    def is_empty(self):
        return self.size == 0

    # Retursn oldest payment in queue (node at the front of the queue)
    def peek(self):
        return self.oldestPayment

    # Adds new payment to end of queue
    def enqueue(self, nextPayment):
        oldNewestPayment = self.newestPayment
        self.newestPayment = nextPayment
        self.newestPayment.set_next_payment()

        if (PaymentQueue.is_empty(self)):
            self.oldestPayment = self.newestPayment
        else:
            oldNewestPayment.set_next_payment(self.newestPayment)

        self.size += 1

    # Removes oldest payment in queue (node at front of the queue)
    def dequeue(self):
        nodeToRemove = self.oldestPayment

        self.oldestPayment = nodeToRemove.get_next_payment()
        self.size -= 1

        return nodeToRemove

    # Spends points from oldest payment to newest, if a payment node runs out of points, it is removed from the queue
    def spend_points(self, points_to_spend):
        while True:
            currentPayment = self.oldestPayment

            if (points_to_spend > currentPayment.get_points()):
                points_to_spend -= currentPayment.get_points()

                if (currentPayment.get_name() not in self.user_balances.keys()):
                    self.user_balances[currentPayment.get_name()] = 0

                PaymentQueue.dequeue(self)
            else:
                currentPayment.remove_points(points_to_spend)
                break

    # Returns summary of all user's total points
    def get_user_balances(self):
        currentPayment = self.oldestPayment

        for index in range(self.size):
            if (currentPayment.get_name() not in self.user_balances.keys()):
                self.user_balances[currentPayment.get_name(
                )] = currentPayment.get_points()
            else:
                self.user_balances[currentPayment.get_name(
                )] += currentPayment.get_points()

            currentPayment = currentPayment.get_next_payment()

        return self.user_balances
