import datetime

VERSION="0.0.1"

def configure():
    # When run, this will automatically ask us to configure a plan
    # For now, we assume that it will be a 2-week plan
    
    # Default date
    start_date = datetime.datetime.now()
    # Get user input
    year = int(input("Enter the year to start (default is current year): "))
    month = int(input("Enter the month to start (default is current month): "))
    day = int(input("Enter the day to start (default is current day): "))
    # Convert this all to a date
    start_date = datetime.date(year, month, day)
    
    generate_plan(start_date)
    
def get_day(date):
    # Return the name of the day of a given date.
    return date.strftime("%A")
    
def generate_plan(start_date):
    # Generate the plan as a plain txt file
    # LAYOUT EXAMPLE:
    # [ ] DD/MM/YYYY (MONDAY)
    # [ ] DD/MM/YYYY (TUESDAY)
    # ...
    
    # Plan length in days
    plan_length = 14
    date = start_date
    filename = date.strftime("%d-%m-%y") + "-2week-plan.txt"
    file = open(filename, "x")
    file.close()
    file = open(filename, "a")
    file.write("WORKOUT PLAN\n" +
                "(have to write this manually for now)\n\n" +
                "CHECKLIST\n"
                )
    for day in range(0, plan_length):
        file = open(filename, "a")
        file.write("[ ] " +
            date.strftime("%d/%m/%Y ") +
            "(" + get_day(date) + ")\n"
            )
        file.close()
        date += datetime.timedelta(days=1)

configure()