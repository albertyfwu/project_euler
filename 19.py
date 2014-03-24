# each year has either 365 or 366 days.
# 365 % 7 = 1 and 366 % 7 = 2
# this means 1 Jan 1901 was a Tuesday (1900 had 365 days)

def num_days_in_month_year(month, year):
	if month == 1:
		if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
			return 29
		else:
			return 28
	return [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]

sundays = 0
day_of_week = 2 # Tuesday
for year in range(1901, 2001):
	for month in range(0, 12):
		# for each month, see if the first day is a Sunday
		if day_of_week == 0:
			sundays += 1

		# compute the next month's 1st date
		num_days = num_days_in_month_year(month, year)
		day_of_week = (day_of_week + num_days) % 7

print sundays
