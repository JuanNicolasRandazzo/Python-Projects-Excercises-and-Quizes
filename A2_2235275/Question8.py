"""
    Topic: Question8
    Date: 06 Oct 2023
    Author: Juan Nicolas Randazzo

"""

print("Input birthday: " , end=" ")
input_birthday = int(input())
print("Input month of birth: ", end=" ")
input_month_birth = input()
print(f"Birthdate: {input_birthday}/{input_month_birth}")
list_birthdate = [input_birthday,input_month_birth]

months_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]




if (input_month_birth in months_list):
    
    if(input_birthday >= 1 and input_birthday <=31):
        if (( input_month_birth == months_list[2] and input_birthday >= 21) or ( input_month_birth == months_list[3] and input_birthday <= 19)):
            print("Aries")
        elif (( input_month_birth == months_list[3] and input_birthday >= 20) or ( input_month_birth == months_list[4] and input_birthday <= 20)):
            print("Taurus")
        elif (( input_month_birth == months_list[4] and input_birthday >= 21) or ( input_month_birth == months_list[5] and input_birthday <= 20)):
            print("Gemini")
        elif (( input_month_birth == months_list[5] and input_birthday >= 21) or ( input_month_birth == months_list[6] and input_birthday <= 22)):
            print("Cancer")
        elif (( input_month_birth == months_list[6] and input_birthday >= 23) or ( input_month_birth == months_list[7] and input_birthday <= 22)):
            print("Leo")
        elif (( input_month_birth == months_list[7] and input_birthday >= 23) or ( input_month_birth == months_list[8] and input_birthday <= 22)):
            print("Virgo")
        elif (( input_month_birth == months_list[8] and input_birthday >= 23) or ( input_month_birth == months_list[9] and input_birthday <= 22)):
            print("Libra")
        elif (( input_month_birth == months_list[9] and input_birthday >= 23) or ( input_month_birth == months_list[10] and input_birthday <= 21)):
            print("Scorpio")
        elif (( input_month_birth == months_list[10] and input_birthday >= 22) or ( input_month_birth == months_list[11] and input_birthday <= 21)):
            print("Sagittarius")
        elif (( input_month_birth == months_list[11] and input_birthday >= 22) or ( input_month_birth == months_list[0] and input_birthday <= 19)):
            print("Capricorn")
        elif (( input_month_birth == months_list[0] and input_birthday >= 20) or ( input_month_birth == months_list[1] and input_birthday <= 18)):
            print("Aquarius")    
        elif (( input_month_birth == months_list[1] and input_birthday >= 19) or ( input_month_birth == months_list[2] and input_birthday <= 20)):
            print("Pisces")
        
        else:
            print("Day doesn't correspond to any sodiacal sign")
    else:
        print(" Invalid day")
else:
    print(" Invalid month")
    















            
        
"""
if ((list_birthdate[1] == "Dec" or list_birthdate[1] == "Jan") and list_birthdate[0]>= 19):
    print("Capricorn")
elif ((list_birthdate[1] == "Jan" or list_birthdate[1] == "Feb") and list_birthdate[0]>= 18):
    print("Aquarius")
elif (list_birthdate[0]>= 19 and (list_birthdate[1] == "Feb" or list_birthdate[1] == "Mar")):
    print("Pisces")
elif (list_birthdate[0]> 19 and (list_birthdate[1] == "Apr" or list_birthdate[1] == "May")):
    print("Taurus")

"""
