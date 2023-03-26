
def is_magic_date(day,month,year):
    prod = day*month
    last_two_digits = year%100
    if prod == last_two_digits:
        return True
    else:
        return False
print(is_magic_date(10,6,1960))
