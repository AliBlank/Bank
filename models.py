from database import*
import hashlib


class User:

    def __init__(self, first_name, last_name, age, gender,password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.password = password

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def user_information(self):
        print(f'User Information')
        print('-'*20)
        print(f'{self.full_name}\nAge: {self.age}\nGender: {self.gender}')



class Bank(User):

    def __init__(self, first_name, last_name, age, gender,password):
        super().__init__(first_name, last_name, age, gender,password)
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You have withdrawn {amount} Now balance is {self.balance} ')
            try:
                myCursor.execute("""
                    UPDATE user_bank SET balance = ? WHERE first_name = ? AND last_name = ?
                """, (self.balance, self.first_name, self.last_name))
                mydb.commit()
            except sqlite3.Error as e:
                print(f"something went wrong: {e}")
        else:
            print("You don't have enough money!")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposited {amount} Now You Have {self.balance}')

        try:
            myCursor.execute("""
                UPDATE user_bank SET balance = ? WHERE first_name = ? AND last_name = ?
            """,(self.balance, self.first_name, self.last_name))
            mydb.commit()
        except sqlite3.Error as e:
            print(f"something went wrong: {e}")

    def bank_balance(self):
        print(f'{self.full_name} your bank balance is: {self.balance}')



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validate_input(prompt, err_message, condition):
    while True:
        user_input = input(prompt).strip().lower()
        if condition(user_input):
            return user_input
        print(err_message)


def is_valid_name(name):
    return name.isalpha()

def is_valid_number(number):
    try:
        float(number)
        return float(number)
    except ValueError:
        return False

def is_valid_password(password):
    return password and " " in password or password == ""
