#sort a list of data provided  in day month year format chronologically 
#input:
#an integer n(1<n<100)
#a list of n strings  in date month year format 
#output:
#sorted list of dates (earliest to latest)
#example
#input["12-05-2025","01-01-2022","15-06-2023"]
#output["01-01-2022","15-06-2023","12-05-2025"]


from datetime import datetime

def sort_dates(dates):
    return sorted(dates, key=lambda x: datetime.strptime(x, "%d-%m-%Y"))

# Test
dates = ["12-05-2025", "01-01-2022", "15-06-2023"]
print(sort_dates(dates))






####
def sort_dates(dates):
    dates.sort(key=lambda x: x.split('-')[2] + x.split('-')[1] + x.split('-')[0])
    return dates

# Test with mixed year formats
dates = ["12-05-25", "01-01-2022", "15-06-23", "20-12-2024"]
print(sort_dates(dates))


#####
def sort_dates(dates):
    def get_sort_key(date):
        day, month, year = date.split('-')
        # Convert 2-digit year to 4-digit (assuming 20xx)
        if len(year) == 2:
            year = '20' + year
        return year + month + day
    
    dates.sort(key=get_sort_key)
    return dates

# Test with mixed year formats
dates = ['01-01-2022', '20-12-2024', '15-06-23', '12-05-25']
print(sort_dates(dates))





