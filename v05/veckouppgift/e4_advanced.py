import math, datetime

"""
1
Det är ca 470 km mellan Stockholm och Göteborg. 
Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. 
Du behöver fråga användaren hur fort man ska köra, i km/h.
"""
distance = 470

try: 
    speed = int(input("What speed, in km/h, do you want to travel between Goteborg and Stockholm? >> "))
    
    print(f"The journey will take {(distance / speed):.1f} hour{ 's' if (distance / speed) > 1 else ''}.")
    print(f"The journey will take {((distance / speed)*60*60):.0f} seconds.")
    print(f"The journey will take {((distance / speed)*60):.0f} minutes.")
    
    train_seconds = int((distance / speed) *60 *60)
    train_hours = train_seconds // (60*60)
    train_min = math.ceil((train_seconds % (60*60)) / 60)
        
    print(f"The journey will take {train_hours} hour{ '' if train_hours == 1 else 's'} and {train_min} minute{ 's' if train_min != 1 else ''}.")
    
except:
    print("Sorry the train got stuck")
    
    
"""
2
Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. 
Användaren behöver skriva in längden på de två kortare sidorna.
"""
print("""
              +
              | \\  Side X
       Side A |  \\
              +---+
              Side B
      """)

try:
    side_a = int(input("What is the length of side A? >> "))
    side_b = int(input("What is the length of side B? >> "))
    
    side_x = math.sqrt(side_a * side_a + side_b * side_b)
    
except:
    print("Sorry that is an square")
    
else:
    print(f"Side X is of lenght: {side_x:.1f}.")
    
finally:
    pass
    
"""
3A
Skriv ett program som talar om dagens datum.
"""

date_format = "%Y%b%d"

days_ahead = 7

date_today = datetime.datetime.today()
date_next_week = (datetime.datetime.strptime(date_today.strftime(date_format), date_format) + datetime.timedelta(days=days_ahead))

print(f"\nTodays date: {date_today.strftime(date_format)}")
print(f"In {days_ahead} days the date will be: {date_next_week.strftime(date_format)}.")

