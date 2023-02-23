class PaymentQueue:
    def __init__(self, name, oldestPayment=None, newestPayment=None, size=0):
        self.name = name
        self.oldestPayment = oldestPayment
        self.newestPayment = newestPayment
        self.size = size

    def __str__(self):
        toString = ""
        currentPayment = self.oldestPayment

        for i in range(self.size):
            toString += currentPayment.__str__() + " "
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
        self.newestPayment.set_next_payment(self)

        if (PaymentQueue.is_empty(self)):
            self.oldestPayment = self.newestPayment
        else:
            oldNewestPayment.set_next_payment(self.newestPayment)

        self.size += 1
