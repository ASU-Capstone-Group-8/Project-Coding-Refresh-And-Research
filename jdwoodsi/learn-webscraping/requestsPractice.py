from bs4 import BeautifulSoup
import requests
import time
import datetime

print("List a skill that you aren't familiar with")
unfamiliar_skill = input(">")
print("Filtering out any jobs that require: " + unfamiliar_skill)

def actions(index, company_name, skills, more_info):
    with open('job listings/listing ' + str(index) + ' as of ' + datetime.datetime.now().strftime(
            "%B %d, %Y") + '.txt', 'w') as f:
        print("Company: " + company_name)
        print("Necessary Skills: " + skills)
        print("More Info: " + more_info)
        f.write("Company: " + company_name)
        f.write("Necessary Skills: " + skills)
        f.write("More Info: " + more_info)

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text #same website as video


    soup = BeautifulSoup(html_text, 'lxml')


    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')


    for index, job in enumerate(jobs):
       published_date = job.find('span', class_ = 'sim-posted').span.text


       if 'few' in published_date:
           company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
           skills = job.find('span', class_='srp-skills').text.replace(' ', '')
           more_info = job.header.h2.a['href']

           if unfamiliar_skill != "":
               if unfamiliar_skill not in skills:
                   actions(index, company_name, skills, more_info)
           else:
               actions(index, company_name, skills, more_info)



if __name__ == '__main__':
    while True:
        find_jobs()

        time_wait = 10 #minutes to wait before refreshing data

        time.sleep(time_wait * 60)