# write your code here
import random
print("Enter the number of friends joining (including you):")
n = int(input())
print()
party = {}
if n < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(n):
        name = input()
        party[name] = 0
    print()
    print("Enter the total bill value:")
    bill_one = int(input())
    bill = round(bill_one / n, 2)
    for key in party.keys():
        party[key] = bill
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    ansower = input()
    if ansower == "Yes":
        lucky = random.choice(list(party.keys()))
        print()
        print(f'{lucky} is the lucky one!')
        bill = round(bill_one / (n - 1), 2)
        party[lucky] = 0
        for key in party.keys():
            if key != lucky:
                party[key] = bill
        print()
        print(party)
    else:
        print()
        print("No one is going to be lucky")
        print()
        print(party)


