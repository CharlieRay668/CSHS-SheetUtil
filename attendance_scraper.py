from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time

#WIP

now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
 # %A is to get the name of the Day! 
justtime = now.strftime("%H:%M")
print (current_time)

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})
    
# directing to the link to be visited; The program first logs into gmail for all around access of google services.
def gmail_login(driver, meet_link):
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("p2pcshsattendance@gmail.com")
    time.sleep(2)
        # Next Button:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
        #Password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys("Merlin@20")
    time.sleep(2)
        #next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
        # #opening Meet:
    driver.get(meet_link)
    driver.refresh()
    time.sleep(5)
        # Turning off video 
    # video_path = '/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div/div[1]'
    # driver.find_element_by_xpath(video_path).click()
    # time.sleep(5)
    #     # turning off audio
    # audio_path = '/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div/div[1]'
    # driver.find_element_by_xpath(audio_path).click()
    time.sleep(20)
        # Join class
    request_join_path = '/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span'
    driver.find_element_by_xpath(request_join_path).click()

driver = webdriver.Chrome(options=opt, executable_path = r'chromedriver')
gmail_login(driver, 'https://meet.google.com/ggx-uewn-twt')