import re

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_chinese_id_card(id_card):

    pattern_18 = r'^[1-9]\d{5}(19\d{2}|20[0-2]\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$'

    if not re.match(pattern_18, id_card):
        return False

    year = int(id_card[6:10])
    month = int(id_card[10:12])
    day = int(id_card[12:14])

    if month > 12 or day > 31:
        return False

    days_in_2 = 29 if is_leap_year(year) else 28

    if (month == 2 and day > days_in_2) or \
       (month in [4, 6, 9, 11] and day > 30) or \
       (day > 31):
        return False

    return True

valid_id_number = "440308199901012345"  
invalid_id_number = "440308199902290123" 

print(validate_chinese_id_card(valid_id_number)) 
print(validate_chinese_id_card(invalid_id_number)) 
