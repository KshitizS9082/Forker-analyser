from selenium.webdriver import Chrome
from time import sleep
import pandas as pd
#change your driver's location here
webdriver = "/Users/kshitizsharma/Downloads/chromedriver"
driver = Chrome(webdriver)

query = input("query on forkers repositories: ")
language = input("language (e.g. java): ")

urls = ["https://github.com/brownhci/WebGazer/network/members"]
########################
count=0
for url in urls:
    # url= "https://github.com/brownhci/WebGazer/network/members"
    driver.get(url)
    items = driver.find_elements_by_class_name("repo")
    print("number of forkers in this rep= "+str(len(items)))

    devLinks = []
    for item in items:
        x = item.find_elements_by_tag_name("a")
        el=x[0]
        link=el.get_attribute("href")
        # print(link)
        devLinks.append(link)
    print(str(len(devLinks)) + "number of links of forkers have been extracted")

    import csv
    with open('appLinks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "API URL" ,"forking developers URL", "Repositories satisfying our conditions"])

        for devlink in devLinks:
            linkToSearch = devlink + "?utf8=✓&tab=repositories&q="+query+"&type=&language="+language
            driver.get(linkToSearch)
            items = driver.find_elements_by_class_name("wb-break-all")
            for item in items:
                x = item.find_elements_by_tag_name("a")
                el=x[0]
                link=el.get_attribute("href")
                print(link)
                writer.writerow([str(count), url, devlink, link])
                count+=1
                if count%10==0:
                    # input("press a key to take scan next 30 links")
                    sleep(10)


