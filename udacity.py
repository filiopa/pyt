# 1
# Write max 100 characters (counting)
headlines = input('Write your sentence here (max 100 characters): ')
news_ticker = " "
for headline in headlines:
    news_ticker += headline + ""
    if len(news_ticker) >= 100:
        news_ticker = news_ticker[:100]
        break
print(news_ticker)

# 2
# Calculate number of weeks and days left for X days 
days = int(input('Tell me how many days yoy got: '))
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(days))