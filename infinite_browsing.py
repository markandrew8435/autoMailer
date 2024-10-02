import asyncio
import re
import pyperclip
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as kController
from main import sendMail
from collections import deque
from threading import *

class InfiniteBrowsing:
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
        for _ in range(12):
            self.keyboard.tap(Key.page_down)
            time.sleep(0.5)

    def scroll_up(self):
        for _ in range(2):
            self.keyboard.tap(Key.page_up)
            time.sleep(0.5)

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
            for _ in range(3):
                self.scroll_down()
                self.scroll_up()

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

            self.mouse.position = extension_icon
            self.mouse.click(Button.left, 1)
            time.sleep(1)

            time.sleep(1)
            pasted_text = pyperclip.paste()
            print(i, pasted_text)
            self.send_to_queue(pasted_text)




# Main entry point
if __name__ == "__main__":

    browser = InfiniteBrowsing()


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
    # Sri@arnexsolution.com, sukanya@coretek.io, rohitb@interaslabs.com, srivastava.p@arkhyatech.com, leela@tanuinfotech.com, leela@tanuinfotech.com, dilip@osairtech.com, ram@sapotsystems.com, geethanjali@vsoftcorporation.com, tejas@intuites.com, waseem.khan@talentemail.com, bairaju.raju@unisys.com, sushma@lor-venk.com, mn@vyngroup.com, kalyanr@princetonamerica.com, brad1innoverglobalinc@gmail.com, salmanm4952@gmail.com, mn@vyngroup.com, Jessi.ch@technogenindia.com, sgoud@s-linx.com, salmanm4952@gmail.com, joshua@innoverglobalinc.com, salmanm4952@gmail.com, brad1innoverglobalinc@gmail.com, kavin@people-prime.com, salmanm4952@gmail.com, abirami.sakthimohan@ideas2it.com, deepak@workcog.com, deepak.recruiter28@gmail.com, hr@phen-tech.com, sangavi@eitacies.com, salmanm4952@gmail.com, kiran.vaddi@3coresystems.com, abdul.j@intone.com, peerulla@scalable-systems.com, deepak@workcog.com, deepak.recruiter28@gmail.com, anusha@rayantechnologiesinc.com, sushma@lor-venk.com, dilip@osairtech.com, geethika.n@mavinsys.com, ramanibenchsales25@gmail.com, contact@oneittech.com, geethika.n@mavinsys.com, Priya.vadhana@disys.com, saranya@mericaninc.com, bairaju.raju@unisys.com, contact@oneittech.com, kaveribenchsales07@gmail.com, geethika.n@mavinsys.com, contact@oneittech.com, nandini.ponduru@valuelabs.com, Jobs.Bfs@valuelabs.com, contact@oneittech.com, dilip@osairtech.com, priya@sapphiresoftwaresolutions.com, shubham.j@krgtech.com, samuel@ipartnerstaffing.com, amarender@wingsmicro.com, ramya@wingsmicro.com, priya@sapphiresoftwaresolutions.com, vinoth.anandhan@nityo.com, vinoth.anandhan@nityo.com, naresh@sumascorp.com, maheen@xytiqtechnologies.com, samuel@ipartnerstaffing.com, sarsanih@i-giants.com, dheeraj@questt.com, ravindras@arohak.com, raju@sirisoftsolutions.com, prasanna@fugetec.com, prasanna@fugetec.com, swathi.g@theegiants.com, g.swathi@inteliroute.net, harshi@eurekainfotech.com, prasanna@fugetec.com, prasanna@fugetec.com, likitha@eurekainfotech.com, hr@webethicssolutions.com, raju.methuku@agoda.com, juiconvictionhr24@gmail.com, zhengyiling.jaslin@bytedance.com, to-Shalini.rathore@seclance.com, narmadha.sriyaa@techwaukee.com, pavan.y@eateam.com, ttmyrecruit10@techtiera.com, mrtaban@absi.ph, raju.methuku@agoda.com, careers.em@valuelabs.com, recruitment@gamutinfosystems.com, hassam2357@gmail.com, raju.methuku@agoda.com, jobs@thegamestormstudios.com, jobs@thegamestormstudios.com, hr@synergysphere.co.in, thiri.ko1@huawei.com, jobs@thegamestormstudios.com, muhammadfaizul.mohdyunus@wdc.com, prathyusha.grandhi@vipanyglobal.com, praneeth@ssquare.com.au, nijee.s@adcuratio.com, hr@neuronsolutions.pk, swetha@ssquare.com.au, swetha@ssquare.com.au, hr@neuronsolutions.pk, sureshkumar.kandipalli@accionlabs.com, Jasmeet.kaur@obrimo.com, jobs@thegamestormstudios.com, hr@neuronsolutions.pk, careers.em@valuelabs.com, HR@cirruscloudsystems.com, faisal.ahmad@kjxsofttech.com, hrdepartment@kjxsofttech.com, Kashish.raj@kjxsofttech.com, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@hrways.co, jobs@thegamestormstudios.com, ahmed.sami.freelance@gmail.com, jobs@thegamestormstudios.com, geethamani@esquareinfo.com, juiconvictionhr24@gmail.com, shiza.growpeople@gmail.com, jeni@zaportiv.com, gopal.vutla@inclined360.com, lakshman.n@contingentpros.com, Cipherbytetechnologies.hr@gmail.com, m.mourad@mcsd.com.eg, radsenkri@gmail.com, s.elhassawy@wassil-claims.com, hr@logicsyner.com, gbakshi@xactlycorp.com, uniqueidealsolutions@gmail.com, makki@value-in.com, udyog@cipherbytetechnologies.com, hr@pycray.com, hr@pycray.com