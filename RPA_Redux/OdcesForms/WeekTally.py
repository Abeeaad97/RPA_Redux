from OdcesForms import SeleniumAbid as sa
import pandas as pd
import ProgramSetting

pd.set_option("display.max_rows", 10, "display.max_columns", 100)

   
    
def weeklyWorkerId(y, df):
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
        df.at[y, "WorkerNum"] = 9920	 #AJones
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
    elif WorkerNum == 162493:
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
def enterTally(counter, df):
    #Sunday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSunday13").send_keys(int(df.iloc[counter]["Q1Sunday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSunday14").send_keys(int(df.iloc[counter]["Q2Sunday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSunday15").send_keys(int(df.iloc[counter]["Q3Sunday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSunday21").send_keys(int(df.iloc[counter]["Q4Sunday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSunday25").send_keys(int(df.iloc[counter]["Q5Sunday"]))
    #Monday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtMonday13").send_keys(int(df.iloc[counter]["Q1Monday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtMonday14").send_keys(int(df.iloc[counter]["Q2Monday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtMonday15").send_keys(int(df.iloc[counter]["Q3Monday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtMonday21").send_keys(int(df.iloc[counter]["Q4Monday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtMonday25").send_keys(int(df.iloc[counter]["Q5Monday"]))
    #Tuesday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtTuesday13").send_keys(int(df.iloc[counter]["Q1Tuesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtTuesday14").send_keys(int(df.iloc[counter]["Q2Tuesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtTuesday15").send_keys(int(df.iloc[counter]["Q3Tuesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtTuesday21").send_keys(int(df.iloc[counter]["Q4Tuesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtTuesday25").send_keys(int(df.iloc[counter]["Q5Tuesday"]))
    #Wednesday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWednesday13").send_keys(int(df.iloc[counter]["Q1Wednesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWednesday14").send_keys(int(df.iloc[counter]["Q2Wednesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWednesday15").send_keys(int(df.iloc[counter]["Q3Wednesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWednesday21").send_keys(int(df.iloc[counter]["Q4Wednesday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWednesday25").send_keys(int(df.iloc[counter]["Q5Wednesday"]))
    #Thursday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtThursday13").send_keys(int(df.iloc[counter]["Q1Thursday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtThursday14").send_keys(int(df.iloc[counter]["Q2Thursday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtThursday15").send_keys(int(df.iloc[counter]["Q3Thursday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtThursday21").send_keys(int(df.iloc[counter]["Q4Thursday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtThursday25").send_keys(int(df.iloc[counter]["Q5Thursday"]))
    #Friday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtFriday13").send_keys(int(df.iloc[counter]["Q1Friday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtFriday14").send_keys(int(df.iloc[counter]["Q2Friday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtFriday15").send_keys(int(df.iloc[counter]["Q3Friday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtFriday21").send_keys(int(df.iloc[counter]["Q4Friday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtFriday25").send_keys(int(df.iloc[counter]["Q5Friday"]))
    #Saturday
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSaturday13").send_keys(int(df.iloc[counter]["Q1Saturday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSaturday14").send_keys(int(df.iloc[counter]["Q2Saturday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSaturday15").send_keys(int(df.iloc[counter]["Q3Saturday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSaturday21").send_keys(int(df.iloc[counter]["Q4Saturday"]))
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtSaturday25").send_keys(int(df.iloc[counter]["Q5Saturday"]))
    
def start(x):
    #print("x = " + str(x))
    counter = x
    
    #print("counter = " + str(counter))
    df = pd.read_csv('C:/Users/Abid B/RPA_Redux/weekTall.csv')
    df = df.fillna(0)
    #print (df)

    sa.driver.find_element_by_id("UCSideNav_HyperLink31").click()
    ProgramSetting.weeklyProg()
    select = sa.Select(sa.driver.find_element_by_id("ContentPlaceHolder1_ddlCounty"))
    #sa.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(str(92804))
    select.select_by_value('216')
    weekbeginning = df.iloc[counter]["Dates"]
    date = weekbeginning.split("-")
    print(date[0])
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWeekBeginning").clear()
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtWeekBeginning").send_keys(str(date[0]))
    weeklyWorkerId(counter, df)
    sa.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(int(df.iloc[counter]["WorkerNum"]))
    enterTally(counter, df)
    sa.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
