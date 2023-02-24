# Stores payer name, points available, timestamp, and link to next node
class PaymentNode:
    # Constructor
    def __init__(self, name, points, time_stamp, next_payment=None):
        self.name = name  # Payer's name
        self.points = points  # Points avaialable
        self.time_stamp = time_stamp  # When transaction was made
        self.next_payment = next_payment  # link to next node

    # To string function
    def __str__(self):
        return f"{self.name} - {self.points} ({self.time_stamp})"

    # Accessor function for payer name
    def get_name(self):
        return self.name

    # Accessor function for points available
    def get_points(self):
        return self.points

    # Accessor function for timestamp date
    def get_time_stamp_date(self):
        return self.time_stamp.date()

    # Accessor function for timestamp time
    def get_time_stamp_time(self):
        return self.time_stamp.time()

    # Accessor function for next payment node
    def get_next_payment(self):
        return self.next_payment

    # Mutator function for next payment node
    def set_next_payment(self, new_next_payment=None):
        self.next_payment = new_next_payment

    # Mutator function for removing points from payment node
    def remove_points(self, points_to_remove):
        self.points -= points_to_remove
