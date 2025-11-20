class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount

        self._transactions: list[int] = []

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str:
        if type(amount) != int:
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        for t in self._transactions:
            yield t

    def __getitem__(self, i: int):
        return self._transactions[i]

    def __reversed__(self):
        return self._transactions[::-1]

    def __eq__(self, other: "Account"):
        return self.balance == other.balance

    def __lt__(self, other: "Account"):
        return self.balance < other.balance

    def __le__(self, other: "Account"):
        return self.balance <= other.balance

    def __add__(self, other: "Account") -> "Account":
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions

        return new_account