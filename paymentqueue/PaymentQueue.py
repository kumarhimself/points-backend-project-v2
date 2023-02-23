class PaymentQueue:
    def __init__(self, oldestPayment=None, newestPayment=None, size=0):
        self.oldestPayment = oldestPayment
        self.newestPayment = newestPayment
        self.size = size

    def __str__(self):
        toString = ""
        currentPayment = self.oldestPayment

        for i in range(self.size):
            toString += currentPayment.__str__() + "\n"
            currentPayment = currentPayment.get_next_payment()

        return toString

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.oldestPayment

    def enqueue(self, nextPayment):
        oldNewestPayment = self.newestPayment
        self.newestPayment = nextPayment
        self.newestPayment.set_next_payment()

        if (PaymentQueue.is_empty(self)):
            self.oldestPayment = self.newestPayment
        else:
            oldNewestPayment.set_next_payment(self.newestPayment)

        self.size += 1

    def dequeue(self):
        nodeToRemove = self.oldestPayment

        self.oldestPayment = nodeToRemove.get_next_payment()
        self.size -= 1

        return nodeToRemove

    def spend_points(self, points_to_spend):
        while True:
            currentPayment = self.oldestPayment

            if (points_to_spend > currentPayment.get_points()):
                points_to_spend -= currentPayment.get_points()
                PaymentQueue.dequeue(self)
            else:
                currentPayment.remove_points(points_to_spend)
                break

    def get_user_balances(self):
        user_balances = {}
        currentPayment = self.oldestPayment

        for index in range(self.size):
            if (currentPayment.get_name() not in user_balances):
                user_balances[currentPayment.get_name(
                )] = currentPayment.get_points()
            else:
                user_balances[currentPayment.get_name(
                )] += currentPayment.get_points()

            currentPayment = currentPayment.get_next_payment()

        return user_balances
