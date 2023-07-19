def calculate_stardate(year, month, day):
    # Step 1: Define constants
    STARDATE_BASE = 2005
    STARDATE_YEAR = 0.00
    EARTH_YEAR = 365

    # Step 2: Determine if it's a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        n = 366  # Leap year
    else:
        n = 365  # Non-leap year

    # Step 4: Calculate the "month number"
    month_numbers = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if month > 2 and n == 366:
        m = month_numbers[month - 1] + 1
    else:
        m = month_numbers[month - 1]

    # Step 5: Determine the day and year
    d = day
    y = year

    # Step 6: Calculate the stardate
    stardate = STARDATE_YEAR + (1000 * (y - STARDATE_BASE)) + ((1000 / n) * (m + d - 1))
    stardate = round(stardate, 2)

    return stardate


# Example usage:
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))

stardate = calculate_stardate(year, month, day)
print("Stardate:", stardate)
