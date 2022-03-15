#!/usr/bin/python3
from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def resolver_err_xpath(path, driver):
    i = 1
    while i == 1:
        try:
            ele = driver.find_element_by_xpath(path)
            i = 0
        except NoSuchElementException as ex:
            print("solving issue :-"+path)
            time.sleep(1)

def resolver_err_site_ele(path, driver):
    i = 1
    while i == 1:
        if i == 5:
            break
        try:
            ele = driver.find_element_by_xpath(path)
            i = 0
        except NoSuchElementException as ex:
            time.sleep(1)

def form_to_fill(drive):
    res = 0
    resolver_err_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[2]', drive)
    for i in range(1,50):
        try:
            drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[2]')
            res += 1
        except NoSuchElementException:
            break
    return res
def chk_len_opt(pathvar,driver):
    res = 0
    resolver_err_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div['+str(pathvar)+']/div[2]/div/div/table/tbody/tr[1]/td[3]/label/span', driver)
    for j in range(1,15):
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div['+str(pathvar)+']/div[2]/div/div/table/tbody/tr['+str(j)+']/td[3]/label/span')
            res+=1
        except NoSuchElementException:
            break
    return res
def work(ida,passa,chrD_path,pref_sel):
    temp_pref_sel = pref_sel
    print("[+] ~ Bot Started")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")


    drive = webdriver.Chrome(chrD_path,chrome_options=chrome_options)
    drive.maximize_window()

    drive.get("https://s.amizone.net/")
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[1]/input[1]').send_keys(ida) # id (Check auth file)
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[2]/input').send_keys(passa) # password (Check auth file)
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[4]/button').click()
    drive.implicitly_wait(1)#resolver_err_site_ele('/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/button', drive)
    try:
        drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]/div/div/div[1]/button').click()
    except:
        pass
    try:
        drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/button').click()
    except:
        pass
    try: 
        drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div/div[1]/button').click()
    except:
        pass

    drive.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[1]/ul/li[6]/a/span').click()

    for i in range(1,form_to_fill(drive)+1): ## Number of feedback forms you have to fill
        cond = 0
        resolver_err_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[2]', drive)
        drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[2]').click()
        try:
            drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a')
        except:
            print("done")
            cond = 1
        
        if cond == 0:
            resolver_err_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a', drive)
            time.sleep(2)
            drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a').click()
            
            for j in range(1,chk_len_opt(1,drive)+1):
                if temp_pref_sel == 6:
                    pref_sel = random.randint(1, 3)
                resolver_err_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[2]/div/div/table/tbody/tr['+str(j)+']/td['+str(pref_sel+2)+']/label/span', drive)#drive.implicitly_wait(1)
                drive.implicitly_wait(1)
                drive.execute_script("window.scrollTo(0,0)")
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[2]/div/div/table/tbody/tr['+str(j)+']/td['+str(pref_sel+2)+']/label/span').click()
                                    
                #drive.execute_script("window.scrollTo(0,0)")
            for k in range(1,chk_len_opt(2,drive)+1):
                if temp_pref_sel == 6:
                    pref_sel = random.randint(1, 3)
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr['+str(k)+']/td['+str(pref_sel+2)+']/label/span').click()
            for l in range(1,chk_len_opt(3,drive)+1):
                if temp_pref_sel == 6:
                    pref_sel = random.randint(1, 3)
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr['+str(l)+']/td['+str(pref_sel+2)+']/label/span').click()
            for o in range(1,chk_len_opt(4,drive)+1):
                if temp_pref_sel == 6:
                    pref_sel = random.randint(1, 3)
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[4]/div[2]/div/div/table/tbody/tr['+str(o)+']/td['+str(pref_sel+2)+']/label/span').click()
            for m in range(1,chk_len_opt(5,drive)+1):
                if temp_pref_sel == 6:
                    pref_sel = random.randint(1, 3)
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[5]/div[2]/div/div/table/tbody/tr['+str(m)+']/td['+str(pref_sel+2)+']/label/span').click()
            for n in range(1,4):
                drive.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr['+str(n)+']/td[3]/label/span').click()
            drive.find_element_by_xpath('//*[@id="FeedbackRating_Comments"]').send_keys("All good:)")
            drive.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        drive.execute_script("window.scrollTo(0,"+str(i*70)+")")
        time.sleep(2)
        print("done")
    time.sleep(2)
    print("Thanks!!!")
    drive.close()




