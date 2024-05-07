from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("""
     Instagram Bot'a Hoşgeldiniz!!!
     1-) Takip 
     
     
     2-) Beğeni
      """)

secim = input("Giriniz: ")
takipkontrol = 0

if secim == "1":
    print("""
    Takip etmek istediğiniz kişinin kullanıcı adını giriniz.
    """)
    kullanıcıadı = input("Kullanıcı Adı: ")
    takipkontrol =1
    


options = Options()
options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"


browser = webdriver.Firefox(options=options)


browser.get('https://www.instagram.com/')



wait = WebDriverWait(browser, 10)  # 10 saniye boyunca bekleyecek
try:
    ##element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[contains(@class, 'gameThumbContainer')][8]/a/img[contains(@class, 'gameThumb')]"))).click()
    ##browser.refresh()
    print("Element found!")
    ##msg = "Başarıyla tıklandı"
    ##postMail(msg)
except:
    print("Element not found!")
    ##msg = "Error!!!"
    ##postMail(msg)
    

kullanıcı = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Telefon numarası, kullanıcı adı veya e-posta']")))
sifre = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Şifre']")))

kullanıcı.send_keys('xxx@gmail.com')
sifre.send_keys('xxxxxx')

girisyap=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x1xmf6yo') and contains(@class, 'x1e56ztr') and contains(@class, 'x540dpk') and contains(@class, 'x1m39q7l') and contains(@class, 'x1n2onr6') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xdt5ytf') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]"))).click()

time.sleep(5)
simdideil = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(@class, 'xjqpnuy') and contains(@class, 'xa49m3k') and contains(@class, 'xqeqjp1') and contains(@class, 'x2hbi6w') and contains(@class, 'xdl72j9') and contains(@class, 'x2lah0s') and contains(@class, 'xe8uvvx') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'x2lwn1j') and contains(@class, 'xeuugli') and contains(@class, 'x1hl2dhg') and contains(@class, 'xggy1nq') and contains(@class, 'x1ja2u2z') and contains(@class, 'x1t137rt') and contains(@class, 'x1q0g3np') and contains(@class, 'x1lku1pv') and contains(@class, 'x1a2a7pz') and contains(@class, 'x6s0dn4') and contains(@class, 'xjyslct') and contains(@class, 'x1ejq31n') and contains(@class, 'xd10rxx') and contains(@class, 'x1sy0etr') and contains(@class, 'x17r0tee') and contains(@class, 'x9f619') and contains(@class, 'x1ypdohk') and contains(@class, 'x1f6kntn') and contains(@class, 'xwhw2v2') and contains(@class, 'xl56j7k') and contains(@class, 'x17ydfre') and contains(@class, 'x2b8uid') and contains(@class, 'xlyipyv') and contains(@class, 'x87ps6o') and contains(@class, 'x14atkfc') and contains(@class, 'xcdnw81') and contains(@class, 'x1i0vuye') and contains(@class, 'xjbqb8w') and contains(@class, 'xm3z3ea') and contains(@class, 'x1x8b98j') and contains(@class, 'x131883w') and contains(@class, 'x16mih1h') and contains(@class, 'x972fbf') and contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and contains(@class, 'xm0m39n') and contains(@class, 'xt0psk2') and contains(@class, 'xt7dq6l') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x1n2onr6') and contains(@class, 'x1n5bzlp') and contains(@class, 'x173jzuc') and contains(@class, 'x1yc6y37') and text()='Şimdi değil']"))).click()
time.sleep(2)
if takipkontrol ==1:
    browser.get("https://www.instagram.com/" + kullanıcıadı)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Takip Et']"))).click()
time.sleep(5)
simdideil2= wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='_a9-- _ap36 _a9_1' and text()='Şimdi Değil']"))).click()

time.sleep(3)

profilegit=wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@class, 'xpdipgo') and contains(@class, 'x972fbf') and contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and contains(@class, 'xm0m39n') and contains(@class, 'xk390pu') and contains(@class, 'x5yr21d') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'xl1xv1r') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x11njtxf') and contains(@class, 'xh8yej3')]"))).click()