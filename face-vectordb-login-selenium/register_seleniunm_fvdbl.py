from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# webdriver.maximize_window() # For maximizing window
# webdriver.implicitly_wait(20) # gives an implicit wait for 20 seconds

options = webdriver.ChromeOptions()

# 默认chrome允许使用麦克风和摄像头权限(1允许2不允许)
options.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 1,
    },
)
webdriverFVL = webdriver.Chrome(options=options)
webdriverFVL.get("http://127.0.0.1:5000")
sleep(1)

print("进入 注册页面 进行测试。。。")

# 测试注册界面
webdriverFVL.find_element(By.LINK_TEXT, "注册页面").click()
sleep(1)

webdriverFVL.find_element(By.ID, "startBtnRegister").click()
sleep(3)

webdriverFVL.find_element(By.ID, "captureButton").click()
sleep(1)

webdriverFVL.find_element(By.ID, "name").send_keys("曾逸夫")
sleep(1)

webdriverFVL.find_element(By.ID, "registerButton").click()  # 注册
sleep(2)

webdriverFVL.switch_to.alert.accept()  # 点击确定按钮
sleep(1)

webdriverFVL.find_element(By.ID, "stopBtnRegister").click()
sleep(2)


# sleep(2)
webdriverFVL.quit()
