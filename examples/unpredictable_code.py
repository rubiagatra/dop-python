class Member:
    is_blocked = None

    def display_blocked_status_twice(self):
        is_blocked = self.is_blocked
        print(is_blocked)
        print(is_blocked)
