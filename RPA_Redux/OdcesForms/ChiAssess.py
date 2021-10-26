from OdcesForms import SeleniumAbid 
from OdcesForms import IndiLog 
from OdcesForms import AduAssess
from OdcesForms import zipCodeDirectory
from OdcesForms import ProgramSetting
import testData
import datetime

def ChiAgeGen(dataF, counter):
    if dataF.iloc[counter]["Child Age"] == 'preschool (0-5 years))':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_0").click()
    elif dataF.iloc[counter]["Child Age"] == 'child (6-11 years)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_1").click()
    elif dataF.iloc[counter]["Child Age"] == 'adolescent (12-17 years)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_2").click()
    elif dataF.iloc[counter]["Child Age"] == 'preschool (0-5 years));child (6-11 years);adolescent (12-17 years)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_0").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_1").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlChildAgeCode_2").click()
    
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtGradeLevel").send_keys(str(dataF.iloc[counter]["Grade Level"]))
    
    if dataF.iloc[counter]["Child Gender"] == 'Male':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_0").click()
    elif dataF.iloc[counter]["Child Gender"] == 'Female': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_1").click()
    elif dataF.iloc[counter]["Child Gender"] == 'Transgender':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_2").click()
    elif dataF.iloc[counter]["Child Gender"] == 'None of these':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_3").click()
    elif dataF.iloc[counter]["Child Gender"] == 'Male;Female;Transgender;None of these':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_0").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_1").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_2").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_3").click()
        
def ChiAssessQuest(dataF, counter):
    chiAssessQ = {
        1:dataF.iloc[counter]["Chi Assessment 1"],
        2:dataF.iloc[counter]["Chi Assessment 2"],
        3:dataF.iloc[counter]["Chi Assessment 3"],
        4:dataF.iloc[counter]["Chi Assessment 4"],
        5:dataF.iloc[counter]["Chi Assessment 5"],
        6:dataF.iloc[counter]["Chi Assessment 6"],
        7:dataF.iloc[counter]["Chi Assessment 7"],
        8:dataF.iloc[counter]["Chi Assessment 8"],
        9:dataF.iloc[counter]["Chi Assessment 9"],
        10:dataF.iloc[counter]["Chi Assessment 10"],
        11:dataF.iloc[counter]["Chi Assessment 11"],
        12:dataF.iloc[counter]["Chi Assessment 12"],
        13:dataF.iloc[counter]["Chi Assessment 13"],
        14:dataF.iloc[counter]["Chi Assessment 14"],
        15:dataF.iloc[counter]["Chi Assessment 15"],
        16:dataF.iloc[counter]["Chi Assessment 16"],
        17:dataF.iloc[counter]["Chi Assessment 17"],
        18:dataF.iloc[counter]["Chi Assessment 18"],
        19:dataF.iloc[counter]["Chi Assessment 19"],
        20:dataF.iloc[counter]["Chi Assessment 20"],
        21:dataF.iloc[counter]["Chi Assessment 21"],
        22:dataF.iloc[counter]["Chi Assessment 22"],
        23:dataF.iloc[counter]["Chi Assessment 23"],
        24:dataF.iloc[counter]["Chi Assessment 24"],
        25:dataF.iloc[counter]["Chi Suicide Assessment"]
        }
    
    for key in chiAssessQ:
        if key == 1:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_4").click()
            elif chiAssessQ[key] == 'N/A':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_5").click()
        elif key == 2:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_5").click()
        elif key == 3:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_5").click()
        elif key == 4:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_5").click()
        elif key == 5:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_5").click()
        elif key == 6:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_5").click()
        elif key == 7:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_5").click()
        elif key == 8:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_5").click()
        elif key == 9:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_5").click()
        elif key == 10:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_5").click()
        elif key == 11:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_5").click()
        elif key == 12:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_5").click()
        elif key == 13:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_5").click()
        elif key == 14:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_5").click()
        elif key == 15:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ15Code_5").click()
        elif key == 16:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ16Code_5").click()
        elif key == 17:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ17Code_5").click()
        elif key == 18:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ18Code_5").click()
        elif key == 19:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ19Code_5").click()
        elif key == 20:
            if chiAssessQ[key] == '0-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_0").click()
            elif chiAssessQ[key] == '1-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_1").click()
            elif chiAssessQ[key] == '2-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_2").click()
            elif chiAssessQ[key] == '3-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_3").click()
            elif chiAssessQ[key] == '4-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_4").click()
            elif chiAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ20Code_5").click()
        elif key == 21:
            if chiAssessQ[key] == 'NO':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ21Code_1").click()
            elif chiAssessQ[key] == 'YES':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ21Code_0").click()
        elif key == 22:
            if chiAssessQ[key] == 'NO':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ22Code_1").click()
            elif chiAssessQ[key] == 'YES':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ22Code_0").click()
        elif key == 23:
            if chiAssessQ[key] == 'NO':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ23Code_1").click()
            elif chiAssessQ[key] == 'YES':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ23Code_0").click()
        elif key == 24: 
            if chiAssessQ[key] == 'NO':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ24Code_1").click()
            elif chiAssessQ[key] == 'YES':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ24Code_0").click()
        elif key == 25:
            if chiAssessQ[key] == 'YES':
                print (chiAssessQ[key])
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlKillYourselfCode_0").click()
                #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlKillYourselfCode_0")
            elif chiAssessQ[key] == 'NO':
                print (chiAssessQ[key])
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlKillYourselfCode_1").click()
                #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlKillYourselfCode_1")
                
        
def ChiLoca(dataF, counter):
    print(dataF.iloc[counter]["Visit Number"])
    if str(dataF.iloc[counter]["Visit Number"]) == 'First Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
    elif str(dataF.iloc[counter]["Visit Number"]) == 'Second Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_1").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_1").click()
    elif str(dataF.iloc[counter]["Visit Number"]) == 'Third Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_2").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_2").click()
    elif str(dataF.iloc[counter]["Visit Number"]) == 'Fourth Visit': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_3").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_3").click()
    elif str(dataF.iloc[counter]["Visit Number"]) == 'Fifth Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_4").click() 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_4").click()         
    




def start (y, df): 
    counter = y
    dataF = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink33").click()
    ProgramSetting.programSet(dataF, counter)
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(int(dataF.iloc[y]["WorkerNum"]))
    #IndiLog.visitNumber(dataF, counter)
    ZipCode = int(dataF.iloc[y]["ZipCode"])
    ZipCodeStr = str(ZipCode)
    print(ZipCodeStr)
    if len(ZipCodeStr) < 5 : 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(92629)
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(int(dataF.iloc[y]["ZipCode"]))
    t = str(dataF.iloc[y]["Date"])
    date = datetime.datetime.strptime(t, '%m/%d/%Y %H:%M')
    print(date.strftime('%m/%d/%Y'))
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").click()
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").send_keys((date.strftime('%m/%d/%Y')))
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
    IndiLog.visitDuration(dataF, counter)
    if dataF.iloc[counter]["Parent/Caregiver Present"] == 'YES':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlParentPresentCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlParentPresentCode_1").click()
    if dataF.iloc[counter]["Lead Pres"] == 'YES':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlLeadPresentCode_0").click()
    else: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlLeadPresentCode_1").click()
    IndiLog.loca(dataF, counter)
    AduAssess.AduRiskCode(dataF, counter)
    ChiAgeGen(dataF, counter)
    IndiLog.dis(dataF, counter)
    IndiLog.lang(dataF, counter)
    IndiLog.raceEthnicity(dataF, counter)
    ChiAssessQuest(dataF, counter)
    IndiLog.referral(dataF, counter)
    if dataF.iloc[counter]["Child Referral Acceptance"] == 'YES':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptByChildCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptByChildCode_1").click()
        
    if dataF.iloc[counter]["Parent Referral Acceptance"] == 'YES':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptByParentCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptByParentCode_1").click()
    zipCodeDirectory.Zip(dataF, counter)
    
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
    
