
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas
import random
import smtplib


def send_wishes():
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = random.choice(letters)
    email_addr = "youremail@gmail.com"
    password = "your app password"
    with open(f"letter_templates/{letter}") as new_letter:
        raw_wish_letter = new_letter.read()
    for index, row in birthday_guys.iterrows():
        name = row["name"]
        email_id = row.email
        final_wish_letter = raw_wish_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(email_addr, password)
            connection.sendmail(from_addr=email_addr, to_addrs=email_id,
                                msg=f"Subject:Happy Birthday\n\n{final_wish_letter}")
    print("Wishes sent successfully")


today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
birthday_guys = data[(data.month == today.month) & (data.day == today.day)]
if not birthday_guys.empty:
    send_wishes()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# jump to send_wishes function definition

# 4. Send the letter generated in step 3 to that person's email address.
##jump to send_wishes function definition line 21