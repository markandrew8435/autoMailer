import asyncio
import re
import pyperclip
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as kController
from main import sendMail
from collections import deque
from threading import *

class PaginatedBrowsing:
    def __init__(self):
        self.keyboard = kController()
        self.mouse = Controller()
        self.mail_queue = deque([])
        self.is_clearing = False

    # Function to simulate pressing the search bar
    def go_to_searchbar(self):
        self.keyboard.press(Key.ctrl_l)
        self.keyboard.type("l")
        self.keyboard.release(Key.ctrl_l)

    # Function to generate LinkedIn search URL
    def get_url(self, page: int):
        return f"https://www.linkedin.com/search/results/all/?keywords=%22looking%22%20%22springboot%22%20%22resume%22&origin=GLOBAL_SEARCH_HEADER&page={page}&sid=st4"

    # Function to scroll down the page
    def scroll_down(self):
        scrl = (1911, 766)
        for _ in range(5):
            time.sleep(3)
            self.keyboard.tap(Key.page_down)

    # Async function to clear the email queue
    def clear_queue(self):
        self.is_clearing = True
        while self.mail_queue:
            mail = self.mail_queue.pop()

            sendMail(mail)  # Assuming sendMail is a synchronous function
        self.is_clearing = False

    # Function to send email IDs to the queue
    def send_to_queue(self, mailids):
        mailids = mailids.split(',')
        for i in mailids:
            if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', i.strip()):
                self.mail_queue.appendleft(i.strip())
        print(mailids)
        # if not self.is_clearing:
        #     print("reached here____________________________")
        #     asyncio.create_task(self.clear_queue())

    # Async function for browsing LinkedIn and processing data
    async def start_browsing(self):
        time.sleep(3)
        extension_icon = (1771, 61)
        read_btn = (1325, 102)
        copy_btn = (1415, 101)

        for i in range(1, 1000):
            self.go_to_searchbar()
            self.keyboard.type(self.get_url(i))
            self.keyboard.tap(Key.enter)
            time.sleep(15)
            self.scroll_down()

            self.mouse.position = extension_icon
            self.mouse.click(Button.left, 1)
            time.sleep(1)

            for _ in range(2):
                self.mouse.position = read_btn
                self.mouse.click(Button.left, 1)
                time.sleep(1)

            self.mouse.position = copy_btn
            time.sleep(1)
            self.mouse.click(Button.left, 1)

            time.sleep(1)
            pasted_text = pyperclip.paste()
            print(i, pasted_text)
            self.send_to_queue(pasted_text)




# Main entry point
if __name__ == "__main__":

    browser = LinkedInBrowser()


    class Browse(Thread):
        def run(self):
            asyncio.run(browser.start_browsing())


    class ClearQ(Thread):
        def run(self):
            if(not browser.is_clearing):
                browser.clear_queue()

    Browse().start()

    while(True):
        if(not browser.is_clearing):
            ClearQ().start()

        time.sleep(2)



    #https://www.linkedin.com/search/results/all/?keywords=%22looking%22%20%22springboot%22%20%22resume%22&origin=GLOBAL_SEARCH_HEADER&page=1&sid=st4
    # while(True):
    #     time.sleep(1)
    #     print(browser.mouse.position)