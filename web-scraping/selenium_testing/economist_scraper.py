from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import argparse, json, time
import numpy as np

def expo_wait():
    '''
    expo wait - create an exponential random sleep time
    '''
    time.sleep(210*np.random.exponential())

def scrape_topic(driver, topic_stem, collection, page=None):
    '''
    scrape topic - get a list of articles by topic from the economist, itterate throught
    Inputs:
    * driver = a selenium web driver logged into the economist
    * topic_stem = the page type from the economist (e.g. "science-and-technology/")
    * db = pyMongo collection object
    * page = the page number to scrape, default None (default is page 1)
    '''
    if page == None:
        driver.get("https://www.economist.com/" + topic_stem)
    else:
        print("Page : {}".format(str(page)))
        driver.get("https://www.economist.com/" + topic_stem + "?page=" + str(page))
    time.sleep(10)

    articles = driver.find_elements_by_class_name('teaser__link')
    
    # loop through tags getting sub pages
    for art in articles:
        try:
            link = art.get_attribute('href')
        
            # Open new tab
            driver.execute_script("window.open('');")
            time.sleep(3)

            # Switch to the new window
            driver.switch_to.window(driver.window_handles[1])
            driver.get(link)
            expo_wait()

            # Get text of article
            words = driver.find_element_by_class_name('blog-post__text').text
            title = driver.find_element_by_class_name('flytitle-and-title__title').text
            print("\tTitle: {}".format(title))
            collection.insert_one({"class":topic_stem[:-1], "text":words, "headline":title})
        except:
            continue

        # close the active tab
        driver.close()

        # Switch focus back to main tab
        driver.switch_to.window(driver.window_handles[0])


def main(name, passwd):
    # Initialize Driver
    driver = webdriver.Firefox()
    driver.get("https://www.economist.com/free-email-newsletter-signup?tab=login")
    time.sleep(5)
    # Login
    elem = driver.find_element_by_css_selector('input[type="email"]')
    elem.send_keys(name)
    elem = driver.find_element_by_css_selector('input[type="password"]')
    elem.send_keys(passwd)
    time.sleep(5)
    driver.find_element_by_id("submit-login").click()
    time.sleep(5)
    # Initialize Mongo DB
    client = MongoClient()
    db = client.economist
    collection = db.articles
    # Scrape topics
    scrape_topic(driver, "science-and-technology/", collection)
    for page in range(2,250):
        scrape_topic(driver, "science-and-technology/", collection, page=page)
    driver.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cred_file", help="Relative file path and name for credentials file")
    args = parser.parse_args()
    with open(args.cred_file, 'r') as f:
        creds = json.load(f)
    name = creds["economist"]["uname"]
    passwd = creds["economist"]["passwd"]
    main(name, passwd)