'''
import pandas as pd 
from OdcesForms import SeleniumAbid
import time

df = pd.read_csv("C:/Users/Abid B/Documents/roster.csv")
print (df)

from csv import reader
SeleniumAbid.driver.set_page_load_timeout(30)


##################TEST DATA##########################
worker = "Joy Hinshilwood"
Date = "7/8/2021"
Name = "The Guidance Center"
Starttime = "09:41 AM"
Endtime = "09:43 AM"
Phone = 5625951159
Address = "1301 Pine Ave"
City = "Long Beach"
State = "California"
County = "Los Angeles County"
ZipCode = "90813"
Outcome = "Spoke with someone; they're not interested"
CTAudience = "Corporation: Employees"
Spanish = "NO"
Industry = "Mental Health Service"
################TEST DATA############################



SeleniumAbid.driver.get("https://na0.icarol.com/secure/signon.aspx?ReturnUrl=%2fsecure%2fdefault.aspx")
SeleniumAbid.driver.find_element_by_id("txtEmail").send_keys("abakhtiyar@alterhealthgroup.com")
SeleniumAbid.driver.find_element_by_id("txtPW").send_keys("CsufTitans2021!")
SeleniumAbid.driver.find_element_by_id("btnSignOn").click()

SeleniumAbid.driver.find_element_by_id("hlReports").click()
SeleniumAbid.driver.find_element_by_id("cphBody_hlNewCallReport").click()
SeleniumAbid.driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/table/tbody/tr/td[1]/div/a[5]").click()


with open('C:/Users/Abid B/Downloads/CSC OUTREACH 1st Attempt Log - SHIFT1 (8AM - 12PM) 6917.csv', 'r') as read_obj:
    y=0
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            if str(df.iloc[y]["PHONE"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_txtLookupPhoneV4").send_keys(str(df.iloc[y]["PHONE"]))  
            SeleniumAbid.driver.find_element_by_id("cphBody_ddVolunteer").send_keys(str(df.iloc[y]["CSC NAME"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtCaller").send_keys(str(df.iloc[y]["FACILITY"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtStartTime").clear()
            SeleniumAbid.driver.find_element_by_id("cphBody_txtStartTime").send_keys(str(df.iloc[y]["CALL START TIME"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtEndTime").send_keys(str(df.iloc[y]["CALL END TIME"]))
            if str(df.iloc[y]["ADDRESS"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_txtAddress").send_keys(str(df.iloc[y]["ADDRESS"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtLookupPostalCode").send_keys(int(df.iloc[y]["CITY OR ZIP"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_btnLookupPostalCode").click()
            #a = SeleniumAbid.ActionChains(SeleniumAbid.driver)
            #SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").a.key_down(SeleniumAbid.Keys.CONTROL).send_keys('a').a.key_up(SeleniumAbid.Keys.CONTROL).perform()
            
            if str(df.iloc[y]["PHONE"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_txtLookupPhoneV4").send_keys(str(df.iloc[y]["PHONE"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(SeleniumAbid.Keys.BACKSPACE)
            SeleniumAbid.driver.find_element_by_id("cphBody_txtDateOfCall").send_keys(str(df.iloc[y]["DATE"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_465356").send_keys(str(df.iloc[y]["OUTCOME"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_465357").send_keys(str(df.iloc[y]["CATEGORY & TARGET AUDIENCE"]))
            if str(df.iloc[y]["INDUSTRY"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_465360").send_keys(str(df.iloc[y]["INDUSTRY"]))
            if str(df.iloc[y]["EMAIL (If Interested)"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_465363").send_keys(str(df.iloc[y]["EMAIL (If Interested)"]))
            if str(df.iloc[y]["NOTES"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_465361").send_keys(str(df.iloc[y]["NOTES"]))
            if str(df.iloc[y]["SPANISH (Y/N)"]) != 'nan':
                SeleniumAbid.driver.find_element_by_id("cphBody_cbl465359_0").click()
            else:
                SeleniumAbid.driver.find_element_by_id("cphBody_cbl465359_1").click()
            #time.sleep(10)
            #SeleniumAbid.driver.find_element_by_id("cphBody_btnReportSubmit").click()

            #time.sleep(10)
            SeleniumAbid.driver.refresh()
            print("done")
            y += 1

print ("entry done " + y + " times")


SeleniumAbid.driver.find_element_by_id("hlMessaging").click()
SeleniumAbid.driver.find_element_by_id("cphBody_hlConfigureServices").click()
SeleniumAbid.driver.find_element_by_id("ui-id-4").click()
select = SeleniumAbid.Select(SeleniumAbid.driver.find_element_by_id("cphBody_ddPortal"))
select.select_by_value('NULL')

SeleniumAbid.driver.find_element_by_id("cphBody_rblMessageType_2").click()
SeleniumAbid.driver.find_element_by_id('cphBody_chkMessageMakeVisibleToAllPortals').click()
#SeleniumAbid.driver.find_element_by_id("cphBody_rblMessageType_2").click()
with open('C:/Users/Abid B/Documents/roster.csv', 'r') as read_obj:
    y=0
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        
        for row in csv_reader:
            SeleniumAbid.driver.find_element_by_id("cphBody_txtStandardMessageTitle").send_keys(str(df.iloc[y]["Name"]))
            SeleniumAbid.driver.find_element_by_id("cphBody_txtStandardMessageText").send_keys("Hi, my name is " + str(df.iloc[y]["Chat Name"])+ ", how can I support you today?")
            SeleniumAbid.driver.find_element_by_id("cphBody_txtStandardMessageOrderInLists").send_keys(str(df.iloc[y]["Order Number"]))
            #SeleniumAbid.driver.find_element_by_id('cphBody_chkMessageMakeVisibleToAllPortals').click()
            SeleniumAbid.driver.find_element_by_id("cphBody_btnAddNewStandardMessage").click()
            #time.sleep(15)
            print("done")
            y += 1
'''