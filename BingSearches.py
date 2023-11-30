from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
        time.sleep(3)
        driver.get("https://www.bing.com/")


def main():
    edge_path = EdgeChromiumDriverManager().install()

    driver = webdriver.Edge(executable_path=edge_path)
    driver.maximize_window()

    driver.get("https://www.bing.com/")
    time.sleep(8)
    
    search_loop(driver, 35)

    messagebox.showinfo("WARNING!", message)

    search_loop(driver, 21)

    driver.close()


if __name__ == "__main__":
    main()
