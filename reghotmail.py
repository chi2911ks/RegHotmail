 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
 
from selenium.webdriver.chrome.service import Service
import time,requests,random,threading
 

class Chrome(threading.Thread):
    def __init__(self, Proxy, x):
      threading.Thread.__init__(self)
      self.Proxy = Proxy
      self.x = x
    def FunCaptcha(self):
        # try:
        data_any={
        "clientKey":"217d5b6070814290b5b7d25ec7cfa154",
            "task":{
            "type":"FunCaptchaTaskProxyless",
            "websiteURL":"https://signup.live.com/signup?lic=1&uaid=9b23f83c11f440f8993626a59f3aac7f",
            "websitePublicKey":"B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",
            },
            "softId":847,
            "languagePool":"en"
        }
        posat=requests.post("https://api.anycaptcha.com/getBalance",data={"clientKey": "217d5b6070814290b5b7d25ec7cfa154"}).json()
        if float(posat["balance"])<0.003:
            print("Hết tiền")
            return "money"
        post=requests.post("https://api.anycaptcha.com/createTask",json=data_any).json()
        taskId=post["taskId"]
        result=requests.post("https://api.anycaptcha.com/getTaskResult",data={"clientKey":"217d5b6070814290b5b7d25ec7cfa154","taskId":taskId}).json()
        if result["errorId"]==2:
            exit()
        if result["status"]=="ready" and result["errorId"]==0:
            return result["solution"]["token"]
        # except:
        #     return 0
    def Create_Password(self):
        self.password = ""
        for i in range(4):
            LIST_NUMBERS = random.choice([0,1,2,3,4,5,6,7,8,9])
            LIST_ALPHABET_LOWER = random.choice(["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"])
            LIST_ALPHABET_UPPER = random.choice(["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"])
            LIST_CHAR = random.choice(["~","!","#","$","%","^","&","*","(",")","<",">","?",".","/","|"])
            self.password += LIST_ALPHABET_LOWER+str(LIST_NUMBERS)+LIST_ALPHABET_UPPER+LIST_CHAR
    def LastName_FirtName(self):
        ten=random.choice(['Nguyễn Văn Vinh','Đỗ Trọng Bảo','Đỗ Trọng Chi','Đỗ Bình Linh','Đặng Tuấn Anh','Lưu Trang Anh','Hoàng Đức Anh','Phạm Hoàng Anh','Phạm Thị Anh','Đỗ Gia Bảo','Trần Thị Châu','Tăng Phương Chi','Phạm Tiến Dũng','Trần An Dương','Mạc Trung Đức','Vũ Hương Giang','Nguyễn Thị Ngân','Nguyễn Lê Hiếu','Phạm Xuân Hòa','Khoa Minh Hoàng','Nguyễn Hữu Hiệp','Nguyễn Mạnh Hùng','Nguyễn Vũ Gia','Trần Tuấn Hưng','Đàm Yến Nhi','Đoàn Hoàng Sơn'])
        self.LastName = ten.split(" ")[1] +" "+ ten.split(" ")[2]
        self.FirtName = ten.split(" ")[0]
    def MemberNamee(self):
        self.MemberName = ""
        for f in range(4):
            LIST_NUMBERS = random.choice([0,1,2,3,4,5,6,7,8,9])
            LIST_ALPHABET_LOWER = random.choice(["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"])
            LIST_ALPHABET_UPPER = random.choice(["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"])
            self.MemberName += LIST_ALPHABET_LOWER+str(LIST_NUMBERS)+LIST_ALPHABET_UPPER
    def run(self):
        self.Create_Password()
        self.LastName_FirtName()
        self.MemberNamee()
        options = webdriver.ChromeOptions()
        options.add_argument("--proxy-server="+self.Proxy)
        options.add_argument("--window-size=270,425")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-application-cache")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--app=https://httpbin.org/ip")
        self.driver = webdriver.Chrome(service = Service("G:\\MaxCare\\chromedriver.exe"),options=options)
        self.driver.set_window_position(self.x, 0, windowHandle='current')
        self.driver.get("https://signup.live.com/signup")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,"MemberName").send_keys(self.MemberName+"@hotmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID,"iSignupAction").click()
        time.sleep(5)
        self.driver.find_element(By.ID,"PasswordInput").send_keys(self.Password)
        time.sleep(1)
        self.driver.find_element(By.ID,"iSignupAction").click()
        time.sleep(3)
        self.driver.find_element(By.ID,"FirstName").send_keys(self.FirtName)
        time.sleep(1)
        self.driver.find_element(By.ID,"LastName").send_keys(self.LastName)
        time.sleep(1)
        self.driver.find_element(By.ID,"iSignupAction").click()
        time.sleep(4)
        days = Select(self.driver.find_element(By.ID,"BirthDay"))
        months = Select(self.driver.find_element(By.ID,"BirthMonth"))
        months.select_by_value(str(random.randint(1,12)))
        time.sleep(1)
        days.select_by_value(str(random.randint(1,30)))
        time.sleep(1)
        self.driver.find_element(By.ID,"BirthYear").send_keys(random.randint(1968,2004))
        time.sleep(1)
        self.driver.find_element(By.ID,"iSignupAction").click()
        time.sleep(3)
        self.driver.implicitly_wait(10)
        if "We'll text you the code you'll use to verify your phone number." in self.driver.page_source:
            self.driver.close()
            return
        time.sleep(50)
        token = self.FunCaptcha()
        if token == 0:
            print("Lỗi nè đm")
            self.driver.close()    
        elif token == "money":
            self.driver.close()
            return
        else:
            self.driver.execute_script("""var anyCaptchaToken = '"""+token+"""';var enc = document.getElementById('enforcementFrame');
                                        var encWin = enc.contentWindow || enc;
                                        var encDoc = enc.contentDocument || encWin.document;
                                        let script = encDoc.createElement('SCRIPT');
                                        script.append('function AnyCaptchaSubmit(token) { parent.postMessage(JSON.stringify({ eventId: "challenge-complete", payload: { sessionToken: token } }), "*") }');
                                        encDoc.documentElement.appendChild(script);
                                        encWin.AnyCaptchaSubmit(anyCaptchaToken);""")
        time.sleep(10)
        if "Stay signed in?" in self.driver.page_source:
            print("Tạo thành công")
            open("hotmail.txt","a+").write("%s|%s\n"%(self.MemberName+"@hotmail.com",self.Password))
            self.driver.find_element(By.ID,"idSIButton9").click()
            time.sleep(5)
            self.driver.close()
        self.driver.implicitly_wait(10)
        if "We'll text you the code you'll use to verify your phone number." in self.driver.page_source:
            self.driver.close()
            return
if __name__ == '__main__': 
    while True:
        # x = 0
        # for j in range(2):
        #     c = Chrome("", x)
        #     c.start()
        #     x += 340
        # time.sleep(150)
        Proxy = requests.get("https://proxy.tinsoftsv.com/api/changeProxy.php?key=TLiLkIcTdQTssLdE6poM4k7vvCdMYdkk3tvh1q&location=0").json()
        if Proxy["success"]:
            x = 0
            for j in range(3):
                c = Chrome(Proxy["proxy"], x)
                c.start()
                x += 267
            time.sleep(150)
        else:
            if "Request so fast" in str(Proxy) or "key expired!" in str(Proxy["description"]):
                break
            else:
                time.sleep(Proxy["next_change"])

