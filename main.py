# coronavirus outbreak notification system with plyer and bs4

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\pythonpro\My IMP projects\Covid Notification system\cicon_ULN_icon.ico",
        timeout=6
    )

# get data from url
def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        notifyme("Sagar", "let's stop the spread of the VIRUS together")
        myhtmldata = getdata('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myhtmldata, 'html.parser')
        # print(soup.prettify())
        mydatastr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydatastr += tr.get_text()
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        states = ['Maharashtra', 'Kerala', 'Telengana',
                  'Bihar','Delhi','Andhra Pradesh',
                  'Chhattisgarh','Gujarat','Haryana',
                  'Himachal Pradesh','Karnataka',
                  'Odisha','Puducherry','Punjab',
                  'Rajasthan','Tamil Nadu','Chandigarh',
                  'Jammu and Kashmir','Ladakh','Uttarakhand',
                  'West Bengal','Uttar Pradesh','Andaman and Nicobar Islands',
                  'Arunachal Pradesh','Assam','Goa',
                  'Jharkhand','Madhya Pradesh','Manipur',
                  'Mizoram','Tripura','	Uttarakhand'
                  ]
        for item in itemlist[0:31]:
            datalist = item.split('\n')
            if datalist[1] in states:
                print(datalist)
                ntitle = 'Cases of Covid-19'
                ntext = f"STATE : {datalist[1]}\nConfirmed : {datalist[2]}\nCured : {datalist[3]}\nDeaths : {datalist[4]} "
                notifyme(ntitle, ntext)
                time.sleep(5)
        time.sleep(3600)
