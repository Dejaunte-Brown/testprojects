#Import the needed libraries
import requests
from bs4 import BeautifulSoup
import csv

#Go to the site you want to scrape and define the catagories for the excel spreadsheet
page_to_scrape = requests.get("https://www.zero-day.cz/database/?set_filter=Y&arrFilter_pf%5BYEAR_FROM%5D=2026&arrFilter_pf%5BYEAR_TO%5D=2026&arrFilter_pf%5BSEARCH%5D=")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
titles = soup.find_all("h3", {"class":"issue-title"})
descriptions = soup.find_all("div", {"class" : "description for-l"})
discovered = soup.find_all("div", {"class" : "discavered"})
patch = soup.find_all("div", {"class" : "patched"})

#Give the Newly Scrapped information a file to write over
file = open("ZERO_day_scrapped1.csv" , "w")
writer = csv.writer(file)
writer.writerow(["Titles", "Description", "Discovered", "Patched"])


#Define how you want it to look and check out the finished result
for title, description, discavered, patched in zip(titles, descriptions, discovered, patch):
    print(title.text + "-" + description.text + "  date found-" + discavered.text + " patch date- " + patched.text)
    writer.writerow([title.text, description.text, discavered.text, patched.text])
file.close()
