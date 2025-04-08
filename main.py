from database import *
from models import User, Bank, hash_password, validate_input, is_valid_name, is_valid_number

first_name = validate_input(
    'Enter Your FirstName :',
    'Please enter a valid first name (letters only, no spaces) ',
    is_valid_name)

last_name = validate_input(
    'Enter your last name: ',
'Please enter a valid last name (letters only, no spaces) ',is_valid_name)

password = hash_password(input('Enter your password: '))


while True:
    try:
        myCursor.execute("""
        SELECT age,gender,balance FROM user_bank WHERE first_name = ? AND last_name = ? AND password = ?
            """, (first_name, last_name, password))
        result = myCursor.fetchone()
        if result:
            age, gender, balance = result
            user = Bank(first_name, last_name, age, gender, password)
            user.balance = balance
            print(f'welcome back {user.full_name}!')
            break

        else:
            myCursor.execute("""
                SELECT * FROM user_bank WHERE first_name = ? AND last_name = ?
            """, (first_name, last_name))
            user_exist = myCursor.fetchone()
            if user_exist:
                print(f'password is incorrect')
                password = hash_password(input('Enter your password: '))
            else:
                age = int(input('Enter your age: '))
                gender = input('Enter your gender: ')
                user = Bank(first_name, last_name, age, gender,password)
                user.user_information()
                try:
                    myCursor.execute("""INSERT INTO user_bank (first_name, last_name, age, gender, balance, password) 
                                VALUES (?, ?, ?, ?, ?, ?)""",
                                (user.first_name, user.last_name, user.age, user.gender, user.balance, user.password))
                    mydb.commit()
                    break
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
                    break

    except sqlite3.Error as e :
        print(f'something went wrong: {e}')

    print('-'*50)
while True:
    bank_actions = input('What would you like to do?\n1.Bank Balance\n2.Deposit\n3.Withdraw\nchoose :')
    if bank_actions == '1':
        user.bank_balance()
    elif bank_actions == '2':

            bank_deposit = float(validate_input(
                'How much do you want to deposit?',
            'Enter Number Only',
                        is_valid_number))
            user.deposit(bank_deposit)


    elif bank_actions == '3':
        try:
            bank_withdraw = float(validate_input(
                'How much do you want to withdraw?',
                'Enter Number Only',
                is_valid_number
            ))
            user.withdraw(bank_withdraw)
        except ValueError:
            print('Please enter a valid input')
    else:
        print('Please enter a valid input( 1 , 2 , 3 )')

    try:
        continue_program = input('Do you want to continue? (y/n)')
        if continue_program == 'n':
            print('Thank You!')
            break
    except ValueError:
        print('Please enter a valid input( y / n )')



mydb.close()


