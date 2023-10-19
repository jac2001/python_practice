
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    valid_date = fix_the_date()
    print(valid_date)
def fix_the_date():
    while True:
        try:
            date = input("Date: ")
            if ("/") in date and (",") not in date:
                date = date.replace(" ", "").split("/")
                month = date[0].zfill(2)
                day = date[1].zfill(2)
                year = date[2]
                if int(day) > 31 or int(month) > 12:
                    date = input("Date: ")
                valid = f"{year}-{month}-{day}"
                return valid

            elif(",") in date and ("/") not in date :

                date = date.replace(",", "").split(" ")
                month_index = months.index(date[0]) + 1

                day = date[1].zfill(2)
                year = date[2]
                if int(day) > 31:
                    date = input("Date: ")
                valid = f"{year}-{month_index:02}-{day}"
                return valid
        except ValueError:
            date = input("Date: ")
        else:
            continue




main()