import time
timestamp = time.strftime('%I:%M:%S %p')
monthstamp = time.strftime('%d/%m/%y %a')
print("Your Day is:-", monthstamp)
print("Your Time is:-", timestamp)
if ('%H' in ['12', '13', '14', '15' ,'16']):
    print("Hello Sir, Good Afternoon")
elif ('%H' in ['17','18','19']):
    print("Hello Sir, Good Evening")
elif ('%H' in ['20','21','22','23','24']):
    print("Hello Sir, Good Night")
else:
    print("Hello Sir, Good Morning")