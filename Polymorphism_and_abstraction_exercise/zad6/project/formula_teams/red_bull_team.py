from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250000
    ORACLE_SPONSOR_MONEY = {
        1: 1500000,
        2: 800000
    }
    HONDA_SPONSOR_MONEY = {
        8: 20000,
        10: 10000
    }

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        oracle_money = self.find_money(self.ORACLE_SPONSOR_MONEY, race_pos)
        honda_money = self.find_money(self.HONDA_SPONSOR_MONEY, race_pos)

        revenue = oracle_money + honda_money - self.EXPENSES_PER_RACE
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def find_money(mapping: dict[int, int], race_pos: int) -> int:
        for key in mapping.keys():
            if key >= race_pos:
                return mapping[key]
        return 0