#Write a program that takes as input an amount of currency (a float) and an exchange rate to another currency
#(a float) and prints out the value of the original amount in the other currency. For the exchange rate, pick
#two currencies and use today’s exchange rate.

#USD   ---> EuRO

def usd_to_euro():
    usd_to_euro_rate = 0.9209

    user_input = float(input("What is the USD amount? "))
    if user_input <= 0:
        return("Please try again!")
    elif user_input > 0:
        return(user_input * usd_to_euro_rate)

print(usd_to_euro())
