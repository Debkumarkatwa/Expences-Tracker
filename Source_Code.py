from Expense_Functions import Save_Details , Search_Details
from ttkbootstrap import *
from tkinter import messagebox 


def Credit():

    global top_win  # createing a new window
    top_win = Toplevel(win, position=(400,150))
    top_win.title('Save Credit')
    top_win.geometry('350x180')
    top_win.resizable(False, False)

    # Creating a label and a Entrybox for Date
    Label(top_win, text=' Date -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=10).grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    Variable0=DateEntry(top_win, bootstyle='success')
    Variable0.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    
    # Creating a label and a Entrybox for Amount
    Label(top_win, text=' Amount -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=10).grid(row=1,column=0,padx=5,pady=5, sticky='w')
    
    Variable1=Spinbox(top_win, from_=0, to=float('inf'), bootstyle='success', width=21)
    Variable1.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    # Creating a label and a Entrybox for Details
    Label(top_win, text=' Details -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=10).grid(row=2,column=0,padx=5,pady=5, sticky='w')
    
    Variable2=Entry(top_win, bootstyle='success', width=25) 
    Variable2.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    
    # Creating a Button for saving the details
    
    a=Button(top_win, text='Save', command=lambda:Save_Details(file_path=expense_file_path, date=Variable0.entry.get(), amount=Variable1.get(), details=Variable2.get()), width=10)
    a.grid(row=3, column=1, padx=5, pady=5)
    
    top_win.mainloop()


def Debit():
    
    global top_win # createing a new window
    top_win = Toplevel(win,position=(400,150))
    top_win.title('Save Debit')
    top_win.geometry('350x200')
    top_win.resizable(False, False)

    # Creating a label and a Entrybox for Date
    Label(top_win, text=' Date -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    Variable0=DateEntry(top_win, bootstyle='success')
    Variable0.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    
    # Creating a label and a Entrybox for Category
    Label(top_win, text='Category -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=1, column=0, padx=5, pady=5, sticky='w')
    
    Variable1=Combobox(top_win, values=['Food', 'Market', 'Home', 'Others'], state='readonly', bootstyle='success', width=23)
    Variable1.grid(row=1, column=1, pady=5)
    Variable1.set('Food')
    
    # Creating a label and a Entrybox for Amount
    Label(top_win, text=' Amount -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=2,column=0,padx=5,pady=5, sticky='w')
    
    Variable2=Spinbox(top_win, from_=0, to=float('inf'), bootstyle='success', width=21)
    Variable2.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    # Creating a label and a Entrybox for Details
    Label(top_win, text=' Details -- ', border=5, relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=3,column=0,padx=5,pady=5, sticky='w')
    
    Variable3=Entry(top_win, bootstyle='success', width=25) 
    Variable3.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    
    # Creating a Button for saving the details
    a=Button(top_win, text='Save', command=lambda:Save_Details(file_path=expense_file_path, date=Variable0.entry.get(), category=Variable1.get(), amount=Variable2.get(), details=Variable3.get()), width=10)
    a.grid(row=4, column=1, padx=5, pady=5)
    top_win.mainloop()


def Search(search_by):
    # print('Search by',search_by)
    global top_win   # createing a new window
    top_win = Toplevel(win,position=(400,150))
    top_win.title('Search Details')
    top_win.geometry('350x180')
    top_win.resizable(False, False)

    Label(top_win, text=f'       -- Search By {search_by} --', border=5,relief='sunken', font=('Imprint MT Shadow', 15, 'bold'), width=28).grid(row=0, column=0, padx=5, pady=5, columnspan=4)

    if search_by == 'Type':
        Label(top_win, text=f' Select Type --', border=5,relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=13).grid(row=1, column=1, padx=5, pady=5, sticky='e')
        Variable0=Combobox(top_win, values=['Credit', 'Debit'], state='readonly', bootstyle='warning')
        Variable0.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        Variable0.set('Credit')
        
    elif search_by == 'Category':
        Label(top_win, text=f' Select Category --', border=5,relief='sunken', font=('Imprint MT Shadow', 10, 'bold'), width=15).grid(row=1, column=1, padx=5, pady=5, sticky='e')
        Variable0=Combobox(top_win, values=['All', 'Food', 'Market', 'Home', 'Others'], state='readonly', bootstyle='success', width=23)
        Variable0.grid(row=1, column=2, padx=5, pady=5, sticky='e')
        Variable0.set('All')

    elif search_by=='Date':
        Label(top_win, text=f' Date From --', border=5,relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=1, column=1, padx=5, pady=5, sticky='e')
        Var0=DateEntry(top_win, bootstyle='warning')
        Var0.grid(row=1, column=2, padx=5, pady=5, sticky='w')

        Label(top_win, text=f' Date To --', border=5,relief='sunken', font=('Imprint MT Shadow', 12, 'bold'), width=12).grid(row=2, column=1, padx=5, pady=5, sticky='e')
        Var1=DateEntry(top_win, bootstyle='warning')
        Var1.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        
    Button(top_win, text='Search', command= lambda:Search_Details(expense_file_path, search_by, [Var0.entry.get(), Var1.entry.get()] if search_by=='Date' else Variable0.get() ), width=12).grid(row=3, column=2, padx=5, pady=5) 

    top_win.mainloop()


# main() function ------------------------------------------------------------------------

# Create a new window
win = Window(themename='solar',position=(50,50))
win.title('Expense Tracker')
win.geometry('480x300')
win.resizable(False, False)

# path of the file used to store the details
global expense_file_path
expense_file_path = 'Expense_Details.csv'  
with open('Expense_Details.csv', 'w+') as file: # create a file if not exists and write the header
    if file.read() == '':
        file.write(' --Date--, --Time--, --Category--, --Amount--,  --Type--, --Remaining Amount--, --Details--\n\n')



# Create a intro frame and label
frame1=Frame(win, relief='groove', border=5, borderwidth=8,bootstyle='light')
frame1.pack(padx=5, pady=5, fill='x')

Label(frame1, text='       Welcome to The Application ', border=10, relief='sunken', foreground='white', background='black', font=('Imprint MT Shadow', 18, 'bold')).pack(fill='x')

# Create a frame and label for selecting the type of expense
frame2=Frame(win, relief='groove', border=2, borderwidth=10,bootstyle='dark')
frame2.pack(padx=18, fill='x')
frame2.grid_anchor('center')

Label(frame2, text=' -- Select the Type of Transaction -- ', foreground='white',border=5, font=('Imprint MT Shadow', 15, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=2)

# Create frame and buttons for credit and debit
frame_1=Frame(frame2,bootstyle='warning',border=5,relief='sunken')
frame_1.grid(row=1,column=1)
frame_2=Frame(frame2,bootstyle='warning',border=5,relief='sunken')
frame_2.grid(row=1,column=2)

Button(frame_1, text=' Credit ', cursor='hand2', command=Credit, bootstyle='outline-success', width=12).grid(row=1, column=1)
Button(frame_2, text=' Debit ', cursor='hand2', command=Debit, bootstyle='outline-success', width=12).grid(row=1, column=2)

# Create frame, labels, button for searching the details
frame3=Frame(win, border=2, borderwidth=5, relief='sunken', bootstyle='dark')
frame3.pack(padx=18, fill='x')
frame3.grid_anchor('center')

Label(frame3, text=' -- Want to Know Your Previous Expences -- ', foreground='white', font=('Imprint MT Shadow', 12, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=2)
Label(frame3, text='  Search by --', font=('Imprint MT Shadow', 12, 'bold')).grid(row=1, column=1, padx=5, pady=2, sticky='e')

Var=Combobox(frame3, values=['Category', 'Date', 'Type'], state=READONLY, bootstyle='warning', font=('Imprint MT Shadow', 10, 'bold'),foreground='white')
Var.grid(row=1, column=2, padx=5, pady=2, sticky='w')
Var.set('Category')

Button(frame3, text='Show Details', command=lambda:Search(Var.get())).grid(row=2, column=2, padx=5, pady=5)

# Run the main loop
win.mainloop()

