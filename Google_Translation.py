from selenium import webdriver
import time
import pymysql.cursors
import re
import wx
import sys, os
import html
import string
import Global_var
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import linecache
app = wx.App()

chrome_options = Options()
chrome_options.add_extension('C:\\Translation EXE\\BrowsecVPN.crx')
browser = webdriver.Chrome(executable_path=str(f"C:\\Translation EXE\\chromedriver.exe"),chrome_options=chrome_options)
browser.maximize_window()
# browser.get("""https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh?hl=en" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh%3Fhl%3Den&amp;ved=2ahUKEwivq8rjlcHmAhVtxzgGHZ-JBMgQFjAAegQIAhAB""")
wx.MessageBox(' -_-  Add Extension and Then Click On OK BUTTON -_- ', 'Contract Award Tender Google Translation Exe', wx.OK | wx.ICON_ERROR)
time.sleep(5)
try:
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)
except:
    browser.switch_to.window(browser.window_handles[0])
browser.get('https://translate.google.com/')

input_xpath_list = ['//*[@id="source"]','//*[@aria-label="Source text"]']
output_xpath_list = ['//*[@class="tlid-translation translation"]','//*[@class="VIiyi"]']
Clear_xpath_list = ['//*[@aria-label="Clear source text"]/i','//*[@class="clear-wrap"]/div/div']

def Print_Exception_detail(e):
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename,lineno, f.f_globals)
    print(f'EXCEPTION: {e}\nLINE NO: {lineno}\nError Line Text: "{line.strip()}")\nException Type: {exc_type}\n')
    
def connection():
    a3 = 0
    while a3 == 0:
        try:
            connection = pymysql.connect(host='185.142.34.92',user='ams',password='TgdRKAGedt%h',db='contractawards_db',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            return connection
        except Exception as e:
            print('Error On Connection Function\n')
            Print_Exception_detail(e)
            time.sleep(10)
            a3 = 0

def casesensitive(ReplyStrings):
    ReplyStrings1 = string.capwords(str(ReplyStrings))
    title = ReplyStrings1.replace(" A ", " a ").replace(" An ", " an ").replace(" The ", " the ").replace(" And "," and "). \
        replace(" If ", " if ").replace(" Else ", " else ").replace(" When ", " when ").replace(" Up ", " up ") \
        .replace(" At ", " at ").replace(" From ", " from ").replace(" By ", " by ").replace(" On ", " on ") \
        .replace(" Off ", " off ").replace(" At ", " at ").replace(" Of ", " of ").replace(" For ", " for "). \
        replace(" In ", " in ").replace(" Out ", " out ").replace(" Over ", " over ").replace(" To ", " to ") \
        .replace(" Is ", " is ").replace(" Or ", " or ").replace(" With ", " with ").replace(" Which ", " which ") \
        .replace(" Will ", " will ").replace(" Be ", " be ").replace(" There ", " there ").replace(" Where ", " where ") \
        .replace(" Have ", " have ").replace(" Do ", " do ").replace(" Nor ", " nor ").replace(" Some ", " some ") \
        .replace(" Since ", " since ").replace(" Till ", " till ").replace(" Until ", " until ").replace(" Onto "," onto ") \
        .replace(" Used ", " used ").replace(" Of ", " of ").replace(" That ", " that ").strip()
    return title


def check_translated_textarea():
    tr_clear = False
    while tr_clear == False:
        tr_val = ''
        for output_xpath in output_xpath_list:
            for tr_box in browser.find_elements_by_xpath(output_xpath):
                tr_val = 'Wait until Output Clear'
                print(tr_val)
                time.sleep(1)    
        if tr_val == '':
            tr_clear = True
        else:
            browser.get('https://translate.google.com/')
            time.sleep(2)
            tr_clear = False

# def click_on_clear():
#     for input_xpath in input_xpath_list:
#         for i in browser.find_elements_by_xpath(input_xpath):
#             i.clear()

#     click_clear = False
#     error = False
#     for Clear_xpath in Clear_xpath_list:
#         try:
#             for clear_btn in browser.find_elements_by_xpath(Clear_xpath):
#                 click_clear = True
#                 clear_btn.click()
#                 time.sleep(2)    
#                 break
#         except:
#             error = True  
#         if click_clear == True:
#             break
#     if error == True:  # this below code for urdu language
#         try:
#             for click_on_google_translate_logo in browser.find_elements_by_xpath('//*[@title="Google Translate"]/span[2]'):
#                 click_on_google_translate_logo_text = click_on_google_translate_logo.get_attribute('innerText').lower().strip()
#                 if 'translate' in click_on_google_translate_logo_text:
#                     click_on_google_translate_logo.click()
#                     time.sleep(3)
#                     break
#         except:
#             print('Error while clicking google translation logo')
#         try:
#             for click_detect_lang in browser.find_elements_by_xpath('//*[@jsname="bN97Pc"]/span'):
#                 click_detect_lang_text = click_detect_lang.get_attribute('innerText').lower().strip()
#                 if 'detect language' in click_detect_lang_text:
#                     click_detect_lang.click()
#                     time.sleep(3)
#                     break
#         except:
#             pass
            
def click_on_tryagain():
    print(' -_-  Please wait page will be refresh automatically after 10 SEC  === NO OUTPUT FOUND === -_- ')
    time.sleep(10)
    main_string = ''
    for output_xpath in output_xpath_list:
        for output_textarea in browser.find_elements_by_xpath(output_xpath):
            main_string = output_textarea.get_attribute('innerText')
            return main_string
            
    try_btn_found = False
    try:
        for try_again_btn in browser.find_elements_by_xpath('//*[@class="tlid-result-container-error-button translation-error-button"]'):
            try_again_btn.click()
            time.sleep(3)
            try_btn_found = True
            for output_xpath in output_xpath_list:
                for output_textarea in browser.find_elements_by_xpath(output_xpath):
                    main_string = output_textarea.get_attribute('innerText')
            break
    except:
        print('Error:  Try Again Button Not Found')
    if try_btn_found == False:
        # clicking_process_on_transltion_logo()   
        browser.get('https://translate.google.com/')
    return main_string


# def language_detect():
#     If_other_Than_English = True
#     for language_detect in browser.find_elements_by_xpath('//*[@class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-right jfk-button-checked"]'):
#         language_detect = language_detect.get_attribute('innerText').lower()
#         if 'english' not in language_detect:
#             If_other_Than_English = True
#         else:
#             If_other_Than_English = False
#         break
#     return If_other_Than_English

# def something_Went_wrong():
#     browser.get('https://translate.google.com/')
#     time.sleep(10)
#     if_find_xpath = False
#     for input_xpath in input_xpath_list:
#         for i in browser.find_elements_by_xpath(input_xpath):
#             if_find_xpath = True
#     if if_find_xpath == False:
#         wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ',' CA Special Translation Exe ', wx.OK | wx.ICON_WARNING)

def tarnslation():
    try:
        
        trasns = connection()
        cur = trasns.cursor()
        # cur.execute(f"SELECT * FROM `contractawards_db`.`ContractAwardFinal` WHERE id = 474881")  # For test
        cur.execute(f"SELECT * FROM ContractAwardFinal WHERE is_english = '1' AND `col1` IN ({str(Global_var.Source_Name)}) ORDER BY id ASC")  # 0 = English, 1 = Non-English
        rows = cur.fetchall()

        if len(rows) == 0:
            browser.quit()
            wx.MessageBox(' -_-  No Contract Award Available For Translation -_- ', 'Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_INFORMATION)
            time.sleep(2)
            sys.exit()

        print(f' Total Contract Award Found For Translation : {len(rows)}')
        count = 0
        Tender_count_for_Refresh = 0
        # global Exception_loop
        # Exception_loop = True
        # while Exception_loop == True:
        for row in rows:
            try:
                try:
                    browser.switch_to.window(browser.window_handles[1])
                    time.sleep(1)
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
                    time.sleep(1)
                except:
                    pass
                id = "%s" % (row["id"])
                source = "%s" % (html.unescape(row["col1"]))
                notice_no = "%s" % (html.unescape(row["ref_number"]))
                purchaser = "%s" % (html.unescape(row["purchasername"]))
                address = "%s" % (html.unescape(row["purchaseradd"]))
                contractorname = "%s" % (html.unescape(row["contractorname"]))
                cont_add = "%s" % (html.unescape(row["cont_add"]))
                title = "%s" % (html.unescape(row["short_descp"]))
                description = "%s" % (html.unescape(row["award_detail"]))

                en_notice_no = ''
                en_purchaser = ''
                en_address = ''
                en_title = ''
                en_description = ''
                en_contractorname = ''
                en_cont_add = ''

                en_notice_no_done = False
                en_purchaser_done = False
                en_address_done = False
                en_title_done = False
                en_description_done = False
                en_contractorname_done = False
                en_cont_add_done = False

                print(f'Selected Source : {Global_var.Source_Name}')
                print(f'Id : {id}')
                print(f'Source : {source}')

                if not re.match("^[\W A-Za-z0-9_@?./#&+-]*$", notice_no):
                    is_available = 1
                    # click_on_clear()
                    # check_translated_textarea()
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            notice_no = re.sub('\s+', ' ', notice_no)
                            notice_no = notice_no.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(notice_no))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        for output_xpath in output_xpath_list:
                            for en_notice_no in browser.find_elements_by_xpath(output_xpath):
                                en_notice_no = en_notice_no.get_attribute('innerText').replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_notice_no_done = True
                                break
                            if en_notice_no_done == True:
                                break
                        if en_notice_no_done == False:
                            click_on_tryagain()
                else:
                    en_notice_no = notice_no
                    en_notice_no_done = True
                print(f'Notice_No : {en_notice_no}')

                is_available = 1
                if purchaser != '':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            purchaser = re.sub('\s+', ' ', purchaser)
                            purchaser = purchaser.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(purchaser))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_purchaser in browser.find_elements_by_xpath(output_xpath):
                                en_purchaser = en_purchaser.get_attribute('innerText').upper().replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_purchaser_done = True
                                break
                            if en_purchaser_done == True:
                                break
                        if en_purchaser_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_purchaser = purchaser
                        #     en_purchaser_done = True
                else:
                    en_purchaser = purchaser
                    en_purchaser_done = True

                en_purchaser = en_purchaser.upper()
                print(f'Purchaser : {en_purchaser}')

                is_available = 1
                if address !='':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            address = re.sub('\s+', ' ', address)
                            address = address.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(address))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_address in browser.find_elements_by_xpath(output_xpath):
                                en_address = en_address.get_attribute('innerText').replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_address_done = True
                                break
                            if en_address_done == True:
                                break
                        if en_address_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_address = address
                        #     en_address_done = True
                else:
                    en_address = address
                    en_address_done = True
                print(f'Pur_Address : {en_address}')

                is_available = 1
                if contractorname != '':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            contractorname = re.sub('\s+', ' ', contractorname)
                            contractorname = contractorname.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(contractorname))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_contractorname in browser.find_elements_by_xpath(output_xpath):
                                en_contractorname = en_contractorname.get_attribute('innerText').upper().replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_contractorname_done = True
                                break
                            if en_contractorname_done == True:
                                break
                        if en_contractorname_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_contractorname = contractorname
                        #     en_contractorname_done = True
                else:
                    en_contractorname = contractorname
                    en_contractorname_done = True

                en_contractorname = en_contractorname.upper()
                print(f'Contractor : {en_contractorname}')

                is_available = 1
                if cont_add !='':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            cont_add = re.sub('\s+', ' ', cont_add)
                            cont_add = cont_add.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(cont_add))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_cont_add in browser.find_elements_by_xpath(output_xpath):
                                en_cont_add = en_cont_add.get_attribute('innerText').replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_cont_add_done = True
                                break
                            if en_cont_add_done == True:
                                break
                        if en_cont_add_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_cont_add = cont_add
                        #     en_cont_add_done = True
                else:
                    en_cont_add = cont_add
                    en_cont_add_done = True
                print(f'Cont_Address : {en_cont_add}')

                is_available = 1
                if title != "":
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            title = re.sub('\s+', ' ', title)
                            title = title.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            i.send_keys(str(title))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_title in browser.find_elements_by_xpath(output_xpath):
                                en_title = en_title.get_attribute('innerText').replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_title_done = True
                                break
                            if en_title_done == True:
                                break
                        if en_title_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_title = title
                            # en_title_done = True
                else:
                    en_title = title
                    en_title_done = True
                en_title = casesensitive(en_title)
                print(f'Title : {en_title}')

                is_available = 1
                if description != "":
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            # i.clear()
                            i.send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                            time.sleep(1)
                            # i.send_keys(Keys.BACKSPACE)
                            check_translated_textarea()
                            description = re.sub('\s+', ' ', description)
                            description = description.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n').strip()
                            if len(description) >= 1200:
                                description = description[:1200] + '...'
                            i.send_keys(str(description))
                            time.sleep(4)
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award Tender Google Translation Exe ', wx.OK | wx.ICON_WARNING)
                        time.sleep(2)
                        # something_Went_wrong() # if Chrome Hanged or some other thing happend with chrome
                    else:
                        time.sleep(2)
                        # if If_other_Than_English == True:
                        for output_xpath in output_xpath_list:
                            for en_description in browser.find_elements_by_xpath(output_xpath):
                                en_description = en_description.get_attribute('innerText').replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\").strip()
                                en_description_done = True
                                break
                            if en_description_done == True:
                                break
                        if en_description_done == False:
                            click_on_tryagain()
                        # else:
                        #     en_description = description
                        #     en_description_done = True
                else:
                    en_description = description
                    en_description_done = True

                print(f'Details : {en_description}')

                # en_notice_no = en_notice_no.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_purchaser = en_purchaser.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_address = en_address.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_title = en_title.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_description = en_description.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_contractorname = en_contractorname.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                # en_cont_add = en_cont_add.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")

                if len(en_title) > 250:
                    en_title = en_title[:246]
                    suffix = "'" 
                    suffix2 = "''"
                    if suffix2 and en_title.endswith(suffix2):
                        pass
                    elif suffix and en_title.endswith(suffix):
                        en_title = en_title[:-len(suffix)]
                    en_title = en_title + '...'

                if len(en_address) > 500:
                    en_address = en_address[:500]
                    suffix = "'"
                    suffix2 = "''"
                    if suffix2 and en_address.endswith(suffix2):
                        pass
                    elif suffix and en_address.endswith(suffix):
                        en_address = en_address[:-len(suffix)]
                    en_address = en_address + '...'

                if en_notice_no_done == True and en_purchaser_done == True and en_address_done == True and en_title_done == True and en_description_done == True and en_contractorname_done == True and en_cont_add_done == True:
                    a = False
                    while a == False:
                        try:
                            trasns = connection()
                            cur = trasns.cursor()
                            Update_Website_Status = f"UPDATE ContractAwardFinal SET is_english = '0', ref_number='{en_notice_no}',purchasername='{en_purchaser}',purchaseradd='{en_address}',contractorname='{en_contractorname}',cont_add='{en_cont_add}',short_descp='{en_title}',award_detail='{en_description}' WHERE id = '{id}'"
                            # print(Update_Website_Status)
                            cur.execute(Update_Website_Status)
                            trasns.commit()
                            a = True
                        except Exception as e:
                            print('ERROR ON UPDATE QUERY EXCEPTION\n')
                            Print_Exception_detail(e)
                            trasns.close()
                            a = False
                            time.sleep(5)
                count += 1
                print(f'Translation Completed : {count}  / {len(rows)}\n')
                # Exception_loop = False
                Tender_count_for_Refresh += 1
                if Tender_count_for_Refresh == 25:
                    Tender_count_for_Refresh = 0
                    clear = lambda: os.system('cls')  # Clear command Prompt
                    clear()
                    browser.delete_all_cookies()
                    try:
                        browser.execute_script("window.open('');")
                        browser.switch_to.window(browser.window_handles[1])
                        browser.get('chrome://settings/clearBrowserData')
                        time.sleep(2)
                        actions = ActionChains(browser) 
                        actions.send_keys(Keys.TAB * 7 + Keys.ENTER) # confirm
                        actions.perform()
                        time.sleep(10) # wait some time to finish
                        browser.close()
                        time.sleep(1)
                        browser.switch_to.window(browser.window_handles[0])
                    except:
                        pass
                    # browser.execute_script("location.reload(true);")
                    time.sleep(4)
                    print(f'Translation Completed : {count}  / {len(rows)}\n')
                    
            except Exception as e:
                print('Error On translation Funtion\n')
                Print_Exception_detail(e)
                try:
                    browser.get('https://translate.google.com/')
                except:
                    wx.MessageBox(' -_- Please Refresh The Page Then Click On OK MessageBox -_- ','Contract Award Tender Google Translation Exe',wx.OK | wx.ICON_ERROR)
                time.sleep(2)
                # Exception_loop = True
        tarnslation()
    except Exception as e:
        print('Error On Main Exception\n')
        Print_Exception_detail(e)
        wx.MessageBox(' -_- (ERROR ON MAIN EXCEPTION) -_- ',' Contract Award Tender Google Translation Exe ',wx.OK | wx.ICON_ERROR)
        browser.quit()
        time.sleep(2)
        sys.exit()


tarnslation()