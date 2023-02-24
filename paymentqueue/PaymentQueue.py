class PaymentQueue:
    def __init__(self, size=0):
        self.user_balances = {}
        self.oldestPayment = None
        self.newestPayment = None
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

                if (currentPayment.get_name() not in self.user_balances.keys()):
                    self.user_balances[currentPayment.get_name()] = 0

                PaymentQueue.dequeue(self)
            else:
                currentPayment.remove_points(points_to_spend)
                break

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
