import time as t


class Expense:
    Time = t.strftime("%I:%M:%S_%p")

    def __init__(self, Amount:float, Type:bool, Category, Details = None, Remaining_Amount:float = None,Date = None) -> None:
        self.Details = Details
        self.Category = Category
        self.Amount= Amount
        self.Type = 'Credit' if Type else 'Debit'
        self.Remaining_Amount=Remaining_Amount
        self.Date = Date

        self.Time = Expense.Time

    def __repr__(self):
        return f"<Details:-----\n  \t  {self.Date} --> {self.Category}:- {self.Amount:.2f}.rs ,'{self.Type}'>\n"


# Main() function------- For testing purpose  
if __name__ == '__main__':
    Test = Expense(100.0, False, 'Food', 'Biryani' )
    print(Test)
    print(Test.Time)
    print(Test.Category)
    print(Test.Amount)
    print(Test.Type)
    print(Test.Remaining_Amount)
    print(Test.Date)
    print(Test.Details)




