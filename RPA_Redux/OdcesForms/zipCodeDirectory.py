from OdcesForms import SeleniumAbid

def Zip(data, counter):
    select = SeleniumAbid.Select(SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_ddlCounty"))
    x = str(data.iloc[counter]["COUNTY OF SERVICE"])
    print(x)
    if x == 'Alameda': 
        select.select_by_value('187')
    elif x == 'Alpine':
        select.select_by_value('188')
    elif x == 'Amador':
        select.select_by_value('189')
    elif x == 'Butte':
        select.select_by_value('190')
    elif x == 'Calaveras':
        select.select_by_value('191')
    elif x == 'Colusa':
        select.select_by_value('192')
    elif x == 'Contra Costa':
        select.select_by_value('193')
    elif x == 'Del Norte':
        select.select_by_value('194')
    elif x == 'El Dorado':
        select.select_by_value('195')
    elif x == 'Fresno':
        select.select_by_value('196')
    elif x == 'Glenn':
        select.select_by_value('197')
    elif x == 'Humboldt':
        select.select_by_value('198')
    elif x == 'Imperial':
        select.select_by_value('199')
    elif x == 'Inyo':
        select.select_by_value('200')
    elif x == 'Kern':
        select.select_by_value('201')
    elif x == 'Kings':
        select.select_by_value('202')
    elif x == 'Lake':
        select.select_by_value('203')
    elif x == 'Lassen':
        select.select_by_value('204')
    elif x == 'Los Angeles':
        select.select_by_value('205')
    elif x == 'Madera':
        select.select_by_value('206')
    elif x == 'Marin':
        select.select_by_value('207')
    elif x == 'Mariposa':
        select.select_by_value('208')
    elif x == 'Mendocino':
        select.select_by_value('209')
    elif x == 'Merced':
        select.select_by_value('210')
    elif x == 'Modoc':
        select.select_by_value('211')
    elif x == 'Mono':
        select.select_by_value('212')
    elif x == 'Monterey':
        select.select_by_value('213')
    elif x == 'Napa':
        select.select_by_value('214')
    elif x == 'Nevada':
        select.select_by_value('215')
    elif x == 'Orange':
        select.select_by_value('216')
    elif x == 'Placer':
        select.select_by_value('217')
    elif x == 'Plumas':
        select.select_by_value('218')
    elif x == 'Riverside':
        select.select_by_value('219')
    elif x == 'Sacramento':
        select.select_by_value('220')
    elif x == 'San Benito ':
        select.select_by_value('221')
    elif x == 'San Bernardino':
        select.select_by_value('222')
    elif x == 'San Diego':
        select.select_by_value('223')
    elif x == 'San Francisco': 
        select.select_by_value('224')
    elif x == 'San Joaquin':
        select.select_by_value('225')
    elif x == 'San Luis Obispo':
        select.select_by_value('226')
    elif x == 'San Mateo':
        select.select_by_value('227')
    elif x == 'Santa Barbara':
        select.select_by_value('228')
    elif x == 'Santa Clara':
        select.select_by_value('229')
    elif x == 'Santa Cruz':
        select.select_by_value('230')
    elif x == 'Shasta':
        select.select_by_value('231')
    elif x == 'Sierra':
        select.select_by_value('232')
    elif x == 'Siskiyou':
        select.select_by_value('233')
    elif x == 'Solano':
        select.select_by_value('234')
    elif x == 'Sonoma':
        select.select_by_value('235')
    elif x == 'Stanislaus':
        select.select_by_value('236')
    elif x == 'Sutter':
        select.select_by_value('237')
    elif x == 'Tehama':
        select.select_by_value('238')
    elif x == 'Trinity County':
        select.select_by_value('239')
    elif x == 'Tulare County':
        select.select_by_value('240')
    elif x == 'Tuolumne':
        select.select_by_value('241')
    elif x == 'Ventura':
        select.select_by_value('242')
    elif x == 'Yolo':
        select.select_by_value('243')
    elif x == 'Yuba':
        select.select_by_value('244')
    else: #Most Likely out of state, change the county to 
        select.select_by_value('216')