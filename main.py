# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def ria(htp):
    with open('{htp}') as file:
        src = file.read()
        print(src)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # url = "https://energo.km.ua"
    url = "https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&region.id[0]=4&price.currency=1&mileage.lte=100&engine.lte=1.6&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&size=100&year[0].gte=2005&price.USD.gte=2000&price.USD.lte=4000"
    geturl = requests.get(url)
    #print(geturl.text)
    soup = BeautifulSoup(geturl.text, 'lxml')
    soup1 = soup.find('div', class_='content-bar')
    # ria('energo.km.ua')
    print(soup1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
