from selenium import webdriver
from selenium.webdriver.edge import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox
import string
import random
import time

message = "Change to mobile mode and click OK.\nTo change to device mode:\nOpen devTools through F12 then click on \'Toggle device toolbar\' button"

def string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def search_loop(driver, loops):
    for index in range(loops):
        element = driver.find_element(By.NAME, "q")
        element.clear()
        search_string = string_generator()
        element.send_keys(search_string)
        element.send_keys(Keys.RETURN)
        time.sleep(.5)


def main():
    driver = webdriver.Edge("msedgedriver.exe")
    driver.get("https://www.bing.com/")
    driver.maximize_window()

    search_loop(driver, 41)

    messagebox.showinfo("WARNING!", message)

    search_loop(driver, 21)

    driver.close()


if __name__ == "__main__":
    main()