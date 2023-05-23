from bs4 import BeautifulSoup
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import time
import requests

LAST_DAYS = 10
MINUTES_PER_REQUEST = 10

def Find_Jobs():
    html_text = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3575090335&keywords=python").text
    soup = BeautifulSoup(html_text, 'lxml')
    python_jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    jobs_string = ""

    for python_job in python_jobs:

        publication_date = python_job.find('time')['datetime']
        year, month, day = [int(elem) for elem in publication_date.split('-')]

        publication_date_Type = date(year,month,day)
        current_day = date.today()

        if current_day >= publication_date_Type >= current_day - relativedelta(days=LAST_DAYS):
            
            job_name = python_job.find('h3', class_='base-search-card__title').text.strip()
            more_info = python_job.find('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')['href']

            jobs_string += f"Python Job\n" \
            f"-> Job name: {job_name}\n" \
            f"-> Publication Date: {publication_date}\n" \
            f"-> More info: {more_info}\n\n"
            
    return jobs_string

def Jobs_Logs(job_list: str):
    with open('./src/log/jobs_logs.txt', 'a') as file:
        file.write(f'####################################################\n' \
                   f'Requested at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n' \
                   f'{job_list}')

if __name__ == '__main__':

    while True:
        job_list = Find_Jobs()
        Jobs_Logs(job_list)
        print(f'Next request in {MINUTES_PER_REQUEST} minutes. Wating...')
        time.sleep(MINUTES_PER_REQUEST * 60)
        

