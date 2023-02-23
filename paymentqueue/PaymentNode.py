from datetime import datetime


class PaymentNode:
    def __init__(self, name, points, time_stamp, next_payment=None):
        self.name = name
        self.points = points
        self.time_stamp = time_stamp
        self.next_payment = next_payment

    def __str__(self):
        return f"{self.name} - {self.points} ({self.time_stamp})"

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_time_stamp(self):
        return self.time_stamp

    def get_next_payment(self):
        return self.get_next_payment

    def set_next_payment(self, new_next_payment):
        self.next_payment = new_next_payment

    def add_points(self, points_to_add):
        self.points += points_to_add

    def remove_points(self, points_to_remove):
        self.points -= points_to_remove
