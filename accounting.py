melon_cost = 1.00
def check_melon_payment(payment_file):
    file = open("customer-orders.txt")
    for line in file:
        line = line.rstrip()
        words = line.split('|')
        customer_name = words[1]
        customer_melons = float(words[2])
        customer_paid = float(words[3])
        cost = melon_cost * customer_melons
        if cost < customer_paid:
            print(f'{customer_name} paid {customer_paid}, expected {cost}')
            print(f'{customer_name} has overpaid for their melons.')
        elif cost > customer_paid:
            print(f'{customer_name} paid {customer_paid}, expected {cost}')
            print(f'{customer_name} has underpaid for their melons.')
    file.close()
check_melon_payment('customer-orders.txt')

            



    
