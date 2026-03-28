import calendar
import datetime

def display_months():
    current_year = datetime.datetime.now().year
    
    print(f"Months in the year {current_year}:")
    for month in calendar.month_name[1:]: 
        print(month)

if __name__ == "__main__":
    display_months()