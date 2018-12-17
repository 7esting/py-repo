import csv
import requests
import urllib.request
from bs4 import BeautifulSoup

# The HTML Tags below are scrapped
#<div class="col-md-4 country">
#    <h3 class="country-name">
#        <i class="flag-icon flag-icon-zw"></i>
#            Zimbabwe
#    </h3>
#    <div class="country-info">
#        <strong>Capital:</strong> <span class="country-capital">Harare</span><br>
#        <strong>Population:</strong> <span class="country-population">11651858</span><br>
#        <strong>Area (km<sup>2</sup>):</strong> <span class="country-area">390580.0</span><br>
#    </div>
#</div>
with open("C:\opt\sheets\output_webscraping.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Capital", "Population", "Area"])
    url = "https://scrapethissite.com/pages/simple/"
    r = requests.get(url)
    html_data = r.text
    soup = BeautifulSoup(html_data, "html.parser")
    countries = soup.find_all("div", "country")

    # Storing the Scraped Data & Keeping Track of Progress
    for country in countries:
        name = country.find("h3").text.strip().encode("utf-8")
        capital = country.find("span", "country-capital").text.strip().encode("utf-8")
        population = country.find("span", "country-population").text.strip()
        area = country.find("span", "country-area").text.strip()
        writer.writerow([name, capital, population, area])

# Scrape Estimated Cost of Attendance at Sacramento State

#<td><strong>Tuition Fees</strong></td>
#<td>$7,204</td>
#<td>$7,204</td>
#<td>$7,204</td>
#</tr>
#<tr>

with open("C:\opt\sheets\sac_state_cost_of_attendance.csv", "w+") as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(["Allowance", "With Parents", "On-Campus", "Off-Campus"])
    r_sac_state = requests.get("https://www.csus.edu/faid/future-students/")
    html_request = r_sac_state.text
    soup_sac_state = BeautifulSoup(html_request, "html.parser")
    #cost_of_attendance = soup_sac_state.find_all('tr')[2]

   
    # Storing the Scraped Data & Keeping Track of Progress
    for fee in range(soup_sac_state.find_all('tr')[2]):
        td = soup_sac_state.find_all('td')
            # for i in range(start, end, increment):
        for i in range(1,2,1):
            allowance = td[0].text
            with_parents = td[1].text
            on_campus = td[2].text.strip().encode("utf-8")
            off_campus = td[3].text.strip().encode("utf-8")
            # Write out to csv file
            writer.writerow([with_parents, on_campus, off_campus])


