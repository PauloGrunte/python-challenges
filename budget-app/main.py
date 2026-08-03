class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = '' 
        quantityAsterisk = (30 - (len(self.name)))
        message = ''
        for i in range(quantityAsterisk // 2):
            title += '*'
        title += self.name
        for i in range(quantityAsterisk - (quantityAsterisk // 2)):
            title += '*'           
        for activity in self.ledger:
            value = list(activity.values())[0]
            description = list(activity.values())[1]
            message += f"{description[:23]:<23}{value:>7.2f}\n"
            
        return f'{title}\n{message}Total: {self.get_balance():.2f}'

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = 0
        for v in self.ledger:
            balance += (next(iter(v.values())))
        return balance

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
            if not self.check_funds(amount=amount):
                return False
            self.ledger.append({'amount': -amount, 'description': description})
            return True

    def transfer(self, amount, otherCategory):
            if not self.check_funds(amount=amount):
                return False  
            self.withdraw(amount=amount, description=f'Transfer to {otherCategory.name}')
            otherCategory.deposit(amount=amount, description=f'Transfer from {self.name}')
            return True
        
def sum_spend(categories=[]):
    totalWithdraw = 0
    for category in categories:
        for v in category.ledger:
            value = (next(iter(v.values())))
            if value < 0:
                totalWithdraw += value
    return totalWithdraw

def sum_spend_category(category):
    totalSpendCategory = 0
    for v in category.ledger:
        value = (next(iter(v.values())))
        if value < 0:
            totalSpendCategory += value
    return totalSpendCategory

def sum_percent_spend(categorySpend, totalWithdraw):
    if totalWithdraw == 0:
        return 0
    percent = (categorySpend / totalWithdraw) * 100
    return int(percent) // 10 * 10

def create_spend_chart(categories=[]):
    totalWithdraw = sum_spend(categories)
    percentages = []
    
    for category in categories:
        cat_spend = sum_spend_category(category)
        percentages.append(sum_percent_spend(cat_spend, totalWithdraw))

    chart = 'Percentage spent by category\n'
    
    for y in range(100, -1, -10):
        chart += f"{y:3}| "
        for percent in percentages:
            if percent >= y:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    dash = "-" * (len(categories) * 3 + 1)
    chart += f"    {dash}\n"
    
    names = [c.name for c in categories]
    max_len = max(len(nome) for nome in names)
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += f"{name[i]}  "
            else:
                chart += "   "
                
        if i < max_len - 1:
            chart += "\n"
            
    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.50, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55, 'shirt')

auto = Category('Auto')
auto.deposit(1000, 'initial')
auto.withdraw(15, 'gas')

print(create_spend_chart([food, clothing, auto]))