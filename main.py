def probability():
    try:
        number_of_days = int(input("Please enter number of Days: "))
    except:
        print("Please enter valid number")

    if number_of_days < 4:
        numerator = 2**(number_of_days-1)
        denominator = 2**number_of_days
    else:
        ways_to_attend_on_day_4 = 2
        ways_to_attend_on_day_3 = 1
        ways_to_attend_on_day_2 = 1
        ways_to_attend_on_day_1 = 4
        total_ways_to_attend = 8
        
        for day in range(4, number_of_days+1):
            temp = ways_to_attend_on_day_2
            ways_to_attend_on_day_2 = ways_to_attend_on_day_3
            ways_to_attend_on_day_3 = ways_to_attend_on_day_4
            ways_to_attend_on_day_4 = ways_to_attend_on_day_1
            ways_to_attend_on_day_1 = total_ways_to_attend
            total_ways_to_attend = (total_ways_to_attend - temp) * 2 + temp
            
        numerator = ways_to_attend_on_day_2 + ways_to_attend_on_day_3 + ways_to_attend_on_day_4
        denominator = total_ways_to_attend
    
    return f"{numerator}/{denominator}"

print(probability())
