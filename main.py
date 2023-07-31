import smtplib
import random
import datetime as dt
now = dt.datetime.now()





today_tuple = (now.month, now.day)



import pandas
data = pandas.read_csv(r"Pycharm projects/birthday-wisher-normal-start/birthdays.csv")


my_email = "Your email"
my_password = "Your password"

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}



if today_tuple in birthday_dict:
    birthday = birthday_dict[today_tuple]
    file_path = f"birthday-wisher-normal-start/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as text:
        the_text = text.read()
        the_text = the_text.replace("[NAME]", birthday["name"])



    with smtplib.SMTP("smtp.gmail.com") as coneection:
        coneection.starttls()
        coneection.login(user=my_email, password=my_password)
        coneection.sendmail(from_addr=my_email,
                            to_addrs=birthday["email"],
                            msg=f"subject:Happy Birthday\n\n{the_text}"
    )


