# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def percent_doun(money, persent):
    return money - (money * persent)

def capitalization(money, persent):
    return money + (money * persent)


class BankAccount:
    def __init__(self, id_client: int, name: str):
        self.client_money = 0.0
        self.id_client = id_client
        self.__count_operation = 0
        self.name = name

    def money_up(self, up: int):
        if self.client_money > 5000000:
            self.client_money = percent_doun(self.client_money, 0.1)
        if up % 50 == 0:
            self.client_money += up
            self.__count_operation +=1
        if self.__count_operation > 2:
            self.client_money = capitalization(self.client_money, 0.03)
            self.__count_operation = 0
        print(self.client_money)

    def money_down(self, down: int):
        if self.client_money > 5000000:
            self.client_money = percent_doun(self.client_money, 0.1)
        if down * 0.15 < 30:
            down_money = down + 30
        elif down * 0.15 > 600:
            down_money = down + 600
        else:
            down_money = capitalization(down, 0.15)
        
        if self.client_money >= down_money:
            self.client_money -= down_money
            self.__count_operation += 1
        else:
            print('недостаточно средств')
        if self.__count_operation > 2:
            self.client_money = capitalization(self.client_money, 0.03)
            self.__count_operation = 0
        print(self.client_money)

    def __str__(self):
        return f'Баланс лицевого счета {self.client_money}'

client_1 = BankAccount(111111, 'Петров Петр')
while True:
    choice_operator = int(input('Выберите необходимое действие:\n'\
                                '1 - Пополнить лицевой счет\n'\
                                '2 - Снять деньги\n'\
                                '3 - закончить обслуживание и выйти \n'))
    if choice_operator == 1:
        mon = int(input('Какую сумму зачислить на счет - '))
        client_1.money_up(mon)
    elif choice_operator == 2:
        mon = int(input('Какую сумму снять со счета - '))
        client_1.money_down(mon)
    elif choice_operator == 3:
        exit()
    else:
        print(client_1)