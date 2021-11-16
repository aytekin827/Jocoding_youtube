from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

elem = driver.find_element_by_name("q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN) # enter키와 같은 역할.

# scroll down
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

#결과 더보기 버튼
images = driver.find_elements_by_css_selector(".wXeWr.islib.nfEiy")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgURL = driver.find_element_by_css_selector(".n3VNCb").get_attribute('src')
        urllib.request.urlretrieve(imgURL,f'{str(count)}.jpg')
        count += 1
    except:
        pass
driver.close()