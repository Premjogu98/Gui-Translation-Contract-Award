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
app = wx.App()

chrome_options = Options()
chrome_options.add_extension('C:\\Translation EXE\\BrowsecVPN.crx')
browser = webdriver.Chrome(executable_path=str(f"C:\\Translation EXE\\chromedriver.exe"),chrome_options=chrome_options)
browser.maximize_window()
# browser.get("""https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh?hl=en" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh%3Fhl%3Den&amp;ved=2ahUKEwivq8rjlcHmAhVtxzgGHZ-JBMgQFjAAegQIAhAB""")
wx.MessageBox(' -_-  Add Extension and Then Click On OK BUTTON -_- ', 'Contract Award GUI Google Translation', wx.OK | wx.ICON_ERROR)
time.sleep(5)
try:
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
except:
    browser.switch_to.window(browser.window_handles[0])
browser.get('https://translate.google.com/')

input_xpath_list = ['//*[@id="source"]','//*[@aria-label="Source text"]']
output_xpath_list = ['//*[@class="tlid-translation translation"]','//*[@class="VIiyi"]']
Clear_xpath_list = ['//*[@aria-label="Clear source text"]/i','//*[@class="clear-wrap"]/div/div']
def connection():
    a3 = 0
    while a3 == 0:
        try:
            connection = pymysql.connect(host='185.142.34.92',user='ams',password='TgdRKAGedt%h',db='contractawards_db',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            return connection
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname,"\n", exc_tb.tb_lineno)
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

def click_on_clear():
    click_clear = False
    while click_clear == False:
        for Clear_xpath in Clear_xpath_list:
            try:
                for clear_btn in browser.find_elements_by_xpath(Clear_xpath):
                    click_clear = True
                    clear_btn.click()
                    time.sleep(2)
                    break
            except:
                pass  
            if click_clear == True:
                break
        if click_clear == False:
            print('Clear Button Not Found')
            time.sleep(2)
            
def click_on_tryagain():
    print(' -_-  Please wait browser will be refresh automatically after 30 SEC === NO OUTPUT FOUND === -_- ')
    time.sleep(30)
    try_btn_found = False
    try:
        for try_again_btn in browser.find_elements_by_xpath('//*[@class="tlid-result-container-error-button translation-error-button"]'):
            try_again_btn.click()
            try_btn_found = True
            break
    except:
        pass
    if try_btn_found == False:
        browser.refresh()
        time.sleep(5)
        for i in browser.find_elements_by_xpath('//*[@id="source"]'):
            click_on_clear()
            i.clear()
            break
    time.sleep(2)


def language_detect():
    If_other_Than_English = True
    for language_detect in browser.find_elements_by_xpath('//*[@class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-right jfk-button-checked"]'):
        language_detect = language_detect.get_attribute('innerText').lower()
        if 'english' not in language_detect:
            If_other_Than_English = True
        else:
            If_other_Than_English = False
        break
    return If_other_Than_English


def tarnslation():
    try:
        
        trasns = connection()
        cur = trasns.cursor()
        # cur.execute(f"SELECT * FROM `tenders_db`.`l2l_tenders_tbl` WHERE Posting_Id='523417'")  # For test
        cur.execute(f"SELECT * FROM ContractAwardFinal WHERE is_english = '1' AND `col1` IN ({str(Global_var.Source_Name)}) ORDER BY id ASC")  # 0 = English, 1 = Non-English
        rows = cur.fetchall()

        if len(rows) == 0:
            wx.MessageBox(' -_-  No Contract Award Available For Translation -_- ', 'Contract Award GUI Google Translation ', wx.OK | wx.ICON_INFORMATION)
            time.sleep(2)
            browser.close()
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
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
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
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            notice_no = re.sub('\s+', ' ', notice_no)
                            notice_no = notice_no.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(notice_no))
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(5)
                        for output_xpath in output_xpath_list:
                            for en_notice_no in browser.find_elements_by_xpath(output_xpath):
                                en_notice_no = en_notice_no.get_attribute('innerText')
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
                            click_on_clear()
                            i.clear()
                            purchaser = re.sub('\s+', ' ', purchaser)
                            purchaser = purchaser.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(purchaser))
                            time.sleep(5)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_purchaser in browser.find_elements_by_xpath(output_xpath):
                                    en_purchaser = en_purchaser.get_attribute('innerText').upper()
                                    en_purchaser_done = True
                                    break
                                if en_purchaser_done == True:
                                    break
                            if en_purchaser_done == False:
                                click_on_tryagain()
                        else:
                            en_purchaser = purchaser
                            en_purchaser_done = True
                else:
                    en_purchaser = purchaser
                    en_purchaser_done = True

                en_purchaser = en_purchaser.upper()
                print(f'Purchaser : {en_purchaser}')

                is_available = 1
                if address !='':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            address = re.sub('\s+', ' ', address)
                            address = address.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(address))
                            time.sleep(4)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_address in browser.find_elements_by_xpath(output_xpath):
                                    en_address = en_address.get_attribute('innerText')
                                    en_address_done = True
                                    break
                                if en_address_done == True:
                                    break
                            if en_address_done == False:
                                click_on_tryagain()
                        else:
                            en_address = address
                            en_address_done = True
                else:
                    en_address = address
                    en_address_done = True
                print(f'Pur_Address : {en_address}')

                is_available = 1
                if contractorname != '':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            contractorname = re.sub('\s+', ' ', contractorname)
                            contractorname = contractorname.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(contractorname))
                            time.sleep(5)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_contractorname in browser.find_elements_by_xpath(output_xpath):
                                    en_contractorname = en_contractorname.get_attribute('innerText').upper()
                                    en_contractorname_done = True
                                    break
                                if en_contractorname_done == True:
                                    break
                            if en_contractorname_done == False:
                                click_on_tryagain()
                        else:
                            en_contractorname = contractorname
                            en_contractorname_done = True
                else:
                    en_contractorname = contractorname
                    en_contractorname_done = True

                en_contractorname = en_contractorname.upper()
                print(f'Contractor : {en_contractorname}')

                is_available = 1
                if cont_add !='':
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            cont_add = re.sub('\s+', ' ', cont_add)
                            cont_add = cont_add.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(cont_add))
                            time.sleep(4)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_cont_add in browser.find_elements_by_xpath(output_xpath):
                                    en_cont_add = en_cont_add.get_attribute('innerText')
                                    en_cont_add_done = True
                                    break
                                if en_cont_add_done == True:
                                    break
                            if en_cont_add_done == False:
                                click_on_tryagain()
                        else:
                            en_cont_add = cont_add
                            en_cont_add_done = True
                else:
                    en_cont_add = cont_add
                    en_cont_add_done = True
                print(f'Cont_Address : {en_cont_add}')

                is_available = 1
                if title != "":
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            title = re.sub('\s+', ' ', title)
                            title = title.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            i.send_keys(str(title))
                            time.sleep(5)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_title in browser.find_elements_by_xpath(output_xpath):
                                    en_title = en_title.get_attribute('innerText')
                                    en_title_done = True
                                    break
                                if en_title_done == True:
                                    break
                            if en_title_done == False:
                                click_on_tryagain()
                        else:
                            en_title = title
                            en_title_done = True
                else:
                    en_title = title
                    en_title_done = True
                en_title = casesensitive(en_title)
                print(f'Title : {en_title}')

                is_available = 1
                if description != "":
                    for input_xpath in input_xpath_list:
                        for i in browser.find_elements_by_xpath(input_xpath):
                            click_on_clear()
                            i.clear()
                            description = re.sub('\s+', ' ', description)
                            description = description.replace('<br>','<br>\n').replace('<BR>','<br>\n').replace('<Br>','<br>\n')
                            check_translated_textarea()
                            if len(description) >= 1200:
                                description = description[:1200] + '...'
                            i.send_keys(str(description))
                            time.sleep(5)
                            If_other_Than_English = language_detect()
                            is_available = 0
                            break
                        if is_available == 0:
                            break
                    if is_available == 1:
                        wx.MessageBox('Something Went Wrong Please Refresh Google Translation Page Then Click On -_- OK -_- ','Contract Award GUI Google Translation ', wx.OK | wx.ICON_WARNING)
                    else:
                        time.sleep(1)
                        if If_other_Than_English == True:
                            for output_xpath in output_xpath_list:
                                for en_description in browser.find_elements_by_xpath(output_xpath):
                                    en_description = en_description.get_attribute('innerText')
                                    en_description_done = True
                                    break
                                if en_description_done == True:
                                    break
                            if en_description_done == False:
                                click_on_tryagain()
                        else:
                            en_description = description
                            en_description_done = True
                else:
                    en_description = description
                    en_description_done = True

                print(f'Details : {en_description}')

                en_notice_no = en_notice_no.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_purchaser = en_purchaser.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_address = en_address.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_title = en_title.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_description = en_description.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_contractorname = en_contractorname.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")
                en_cont_add = en_cont_add.replace("'", "''").replace("< ", "<").replace(" >", ">").replace("</ ", "</").replace("\\", "\\\\")

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
                            print(f'ERROR ON UPDATE QUERY EXCEPTION: {e}')
                            trasns.close()
                            a = False
                            time.sleep(5)
                count += 1
                print(f'Translation Completed : {count}  / {len(rows)}\n')
                # Exception_loop = False
                Tender_count_for_Refresh += 1
                if Tender_count_for_Refresh == 100:
                    Tender_count_for_Refresh = 0
                    clear = lambda: os.system('cls')  # Clear command Prompt
                    clear()
                    browser.delete_all_cookies()
                    browser.execute_script("location.reload(true);")
                    time.sleep(4)
                    print(f'Translation Completed : {count}  / {len(rows)}\n')
                    
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname,"\n",exc_tb.tb_lineno)
                browser.get('https://translate.google.com/')
                time.sleep(2)
                # Exception_loop = True
        tarnslation()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",exc_tb.tb_lineno)
        time.sleep(2)
        wx.MessageBox(' -_- (ERROR ON MAIN EXCEPTION) -_- ','Contract Award GUI Google Translation ',wx.OK | wx.ICON_ERROR)
        time.sleep(2)
        browser.close()
        sys.exit()


tarnslation()