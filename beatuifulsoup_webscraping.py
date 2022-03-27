from bs4 import BeautifulSoup
import requests  # request information from websites
import time

print("Type the skills you are unfamiliar with")
unfamiliar_skills = input('>')
print(f"filtering out {unfamiliar_skills}")


def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_='sim-posted').span.text
        if 'few' in posted_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'file saved: {index}')

while True:
    find_jobs()
    time_wait = 60
    print("Waiting 1hour")
    time.sleep(time_wait*60)
