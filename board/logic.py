numbers = [
    '00', 
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
    '31', '32', '33', '34', '35', '36',
    '00'
]

def is_red(number) -> bool:
    return True if number % 2 != 0 and number not in [0, 37] else False

def is_black(number) -> bool:
    return True if number % 2 == 0 and number not in [0, 37] else False

def is_green(number) -> bool:
    return True if number in [0, 37] else False