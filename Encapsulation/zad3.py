class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        if 5 <= len(username) <= 15:
            self.__username = username
            return

        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        upper_present = False
        digit_present = False
        if 8 <= len(password):
            for c in password:
                if c.isdigit():
                    digit_present = True

                if c.isupper():
                    upper_present = True

            if upper_present and digit_present:
                self.__password = password
                return

        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'