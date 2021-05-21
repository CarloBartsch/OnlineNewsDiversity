#Wenn Ordner-Datum kleiner als heutiges Datum, dann
import time
from datetime import date
today = date.today()
print(today)
year = int(time.strftime('%Y'))
month = int(time.strftime('%m'))
day = int(time.strftime('%d'))
print(year)
print(month)
print(day)

import os
import datetime
import smtplib

EMAIL_ADRESS = 'carbinowitz@gmail.com'
EMAIL_PASSWORD = 'divfwwbzsspzdncn'

def filter_by_date(src_folder, archive_date):
    os.chdir(src_folder)
    return [
        name for name in os.listdir('.')
        if os.path.isdir(name)
        and datetime.datetime.fromtimestamp(os.path.getmtime(name)) < archive_date
    ]


if __name__ == '__main__':
    output = filter_by_date(r"C:\Users\admin\Documents\Dissertation\Diversity of News\Files", datetime.datetime(year, month, day))
    print(output)
    for folder in output:
        print(folder)
        if folder != 'twitter':

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

                subject = 'Scraping Alert Test'
                body = 'Folders'

                msg = f'Subject: {subject}\n\n{body}'

                #smtp.sendmail(SENDER, RECEIVER, msg)
                smtp.sendmail(EMAIL_ADRESS, 'carlo.bartsch@hsu-hh.de', msg)



        else:
            print('no')



# Import smtplib for the actual sending function



#EMAIL_ADRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



