import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def save_to_file(file_name, info_lst):
    file = open(f"{file_name}.csv", mode='w')
    writer = csv.writer(file)
    writer.writerow(["place", "company", "time", "pay", "date"])
    for info in info_lst:
        writer.writerow([info[0], info[1], info[2], info[3], info[4]])
    return


def get_job_lst(file_name, url):
    try:
        infos = requests.get(url)
        soup = BeautifulSoup(infos.text, 'html.parser')
        lst = soup.find('div', {'id': 'NormalInfo'}).find("tbody")
        place_lst = lst.find_all('td', {'class': 'local'})
        company_lst = lst.find_all('span', {'class': 'company'})
        time_lst = lst.find_all('span', {'class': 'time'})
        pay_lst = lst.find_all('td', {'class': 'pay'})
        date_lst = lst.find_all('td', {'class': 'regDate'})
        job_counter = len(company_lst)
        jobs = []
        for i in range(0, job_counter):
            jobs.append([place_lst[i].text, company_lst[i].text,
                         time_lst[i].text, pay_lst[i].text, date_lst[i].text])
        save_to_file(file_name, jobs)
    except:
        print("No list of job")
        return


def main():
    alba = requests.get(alba_url)
    soup = BeautifulSoup(alba.text, 'html.parser')
    site_link_lst = soup.find('div', {'id': 'MainSuperBrand'}).find_all(
        'a', {'class': 'brandHover'})
    site_names_links = {}
    for elem in site_link_lst:
        if elem.text:
            site_names_links.update({elem.text[2:-9]: elem['href']})
    for elem in site_names_links:
        print(f"Getting started {elem}")
        get_job_lst(elem, site_names_links[elem])
        print("Process complete")


main()
