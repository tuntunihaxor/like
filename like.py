import os

try: 
    import selenium

except:
    os.system("pip3 install selenium")


biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

os.system("clear")


print(bigreen+"""
   ___ _                      _           _
  / __\ |__   __ _ _ __   ___| |__   __ _| |
 / /  | '_ \ / _` | '_ \ / __| '_ \ / _` | |
/ /___| | | | (_| | | | | (__| | | | (_| | |
\____/|_| |_|\__,_|_| |_|\___|_| |_|\__,_|_|

═══════════════════════════════════════════════
 Tools Name : LIKE4LIKE BOT
 Author : CHANCHAL ISLAM
 Contact :- linktr.ee/tuntunihaxor
═══════════════════════════════════════════════
""")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time 

class.AMFBot:
  def __init__(self, like4like_user, like4likepwd, twitter_user, twitter_pwd):
    self.like4like_user=like4like_user
    self.like4likepwd=like4likepwd
    self.twitter_user=twitter_user
    self.twitter_pwd=twitter_pwd
    self.options=Options()
    self.options.add_argument("--lang=en")
    self.bot=webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)
    
  def open(self):
    bot.maximize_window()
    bot.get("https://like4like.org/login/")
    usuario=bot.find_element_by_name("username")
    senha=bot.find_element_by_name("password")
    usuario.clear()
    senha.clear()
    usuario.send_keys(self.like4like_user)
    senha.send_keys(self.like4likepwd)
    bot.find_element_by_xpath('//*[@id="login"]/fieldset/table/tbody/tr[8]/td/span').click()
    time.sleep(5)
    ed.twtalk()
  
  def twtalk(self):
    bot=self.bot
    bot.get("https://www.like4like.org/free-twitter-followers.php")
    time.sleep(5)
    bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
    time.sleep(2)
    bot.switch_to_window(bot.window_handle[1])
    time.sleep(5)
    
    try:
      log.btn=bot.find_element_by_xpath('//div[@role="button"]//span[text()="Log in"]')
      if log_btn.is_displayed():
        log.btn.click()
        time.sleep(3)
        usuario=bot.find_element_by_xpath("//input[@type='text']")
        usuario.send_keys(self.twitter_user)
        bot.find_element_by_xpath('//div[@role="button"]//span[text()="Next"]').click()
        time.sleep(3)
        senha.bot.find_element_by_xpath("//input[@type='password']")
        senha.send_keys(self.twitter_pwd)
        bot.find_element_by_xpath('//div[@role="button" and @data-testid="LoginForm_Login_Button"]').click()
        time.sleep(5)
        follow=bot.find_element_by_xpath('//div[@role="button" and @data-testid="confirmationSheetConfirm"]')
        if follow.is_displayed():
          follow.click()
        time.sleep(5)  
      else:
        follow=bot.find_element_by_xpath('//div[@role="button" and @data-testid="confirmationSheetConfirm"]')
        if follow_displayed():
          follow.click()
        time.sleep(5)
        
    except bot.NoSuchElementException:
      bot.close()
      bot.switch_to_window(bot.window_handle[0])
      time.sleep(5)
      bot.get("https://www.like4like.org/free-twitter-followers.php")
      ed.twttwo()
      
    bot.close()
    bot.switch_to_window(bot.window_handle[0])
    ed.twttwo()
    
  def twttwo(self):
    bot=self.bot 
    confirm=bot.find_element_by_css_selector("a[class^='cursor pulse-checkBox']")
    if confirm.is_displayed():
      confirm.click()
      time.sleep(2)
      bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']")
      bot.switch_to_window(bot.window_handle[1])
      time.sleep(5)
    else:
      bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']")
      bot.switch_to_window(bot.window_handle[1])
      time.sleep(5)
    try:
      follow=bot.find_element_by_xpath('//div[@role="button" and @data-testid="confirmationSheetConfirm"]')
        if follow_displayed():
          follow.click()
        time.sleep(5)
        
        
    except bot.NoSuchElementException:
      bot.close()
      bot.switch_to_window(bot.window_handle[0])
      time.sleep(5)
      bot.get("https://www.like4like.org/free-twitter-followers.php")
      ed.twttwo()
      
    bot.close()
    bot.switch_to_window(bot.window_handle[0])
    ed.twttwo()  

ed.AMFBot('like4like_user', 'like4likepwd', 'twitter_user', 'twitter_pwd')
ed.open()

    
