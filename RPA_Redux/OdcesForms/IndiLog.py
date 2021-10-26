from OdcesForms import SeleniumAbid
from OdcesForms import zipCodeDirectory
from OdcesForms import ProgramSetting
import testData
import pandas as pd 
import time
import datetime
#driver = webdriver.Chrome("C:/Users/Abid B/Odces_RPA/Drivers/chromedriver.exe")

#Determine the visit type
def visitType (counter, data):
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_0").click()
    '''
    print(data.iloc[counter]["Number of People"])
    if data.iloc[counter]["Number of People"] == 1:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_0").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_0").click()
    elif data.iloc[counter]["Number of People"] == 2:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_1").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_1").click()
    elif data.iloc[counter]["Number of People"] == 3: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_2").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_2").click()
    elif data.iloc[counter]["Number of People"] == 4: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_3").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_3").click()
    elif data.iloc[counter]["Number of People"] == 5: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_4").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_4").click()
    elif str(data.iloc[counter]["Number of People"]) == '6 or more':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_5").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_5").click()
    '''
#determine the visit number 
def visitNumber (data, counter):
    print(data.iloc[counter]["VISIT NUMBER"])
    if str(data.iloc[counter]["VISIT NUMBER"]) == '1':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
    elif str(data.iloc[counter]["VISIT NUMBER"]) == '2':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_1").click() 
    elif str(data.iloc[counter]["VISIT NUMBER"]) == '3':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_2").click()
    elif str(data.iloc[counter]["VISIT NUMBER"]) == '4': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_3").click()
    elif str(data.iloc[counter]["VISIT NUMBER"]) == '5+':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_4").click()   
        
def visitDuration(data, counter):
    if str(data.iloc[counter]["DURATION"]) == '15 - 29 minutes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_0").click()
    elif str(data.iloc[counter]["DURATION"]) == '30 - 44 minutes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_1").click()
    elif str(data.iloc[counter]["DURATION"]) == '45 - 59 minutes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_2").click()
    elif str(data.iloc[counter]["DURATION"]) == '60+ minutes':   
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_3").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_0").click()
        '''       

    if int(data.iloc[counter]["MalePre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMalePreschool").send_keys(int(data.iloc[counter]["MalePre"])) 
    if int(data.iloc[counter]["MaleChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleChild").send_keys(int(data.iloc[counter]["MaleChi"]))
    if int(data.iloc[counter]["MaleAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdolescent").send_keys(int(data.iloc[counter]["MaleAdo"]))
    if int(data.iloc[counter]["MaleAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult18").send_keys(int(data.iloc[counter]["MaleAdu"]))
    if int(data.iloc[counter]["MaleOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult40").send_keys(int(data.iloc[counter]["MaleOldAdu"]))
    if int(data.iloc[counter]["MaleSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult65").send_keys(int(data.iloc[counter]["MaleSen"]))
    
    if int(data.iloc[counter]["FemalePre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemalePreschool").send_keys(int(data.iloc[counter]["FemalePre"])) 
    if int(data.iloc[counter]["FemaleChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleChild").send_keys(int(data.iloc[counter]["FemaleChi"]))
    if int(data.iloc[counter]["FemaleAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdolescent").send_keys(int(data.iloc[counter]["FemaleAdo"]))
    if int(data.iloc[counter]["FemaleAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult18").send_keys(int(data.iloc[counter]["FemaleAdu"]))
    if int(data.iloc[counter]["FemaleOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult40").send_keys(int(data.iloc[counter]["FemaleOldAdu"]))
    if int(data.iloc[counter]["FemaleSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult65").send_keys(int(data.iloc[counter]["FemaleSen"]))
        
    if int(data.iloc[counter]["TransPre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderPreschool").send_keys(int(data.iloc[counter]["TransPre"])) 
    if int(data.iloc[counter]["TransChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderChild").send_keys(int(data.iloc[counter]["TransChi"]))
    if int(data.iloc[counter]["TransAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdolescent").send_keys(int(data.iloc[counter]["TransAdo"]))
    if int(data.iloc[counter]["TransAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult18").send_keys(int(data.iloc[counter]["TransAdu"]))
    if int(data.iloc[counter]["TransOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult40").send_keys(int(data.iloc[counter]["TransOldAdu"]))
    if int(data.iloc[counter]["TransSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult65").send_keys(int(data.iloc[counter]["TransSen"]))        
        '''         
def genAge(data, counter):
    #MaleAge
    print (data.iloc[counter]["GENDER / AGE"])
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 0 - 5 years':
        print ("Male Child")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMalePreschool").send_keys(int(1)) 
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 6 - 11 years':
        print ("Male Kid")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleChild").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 12 - 17 years': 
        print ("Male Kid")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdolescent").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 18 - 39 years': 
        print ("Male Adult")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult18").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 40 - 64 years': 
        print ("Male Older")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult40").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Male 65+ years': 
        print ("Male Senior")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult65").send_keys(int(1))
    #FemaleAge
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 0 - 5 years':
        print ("Female Child")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemalePreschool").send_keys(int(1)) 
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 6 - 11 years':
        print ("Female Kid")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleChild").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 12 - 17 years': 
        print ("Female Teen")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdolescent").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 18 - 39 years': 
        print ("Female Adult")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult18").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 40 - 64 years': 
        print ("Female Older Adult")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult40").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Female 65+ years':
        print ("Female Senior")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult65").send_keys(int(1))
    #TransAge
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 0 - 5 years':
        print ("Trans Child")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderPreschool").send_keys(int(1)) 
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 6 - 11 years':
        print ("Trans Kid")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderChild").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 12 - 17 years': 
        print ("Trans Teens")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdolescent").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 18 - 39 years':
        print ("Trans Adult")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult18").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 40 - 64 years': 
        print ("Trans Older Adult")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult40").send_keys(int(1))
    if str(data.iloc[counter]["GENDER / AGE"]) == 'Transgender 65+ years': 
        print ("Trans Senior")
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult65").send_keys(int(1))
        
def raceEthnicity(data, counter): 
    raceEthnicity = str(data.iloc[counter]["RACE / ETHNICITY"])
    raceEth = raceEthnicity.split(";")
    for x in raceEth:
        if str(x) == 'American Indian | Alaska Native':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_0").click()
        elif str(x) == 'Asian':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_1").click()
        elif str(x) == 'Black | African American':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_2").click()
        elif str(x) == 'Native Hawaiian | Other Pacific Islander':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_3").click()
        elif str(x) == 'White':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_4").click()
        elif str(x) == 'Hispanic | Latino':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_5").click()

def lang(data, counter):
    if str(data.iloc[counter]["LANGUAGE OF ENCOUNTER"]) == 'English':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_0").click()
    elif str(data.iloc[counter]["LANGUAGE OF ENCOUNTER"]) == 'Spanish':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_1").click()
    elif str(data.iloc[counter]["LANGUAGE OF ENCOUNTER"]) == 'Other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_2").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtPrimaryLanguageOther").send_keys(data.iloc[counter]["Other Language"])
        
def dis(data, counter):
    disabilityCode = str(data.iloc[counter]["ACCESS / FUNCTIONAL NEEDS"])
    disCode = disabilityCode.split(";")
    #print(disCode)
    for x in disCode:
        if x == 'Physical (mobility | visual | hearing | medical etc...)':
            print (x)
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_0").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_0").click()
        elif x  == 'Intellectual / Cognitive (learning disability | developmental delay etc...)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_1").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_1").click()
        elif x  == 'Mental Health | Substance Abuse (psychiatric | substance dependence etc...)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_2").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_2").click()

def loca(data, counter):
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_13").click()
def risks(data, counter):
    risk = str(data.iloc[counter]["RISK  CATEGORIES"])
    riskCode = risk.split(";")
    for x in riskCode:
        if x == 'Family missing | dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_0").click()
        elif x == 'Friend missing / dead':        
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_1").click()
        elif x == 'Pet missing / dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_2").click()
        elif x == 'Home damaged / destroyed':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_3").click()
        elif x == 'Vehicle / major property loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_4").click()
        elif x == 'Other financial loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_5").click()
        elif x == 'Disaster unemployed (self / household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_6").click()
        elif x == 'Injured / physically harmed (self / household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_7").click()
        elif x == 'Life was threatened (self / household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_8").click()
        elif x == 'Witnessed death / injury (self / household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_9").click()
        elif x == 'Assisted with rescue/recovery (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_10").click()
        elif x == 'Had to change schools':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_11").click()
        elif x == 'Prolonged separation from family':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_12").click()
        elif x == 'Evacuated quickly with no time to prepare':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_13").click()
        elif x == 'Displaced from home 1 week or more':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_14").click()
        elif x == 'Sheltered in place or sought shelter due to mmediate threat of danger':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_15").click()
        elif x == 'Past substance use / mental health problem':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_16").click()
        elif x == 'Preexisting physical disability':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_17").click()
        elif x == 'Past trauma':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_18").click()

def eventreac(data, counter):
    
    '''
    if (data.iloc[counter]["NumofEventReacs"]) == 1:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_0").click()
    elif (data.iloc[counter]["NumofEventReacs"]) == 2:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_1").click()
    elif (data.iloc[counter]["NumofEventReacs"]) == 3:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_2").click()
    elif (data.iloc[counter]["NumofEventReacs"]) == 4:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_3").click()
    elif (data.iloc[counter]["NumofEventReacs"]) == 5:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_4").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '6 or more':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_5").click()
     '''
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_0").click()
    Reacs = str(data.iloc[counter]["EVENT REACTIONS"])
    SplitReacs = Reacs.split(";")
    for x in SplitReacs:
        if x == 'Behavioral - Extreme change in activity level':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_0").click()
        elif x == 'Behavioral - Excessive drug or alcohol use':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_1").click()
        elif x == 'Behavioral - Isolation / withdrawal':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_2").click()
        elif x == 'Behavioral - On Guard / hypervigilant':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_3").click()
        elif x == 'Behavioral - Agitated / jittery / shaky':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_4").click()
        elif x == 'Behavioral - Violent / dangerous behavior':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_5").click() 
        elif x == 'Behavioral - Acts younger than age (children / youth)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_6").click()      
        elif x == 'Emotional - Sadness / tearful ':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_0").click()
        elif x == 'Emotional - Irritable / angry':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_1").click()
        elif x == 'Emotional - Anxious / fearful':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_2").click()
        elif x == 'Emotional - Despair / Hopeless':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_3").click()
        elif x == 'Emotional - Feelings of guilt / shame':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_4").click()
        elif x == 'Emotional - Numb / disconnected':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_5").click()         
        if x == 'Physical - Headaches':   
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_0").click()
        elif x == 'Physical - Stomach Problems':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_1").click()
        elif x == 'Physical - Difficulty falling / staying asleep ':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_2").click()
        elif x == 'Physical - Eating Problem':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_3").click()
        elif x == 'Worsening of health problems':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_4").click()
        elif x == 'Physical - Fatigue / exhaustion':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_5").click()
        elif x == 'Cognitive - Distressing dreams | nightmares':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_0").click()
        elif x == 'Cognitive - Intrusive thoughts | images':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_1").click()
        elif x == 'Cognitive - Difficulty concentrating':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_2").click()
        elif x == 'Cognitive - Difficulty Remembering things':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_3").click()
        elif x == 'Cognitive - Difficulty Making Decisions':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_4").click()
        elif x == 'Cognitive - Preoccupied with death/destruction':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_5").click()
        elif x == 'Coping Well - No Event Reactions (ONLY IF YOU SELECTED NOTHING ELSE)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cbCopingWell").click()
      
        
def focus(data, counter):
    
    focus = str(data.iloc[counter]["FOCUS OF ENCOUNTER"])
    foc = focus.split(";")
    for x in foc:
        if str(x) == 'Information / education about reactions to disaster':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_0").click()
        elif str(x) == 'Information / education about community resources':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_1").click()
        elif str(x) == 'Information / education about this crisis counseling program':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_2").click()
        elif str(x) == 'Tips for reducing negative thoughts':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_0").click()
        elif str(x) == 'Tips for managing physical /emotional reactions (ex: breathing techniques)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_1").click()
        elif str(x) == 'Tips for doing positive things':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_2").click()
        elif str(x) == 'Tips for problem solving':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_3").click()      
        elif str(x) == 'Compassionate presence / encouragement to connect with others / building social networks':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_0").click()
        elif str(x) == 'Encouragement to participate in community action':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_1").click()      
        elif str(x) == 'Other':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFocusOther").send_keys(x)
        
def material(data, counter):
    if str(data.iloc[counter]["WERE ARTICLES / WEBSITES / FLYERS / PHONE NUMBERS SHARED WITH HELP-SEEKER?"]) == "Yes":
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_1").click()

def referral(data, counter):
    referralsGiven = str(data.iloc[counter]["REFERRAL"])
    refGiv = referralsGiven.split(";")
    if len(refGiv) == 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cbNoReferral").click()
    else:
        for x in refGiv:
            if str(x) == 'Crisis counseling program services (ex: group counseling | referral to team lead | follow-up visit)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_0").click()
            elif str(x) == 'Mental health services (ex: professional longer-term counseling | treatment | behavioral | or psychiatric services)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_1").click()
            elif str(x) == 'Substance abuse services (ex: professional | behavioral | or medical treatment or self-help groups such as Alcoholics Anonymous / Narcotics Anonymous)':
               SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_2").click()
            elif str(x) == 'Community services (ex: FEMA | loans | housing | employment | social services)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_3").click()
            elif str(x) == 'Resources for those with disabilities / other access / functional needs':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_4").click()
            elif str(x) == "No Referral Given": 
                print ("No Referral Given")
            else:
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_5").click()
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtReferralOther").send_keys(str(x))
    
           
def start(y, df):
    counter = y
    data = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink29").click()   
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(int(data.iloc[y]["ODCES ID (1ST EMPLOYEE)"]))
    if int(data.iloc[y]["ODCES ID (2nd EMPLOYEE)"]) != 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber2").send_keys(int(data.iloc[y]["ODCES ID (2nd EMPLOYEE)"]))
    ZipCode = int(data.iloc[y]["ZIP CODE OF SERVICE"])
    ZipCodeStr = str(ZipCode)
    print(ZipCodeStr)
    if len(ZipCodeStr) < 5 : 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(92629)
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(int(data.iloc[y]["ZIP CODE OF SERVICE"]))
    t = str(data.iloc[y]["DATE OF ENCOUNTER"])
    #date = datetime.date(t, '%m/%d/%Y')
    #print(date.strftime('%m/%d/%Y'))
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").click()
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").send_keys(t)
    #ProgramSetting.programSet(data, counter)
    select = SeleniumAbid.Select(SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_ddlDisaster"))
    select.select_by_value('418')
    visitType(counter, data)
    visitNumber(data, counter)
    visitDuration(data, counter)
    genAge(data, counter)
    #MaleAge(data, counter)
    #FemaleAge(data, counter)
    #TransAge(data, counter)
    raceEthnicity(data, counter)
    lang(data, counter)
    dis(data, counter)
    loca(data, counter)
    risks(data, counter)
    eventreac(data, counter)
    focus(data, counter)
    material(data, counter)
    referral(data, counter)
    visitType(counter, data)
    zipCodeDirectory.Zip(data, counter)
    #time.sleep(20)
    #time.sleep(30)
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
    print("Log has been submitted")
    #time.sleep(20)
    