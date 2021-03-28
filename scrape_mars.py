# Dependencies
import os
from splinter import Browser 
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#create function scrape to execute scraping code and return one Python dictionary containing all of the scraped data.
def scrape():
    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Create dictionary to hold all scraped data.
    scrape_mars_dict = {}


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with html
    soup = bs(response.text, 'html.parser')
    #Grab first title and store in variable
    content_title = soup.find('div', class_='content_title').get_text()
    # Grab first title description and store in variable
    content_text = soup.find_all('div', class_='rollover_description_inner')[0].get_text()
    scrape_mars_dict["content_title"] = content_title
    scrape_mars_dict["content_text"] = content_text

    url_jpl = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url_jpl)
    browser.links.find_by_partial_text("FULL IMAGE").click()
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_source_image = soup.find('img', class_="fancybox-image")["src"]
    featured_image_url = f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{mars_source_image}"
    scrape_mars_dict["featured_image_url"] = featured_image_url

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    facts_df = tables[0]
    html_table = facts_df.to_html()
    html_table.replace('\n', '')
    scrape_mars_dict["table"] = html_table

    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    hemispheres = []
    for x in range(4):
        hemisphere = {}
        hemisphere["title"] = browser.links.find_by_partial_text('Enhanced')[x].text
        browser.links.find_by_partial_text('Enhanced')[x].click()
        hemisphere["url"] = browser.links.find_by_partial_text('Sample')["href"]
        hemispheres.append(hemisphere)
        browser.back()
    scrape_mars_dict["hemispheres"] = hemispheres

    # Quit the browser
    browser.quit()

    return scrape_mars_dict

    print(scrape_mars_dict)