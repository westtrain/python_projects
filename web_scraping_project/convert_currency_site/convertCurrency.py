import os
import requests
from bs4 import BeautifulSoup
# from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
trans_currency_url = "https://transferwise.com/gb/currency-converter/"


def get_requests_url(c_lst):
    iban_text = requests.get(url)
    soup = BeautifulSoup(iban_text.text, 'html.parser')
    list = [element.text for element in soup.find_all("td")]
    for i in range(0, len(list), 4):
        if list[i + 1] != 'No universal currency':
            c_lst.append([list[i], list[i + 2]])
    for country in c_lst:
        print(f"# {c_lst.index(country)} {country[0]}")


def transfer_currency(from_code, to_code, currency):
    add_url = from_code + "-to-" + to_code + "-rate?amount=" + currency
    transfer = requests.get(trans_currency_url + add_url)
    soup = BeautifulSoup(transfer.text, 'html.parse')
    res = soup.find('input', {'id': "cc-amount-to"}).get('value')
    return res


def input_another_country(c_lst, ctry_num):
    try:
        print("Now choose another country.")
        print()
        another_crty = int(input("#: "))
        print(f"{c_lst[another_crty][0]}")
        print()
    except:
        print("That wasn't a number.")
        input_another_country(c_lst, ctry_num)
    else:
        print(
            f"How many {c_lst[ctry_num][1]} do you want to convert {c_lst[another_crty][1]}?")
        input_currency = int(input())
        currency = transfer_currency(
            c_lst[ctry_num][1], c_lst[another_crty][1])
        res = format_currency(currency, "KRW", locale="ko_KR")
        print(f"{c_lst[ctry_num][1]} {input_currency} is {res}")


def input_country(c_lst):
    try:
        print("Where are you from? Choose a country by number.")
        print()
        user_input = int(input("#: "))
        if user_input > 264:
            print("Choose a number from the list.")
            input_country(c_lst)
        else:
            print(f"{c_lst[user_input][0]}")
            print()
            input_another_country(c_lst, user_input)
    except:
        print("That wasn't a number.")
        input_country(c_lst)


def main():
    print("Hello! Please choose a country by number:")
    countries_lst = []
    get_requests_url(countries_lst)
    # input_country(countries_lst)


main()

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
print(format_currency(5000, "KRW", locale="ko_KR"))
"""
