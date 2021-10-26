from OdcesForms import *
from OdcesForms import IndiLog
from OdcesForms import AduAssess
from OdcesForms import ChiAssess
from OdcesForms import GroupEncounterLog
from OdcesForms import iCarolIndiLog
import datetime
import time 
#import testData
import pandas as pd 
from OdcesForms import WeekTally
pd.set_option("display.max_rows", 10, "display.max_columns", 100)
df = pd.read_csv('IndividualEncounterLog.csv')
df = df.fillna(0)
from csv import reader 
uName = ""
pWord = ""
def main(UN, PW):
    uName = UN
    pWord = PW
    y = 0
    whyareyoulikethis = 0
    SeleniumAbid.driver.set_page_load_timeout(30)
                
    #Main Login Page
    SeleniumAbid.driver.get("https://ccpdata.org/ccp2field/")
                
    #UserName and Password 
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtLogin").send_keys(uName)
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtPassword").send_keys(pWord)
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
    '''
    def workerID(df, y):
        WorkerNum = df.iloc[y]["WorkerNum"]
        if WorkerNum == 162047:
            df.at[y, "WorkerNum"] = 1234 #Abid
            print (df.iloc[y]["WorkerNum"])
        if WorkerNum == 162458:
            df.at[y, "WorkerNum"] = 10053 #CAguayo
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162486:
            df.at[y, "WorkerNum"] = 9924 #JAyinla
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162456:
            df.at[y, "WorkerNum"] = 9815 #MBayona
        elif WorkerNum == 164257:
            df.at[y, "WorkerNum"] = 11407 #BBlake
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162490:
            df.at[y, "WorkerNum"] = 9928 #VBostic
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162494:
            df.at[y, "WorkerNum"] = 10469 #SBrown
        elif WorkerNum == 164682:
            df.at[y, "WorkerNum"] = 11518 #SCampos
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162523:
            df.at[y, "WorkerNum"] = 9812 #TCochran
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162485:
            df.at[y, "WorkerNum"] = 9923 #DDixon
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162478:
            df.at[y, "WorkerNum"] = 9867 #KDOonovan
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162489:
            df.at[y, "WorkerNum"] = 9927
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162482:
            df.at[y, "WorkerNum"] = 9921 #RFelleke   
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162460: 
            df.at[y, "WorkerNum"] = 9858 #JGarcia
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 164256:
            df.at[y, "WorkerNum"] = 11406 #AGardner 
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 164252:
            df.at[y, "WorkerNum"] = 11295 #KGofigan
            print (df.iloc[y]["WorkerNum"]) 
        elif WorkerNum == 164255:
            df.at[y, "WorkerNum"] = 11296 #TGofigan
            print (df.iloc[y]["WorkerNum"]) 
        elif WorkerNum == 162453:
            df.at[y, "WorkerNum"] = 9813 #IGutierrez  
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162476:
            df.at[y, "WorkerNum"] = 10198 #PGutierrez    
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 163492:
            df.at[y, "WorkerNum"] = 11107 #IHidalgo
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162492: 
            df.at[y, "WorkerNum"] = 9931 #JHinshilwood
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162483:
            df.at[y, "WorkerNum"] = 9920 #AJones
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 163494:
            df.at[y, "WorkerNum"] = 11280 #KLopezvito
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 164254:
            df.at[y, "WorkerNum"] = 11039 #ALovest
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 164676:
            df.at[y, "WorkerNum"] = 11519 #RManfredo
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum ==  162454:
            df.at[y, "WorkerNum"] = 9863 #CMeijia
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162477:
            df.at[y, "WorkerNum"] = 9864 #LMiranda
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162475:
            df.at[y, "WorkerNum"] = 9862 #DPerez
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 163497:
            df.at[y, "WorkerNum"] = 11106 #RPollard
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162494:
            df.at[y, "WorkerNum"] = 10466 #APungi
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162474:
            df.at[y, "WorkerNum"] = 9861 #BRamos
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162473:
            df.at[y, "WorkerNum"] = 9859 #VRodriguez
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162457:
            df.at[y, "WorkerNum"] = 9929 #MSallus
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162459:
            df.at[y, "WorkerNum"] = 9934 #LScott
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162479:
            df.at[y, "WorkerNum"] = 9868 #PSinha
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162480:
            df.at[y, "WorkerNum"] = 9914 #BTamayo
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162491:
            df.at[y, "WorkerNum"] = 9933 #EVizcarra
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 162487:
            df.at[y, "WorkerNum"] = 9925 #JWiggington
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 163499:
            df.at[y, "WorkerNum"] = 11181 #KZamora
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 166942:
            df.at[y, "WorkerNum"] = 11737 #DMadrigal
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 166943:
            df.at[y, "WorkerNum"] = 11739 #JNorfolk 
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 166940:
            df.at[y, "WorkerNum"] = 11738 #PStickles 
            print (df.iloc[y]["WorkerNum"])
        elif WorkerNum == 166941:
            df.at[y, "WorkerNum"] = 11736 #SKalantari
            print (df.iloc[y]["WorkerNum"])
        '''
    with open('IndividualEncounterLog.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader: 
                IndiLog.start(y, df)
                y += 1
                '''
                #workerID(df, y)
                #if y == 6: d
                    #print (df.loc[[y]])
                if int(df.iloc[y]["Report Version"]) == 60404:
                    iCarolIndiLog.start(y, df)
                    print("done Individual Log ")
                #y += 1
                elif int(df.iloc[y]["Report Version"]) == 60433:
                    AduAssess.start(y, df)
                    print("done " + str(df.iloc[y]["Report Version"]) + " Adult Assessment Log ")
                elif int(df.iloc[y]["Report Version"]) == 60434:
                    ChiAssess.start(y, df)
                    print("done " + str(df.iloc[y]["Report Version"]) + " Child Assessment Log ")
                elif int(df.iloc[y]["Report Version"]) == 60432:
                    GroupEncounterLog.start(y, df)
                    print("done " + str(df.iloc[y]["Report Version"]) + " Group Encounter Log")
                #else:
                    #WeekTally.start(y)
                    #print("done Weekly Tally")
                #time.sleep(30)
                #counter+=1
                #print("done " + str(df.iloc[y]["Report Version"]) + "Individual Log ")
                y += 1   
                #print(x)
                '''
       
    '''
    with open('WeekTall.csv', 'r') as read_obj1:
        print ("x = " + str(whyareyoulikethis))
        csv_reader1 = reader(read_obj1)
        header = next(csv_reader1)
        if header != None:
            for row in csv_reader1:
                WeekTally.start(whyareyoulikethis)
                print("done Weekly Tally")
                whyareyoulikethis += 1
                print(whyareyoulikethis)
    '''    
main("media@alterrecovery.com", "ClaireSucks123!")            