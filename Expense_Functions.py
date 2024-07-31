from Expense_Class import Expense
from tkinter import messagebox 
from datetime import date


def Search_Details(file_path:(__file__), search_by:str, search_value=None):
    track = 0
    Total_Amount,Total_Credit_Amount = 0.0, 0.0
    Tracked_data=''
    expenses:list[Expense]=[]

    with open(file_path, "r") as f:
        lines = f.readlines()[2:]  # Skip the first two lines of the file as they are used for headings

        if len(lines) <= 0:
            messagebox.showerror("Error", "Till Now No data Entered\n Please Enter some data")
            return False
        
        for line in lines:
            if line == '\n': continue
           
            data=[]
            data.extend(line.strip().split(","))
            line_expense = Expense(
                Details=data[6],
                Amount=float(data[3]),
                Category=data[2],
                Type=(True if data[4]=='Credit' else False),
                Date=date(int(data[0].split('-')[2]),int(data[0].split('-')[1]),int(data[0].split('-')[0])),  
             # this is needed to covert because if we are searching by date we need to compare the date
                Remaining_Amount=data[5] 
                # Time=data[1] --------- not needed
            )
            expenses.append(line_expense)

    if search_by == 'Type':
        for expense in expenses:
            if expense.Type == search_value:
                Tracked_data=Tracked_data.__add__(f'{expense.Date} --> {expense.Category}:- {expense.Amount:.2f}.rs "{expense.Type}">\n')
                print(expense)
                if expense.Category != '<-+->': Total_Amount+=expense.Amount
                else: Total_Credit_Amount+=expense.Amount
                track += 1

    elif search_by == 'Category':
        if search_value == 'All':
            for expense in expenses:
                if expense.Category == "<-+->": continue
                Tracked_data=Tracked_data.__add__(f'{expense.Date} --> {expense.Category}:- {expense.Amount:.2f}.rs "{expense.Type}">\n')
                print(expense)
                Total_Amount+=expense.Amount
                track += 1
        else:
            for expense in expenses:
                if expense.Category == search_value:
                    Tracked_data=Tracked_data.__add__(f'{expense.Date} --> {expense.Category}:- {expense.Amount:.2f}.rs "{expense.Type}">\n')
                    print(expense)
                    Total_Amount+=expense.Amount
                    track += 1
 
    elif search_by == 'Date':
        to_date = date(int(search_value[1].split('-')[2]),int(search_value[1].split('-')[1]),int(search_value[1].split('-')[0]))
        from_date = date(int(search_value[0].split('-')[2]),int(search_value[0].split('-')[1]),int(search_value[0].split('-')[0]))
        
        for expense in expenses:
            if (from_date <= expense.Date <= to_date) and expense.Category != "<-+->":
                Tracked_data=Tracked_data.__add__(f'{expense.Date} --> {expense.Category}:- {expense.Amount:.2f}.rs "{expense.Type}">\n')
                print(expense)
                Total_Amount+=expense.Amount
                track += 1
            if (from_date <= expense.Date <= to_date) and expense.Category == "<-+->":
                Tracked_data=Tracked_data.__add__(f'{expense.Date} --> {expense.Category}:- {expense.Amount:.2f}.rs "{expense.Type}">\n')
                print(expense)
                Total_Credit_Amount+=expense.Amount
            

    if track == 0:
        messagebox.showwarning("Error", "No data found matching the search criteria")
        return False   
    print(Tracked_data)
    messagebox.showinfo('Details', f'{Tracked_data}\nTotal Expencese : {Total_Amount}.rs\nTotal Credit : {Total_Credit_Amount}.rs')
    return True


def Save_Details( file_path:(__file__), amount:float, category = None, details = None, date = None ):
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please fill in all the fields")
        return False
    
    if amount <= 0 :
        messagebox.showerror("Error", "Expense amount should be greater than 0")
        return False
    
    with open(file_path, "r") as f:# Read the contents of the file and skip the first two lines as they are used for headings
        contents = f.readlines()[2:]

        if len(contents)<=0:
            remaining_amount=0.0
        else:
            contents=(contents[-1]).split(",")
            remaining_amount=float(contents[5])
   
    if category is not None:
        expense = Expense(
            Details = details, Category = category, Amount = amount, Type = False, Remaining_Amount = (remaining_amount - amount), Date = date
        )
    else:   
        expense = Expense(
            Details = details, Category = "<-+->", Amount = amount, Type = True, Remaining_Amount = (remaining_amount + amount), Date = date
        )

    with open(file_path, "a") as f:
        f.write(f"{expense.Date},{expense.Time},{expense.Category},{expense.Amount},{expense.Type},{expense.Remaining_Amount},{expense.Details}\n")
    
    messagebox.showinfo("Success", "Data saved successfully")
    return True


# Main() function------- For testing purpose  
if __name__ == '__main__':
    Search_Details('expenses.csv', 'Category', 'Market' )