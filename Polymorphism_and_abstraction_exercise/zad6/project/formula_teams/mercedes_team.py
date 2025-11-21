from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200000
    PETRONAS_SPONSOR_MONEY = {
        1: 1000000,
        3: 500000
    }
    TEAMVIEWER_SPONSOR_MONEY = {
        5: 100000,
        7: 50000
    }

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        petronas_money = self.find_money(self.PETRONAS_SPONSOR_MONEY, race_pos)
        teamviewer_money = self.find_money(self.TEAMVIEWER_SPONSOR_MONEY, race_pos)

        revenue = petronas_money + teamviewer_money - self.EXPENSES_PER_RACE
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def find_money(mapping: dict[int, int], race_pos: int) -> int:
        for key in mapping.keys():
            if key >= race_pos:
                return mapping[key]
        return 0