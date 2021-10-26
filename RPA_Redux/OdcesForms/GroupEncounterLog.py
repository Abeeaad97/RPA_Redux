from OdcesForms import SeleniumAbid
from OdcesForms import zipCodeDirectory
from OdcesForms import ProgramSetting
import datetime
def groupType(daFra, counter):
    if str(daFra.iloc[counter]["GroupSessionType"]) == 'GROUP COUNSELING':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlServiceTypeCode_0").click()
    else:
        SeleniumAbid .driver.find_element_by_id("ContentPlaceHolder1_rdlServiceTypeCode_1")
def groupLoca(daFra, counter): 
    if str(daFra.iloc[counter]["Location"]) == 'school and child care (all ages through college)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_0").click()
    elif str(daFra.iloc[counter]["Location"]) == 'community center (e.g.  recreation club)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_1").click()
    elif str(daFra.iloc[counter]["Location"]) == 'provider site/mental health agency (agency involved with Crisis Counseling Assistance and Training Program [CCP])':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_2").click()
    elif str(daFra.iloc[counter]["Location"]) == 'workplace (workplace of the disaster survivor and/or first responder)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_3").click()
    elif str(daFra.iloc[counter]["Location"]) == 'disaster recovery center (e.g.  Federal Emergency Management Agency [FEMA]  American Red Cross)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_4").click()
    elif str(daFra.iloc[counter]["Location"]) == 'place of worship (e.g.  church  synagogue  mosque)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_5").click()
    elif str(daFra.iloc[counter]["Location"]) == 'home (temporary or permanent residence  including friend/family home; group homes  including houses  apartments  trailers  and other dwellings)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_6").click()
    elif str(daFra.iloc[counter]["Location"]) == 'retail (e.g.  restaurant  mall  shopping center  store)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_7").click()
    elif str(daFra.iloc[counter]["Location"]) == 'medical center (e.g.  doctor  dentist  hospital  mental health   or substance abuse specialty center)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_8").click()
    elif str(daFra.iloc[counter]["Location"]) == 'public place/event (e.g.  street sidewalk  town square  fair  festival  sports)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_9").click()
    elif str(daFra.iloc[counter]["Location"]) == 'Other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_10").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtGroupServiceLocationOther").send_keys(str(daFra.iloc[counter]["Other Location"]))
def groupSessNum(daFra, counter):
    if str(daFra.iloc[counter]["Visit Number"]) == 'First session of group expected to meet once':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_0").click()
    elif str(daFra.iloc[counter]["Visit Number"]) == 'First session of group expected to meet more than once':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_1").click()
    elif str(daFra.iloc[counter]["Visit Number"]) == 'Second or greater session of ongoing group':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_2").click()
def groupNumofPeople(daFra, counter):
    if int(daFra.iloc[counter]["GroupMinors"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant18").send_keys(int(daFra.iloc[counter]["GroupMinors"]))
    if int(daFra.iloc[counter]["GroupAdults"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant64").send_keys(int(daFra.iloc[counter]["GroupAdults"]))
    if int(daFra.iloc[counter]["GroupSeniors"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant65").send_keys(int(daFra.iloc[counter]["GroupSeniors"]))
def groupCompo(daFra, counter):
    if str(daFra.iloc[counter]["GroupIdentities"]) == 'Children or youth (Under age 18) CHECK  if yes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_0").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_0").click()
    if str(daFra.iloc[counter]["GroupIdentities"]) == 'Adult survivors (adults who were directly affected by the disaster)? CHECK  if yes.':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_1").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_1").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Public safety workers and first responders (e.g.  police  fire  emergency medical services  rescue)? CHECK  if yes.':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_2").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_2").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Other recovery workers (e.g.  health care  disaster relief  social services)? CHECK  if yes.':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_3").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_3").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Was the group composed of a mixtures of the above or none of the above (i.e.  no clear group identity)? CHECK  if yes.':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_4").click()
        #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_4").click()
def groupRaceEth(daFra, counter):
    raceEthnicity = daFra.iloc[counter]["Race/Ethnicity"]
    raceEth = str(raceEthnicity).split(";")
    for x in raceEth:
        if str(x) == 'American Indian/Alaska Native':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_0").click()
        elif str(x) == 'Native Hawaiian/Other Pacific Islander':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_3").click()
        elif str(x) == 'Asian':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_1").click()
        elif str(x) == 'White':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_4").click()
        elif str(x) == 'Black or African American':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_2").click()
        elif str(x) == 'Hispanic or Latino':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_5").click()
def groupDis(daFra, counter):
    disabilityCode = daFra.iloc[counter]["Disability"]
    disCode = str(disabilityCode).split(";")
    for x in disCode:
        if str(x) == "Physical (mobility  visual  hearing  medical  etc.)":
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_0").click()
        elif str(x) == "Intellectual/Cognitive (learning disability  developmental delay  etc.)":
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_1").click()
        elif str(x) == "Mental Health/Substance Abuse(psychiatric  substance  dependence  etc.)":
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_2").click()
def groupFocus(daFra, counter):
    groupInfo = daFra.iloc[counter]["Information Given"]
    groInf = str(groupInfo).split(";")
    for x in groInf:
        if str(x) == 'reactions to disaster':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_0").click()
        elif str(x) == 'community resources':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_1").click()
        elif str(x) == 'this crisis counseling program':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_2").click()
            
    groupTips = daFra.iloc[counter]["Tips"]
    groTi = str(groupTips).split(";")
    for x in groTi: 
        if str(x) == 'reducing negative thoughts':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_0").click()
        elif str(x) == 'managing physical and emotional reactions (e.g.  breathing techniques)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_1").click()
        elif str(x) == 'doing positive things': 
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_2").click()
        elif str(x) == 'problem solving':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_3").click()
            
    groupHealth = daFra.iloc[counter]["Healthy Connections"]
    groHea = str(groupHealth).split(";")
    for x in groHea: 
        if str(x) == 'mutual support/building social networks(s)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_0").click()
        elif str(x) == 'participating in community action':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_1").click()
def groupDura(daFra, counter):
    if int(daFra.iloc[counter]["Visit Duration"]) >= 15 and int(daFra.iloc[counter]["Visit Duration"]) <= 29:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_0").click()
    elif int(daFra.iloc[counter]["Visit Duration"]) >= 30 and int(daFra.iloc[counter]["Visit Duration"]) <= 44:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_1").click()
    elif int(daFra.iloc[counter]["Visit Duration"]) >= 45 and int(daFra.iloc[counter]["Visit Duration"]) <= 59:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_2").click()
    elif int(daFra.iloc[counter]["Visit Duration"]) >= 60:   
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_3").click()
def groupMats(daFra, counter):
    if str(daFra.iloc[counter]["Materials"]) == "Yes":
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_1").click()
def start(y, df):
    counter = y
    daFra = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink30").click()
    ProgramSetting.programSet(daFra, counter)
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(int(daFra.iloc[counter]["WorkerNum"]))
    ZipCode = int(daFra.iloc[y]["ZipCode"])
    ZipCodeStr = str(ZipCode)
    print(ZipCodeStr)
    if len(ZipCodeStr) < 5 : 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(92629)
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtZipCode").send_keys(int(daFra.iloc[y]["ZipCode"]))
    t = str(daFra.iloc[y]["Date"])
    date = datetime.datetime.strptime(t, '%m/%d/%Y %H:%M')
    print(date.strftime('%m/%d/%Y'))
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").click()
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceDate").send_keys((date.strftime('%m/%d/%Y')))
    groupCompo(daFra, counter)
    groupRaceEth(daFra, counter)
    groupDis(daFra, counter)
    groupFocus(daFra, counter)
    groupMats(daFra, counter)
    groupType(daFra, counter)
    groupLoca(daFra, counter)
    groupSessNum(daFra, counter)
    groupNumofPeople(daFra, counter)
    groupDura(daFra, counter)
    zipCodeDirectory.Zip(daFra, counter)
    
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
    #print("Log has been submitted")