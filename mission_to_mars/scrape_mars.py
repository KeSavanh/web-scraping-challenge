import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Mars News Site
    url1 = 'https://redplanetscience.com'
    browser.visit(url1)
    html = browser.html
    soup = bs(html, 'html.parser')

    cards = soup.find_all('div', class_='list_text')
    for element in cards:
        title_list = element.find('div', class_='content_title').text.strip()
        para_list = element.find('div', class_='article_teaser_body').text.strip()
    
    # Featured Space Image site
    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)
    html = browser.html
    soup = bs(html, 'html.parser')

    image_url = soup.find('img', class_='headerimage')['src']
    featured_image_url = url2 + image_url

    # Mars Facts site
    url3 = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url3)
    info_df = tables[0]
    info_df.columns = ['Fact', 'Mars', 'Earth']
    info_df.drop(index=0)
    info_html = info_df.to_html()

    # Astrogeology site
    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    elements = soup.find_all('div', class_='description')
    sub_links = []
    image_titles = []
    
    for e in elements:
        sub_links.append(url4 + e.find('a')['href'])
        image_titles.append(e.find('h3').text.strip())  
    
    image_links = []
    for link in sub_links:
        browser.visit(link)
        html = browser.html
        soup = bs(html, 'html.parser')
        image_links.append(url4 + soup.find('img', class_='wide-image')['src'])

    browser.quit()

    hemisphere_image_urls = []
    for x in range(len(image_links)):
        hemisphere_image_urls.append({'title':image_titles[x], 'img_url': image_links[x]})

    # Create a dictionary to hold all mars information
    mars_info = {}
    mars_info['news_title'] = title_list
    mars_info['news_p'] = para_list
    mars_info['featured_image_url'] = featured_image_url
    mars_info['mars_fact'] = info_html
    mars_info['hemisphere_image_url'] = hemisphere_image_urls

    return mars_info