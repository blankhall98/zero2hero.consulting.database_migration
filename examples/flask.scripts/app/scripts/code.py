class Manager:

    def __init__(self):
        self.data = {}

    def calculate_CI(self,initial_investment,rate_of_return,years):
        return initial_investment*(1+rate_of_return/100)**years