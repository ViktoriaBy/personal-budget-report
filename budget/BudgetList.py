from . import Expense
import matplotlib.pyplot as plt

# Class and constructor
class BudgetList:  
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

#Define the append method
# Add items to overages that are over & under budget
    def append(self, item):
            if self.sum_expenses + item < self.budget:
                self.expenses.append(item)
                self.sum_expenses += item
            else:
                self.overages.append(item)
                self.sum_overages += item

# Define the __len__() method
    def __len__(self):
        return self.expenses.__len__() + self.overages.__len__()

# Create the __iter__() method
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

# Create next()
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()
            


# Define the main function
def main():
    myBudgetList = BudgetList(1200)

# Read in the spending data file
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

# Add the expenses to the BudgetList
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

# Print the Length of myBudgetList
    print('The count of all expenses: '+ str(len(myBudgetList)))
    for entry in myBudgetList:
        print(entry)

    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green', 'red', 'blue'])

    ax.set_title('Your total expenses vs. total budget')
    plt.show()

# Tell Python to run the main function
if __name__ == "__main__":
    main()



            
