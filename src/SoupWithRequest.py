from bs4 import BeautifulSoup
from datetime import date
from dateutil.relativedelta import relativedelta
import requests

LAST_DAYS = 5

html_text = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3575090335&keywords=python").text
soup = BeautifulSoup(html_text, 'lxml')

python_jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')


for python_job in python_jobs:

    publication_date = python_job.find('time')['datetime']
    year, month, day = [int(elem) for elem in publication_date.split('-')]

    publication_date_Type = date(year,month,day)
    current_day = date.today()

    if current_day >= publication_date_Type >= current_day - relativedelta(days=LAST_DAYS):
        
        job_name = python_job.find('h3', class_='base-search-card__title').text.strip()

        print(f"Python Job\n" \
        f"-> Job name: {job_name}\n" \
        f"-> Publication Date: {publication_date}\n"
        )