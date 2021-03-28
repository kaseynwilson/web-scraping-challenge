# Web Scraping Challenge
## Mission to Mars

A web application was built that scrapes data from several websites to gather data and images related to the Mission to Mars and displays the scraped data in an HTML page.

## Web Scraping:

#### NASA Mars News

* Scraped the NASA Mars News Site (https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. 

#### JPL Mars Spaces Images - Featured Image

* Scraped the URL for the JPL Featured Space Image from the following site https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html

#### Mars Facts

* Scraped the Mars Facts table from https://space-facts.com/mars/ using Pandas and converted the data to an HTML table string. 

#### Mars Hemispheres

* From the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars I scraped the links and titles for the inages for each of Mar's hemispheres. 


## MongoDB and Flask Application

* A single Python script runs the scraping code and stores all of the scraped data in a dictionary.

* A route '/scrape' was created to import the Python script and call the scrape function. 

* The return value from the Python script /scrape route is stored in Mongo. 

* Created a root route / that queries the database and passes the mars data into an HTML template to display the data.

* The HTML file 'index.html' displays all of the data in HTML elements with Bootstrap. 
