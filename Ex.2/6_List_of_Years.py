def list_years(dates):
    years = [d[0] for d in dates]
    years.sort()
    return years

# Example Usage:
# (year, month, day)
date1 = (2019, 2, 3)
date2 = (2006, 10, 10)
date3 = (1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)
