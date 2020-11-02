# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
    damages_updated = []
    for cost in damages:
        if cost == 'Damages not recorded':
            damages_updated.append(cost)
        elif 'M' in cost:
            cost = cost.strip('M')
            cost = float(cost)
            cost *= 1000000
            damages_updated.append(cost)
        elif 'B' in cost:
            cost = cost.strip('B')
            cost = float(cost)
            cost *= 1000000000
            damages_updated.append(cost)
    return damages_updated
    
damages_updated = update_damages(damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary():
    hurricane_dictionary = {}
    for i in range(len(names)):
        hurricane_dictionary[names[i]] = {"Name": names[i], "Month": months[i], "Year":years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages_updated[i], "Deaths": deaths[i]}
    return hurricane_dictionary
    
hurricane_dictionary = construct_hurricane_dictionary()

# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year_dictionary(hurricane_dictionary):
    hurricane_by_year_dictionary = {}
    for value in hurricane_dictionary.values():
        if value["Year"] in hurricane_by_year_dictionary:
            hurricane_by_year_dictionary[value["Year"]].append(value)
        else:
            hurricane_by_year_dictionary[value["Year"]] = [value]
    return hurricane_by_year_dictionary
    
hurricane_by_year_dictionary = construct_hurricane_by_year_dictionary(hurricane_dictionary)

# write your count affected areas function here:
def count_affected_areas(hurricane_dictionary):
    affected_areas_count = {}
    for value in hurricane_dictionary.values():
        for area in value["Areas Affected"]:
            if area in affected_areas_count:
                affected_areas_count[area] += 1
            else:
                affected_areas_count[area] = 1
    return affected_areas_count
    
affected_areas_count = count_affected_areas(hurricane_dictionary)

# write your find most affected area function here:
def most_affected_area(affected_areas_count):
    area = ''
    highest_value = 0
    for key, value in affected_areas_count.items():
        if value > highest_value:
            area = key
            highest_value = value
    return area, highest_value

most_affected_area = most_affected_area(affected_areas_count)

# write your greatest number of deaths function here:
def greatest_number_of_deaths(hurricane_dictionary):
    hurricane = ''
    deaths = 0
    for value in hurricane_dictionary.values():
        if value["Deaths"] > deaths:
            hurricane = value["Name"]
            deaths = value["Deaths"]
    return hurricane, deaths

greatest_number_of_deaths = greatest_number_of_deaths(hurricane_dictionary)

# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricane_dictionary):
    categorized_by_mortality = {1: [], 2: [], 3: [], 4: [], 5: []}
    for value in hurricane_dictionary.values():
        if value["Deaths"] > 0 and value["Deaths"] <= 100:
            categorized_by_mortality[1].append(value)
        if value["Deaths"] > 100 and value["Deaths"] <= 500:
            categorized_by_mortality[2].append(value)
        if value["Deaths"] > 500 and value["Deaths"] <= 1000:
            categorized_by_mortality[3].append(value)
        if value["Deaths"] > 1000 and value["Deaths"] <= 10000:
            categorized_by_mortality[4].append(value)
        if value["Deaths"] > 10000:
            categorized_by_mortality[5].append(value)
    return categorized_by_mortality
    
categorized_by_mortality = categorize_by_mortality(hurricane_dictionary)

# write your greatest damage function here:
def greatest_damage(hurricane_dictionary):
    hurricane = ''
    damage = 0
    for value in hurricane_dictionary.values():
        if type(value["Damage"]) == str:
            continue
        elif value["Damage"] > damage:
            hurricane = value["Name"]
            damage = value["Damage"]
    return hurricane, damage

greatest_damage = greatest_damage(hurricane_dictionary)

# write your catgeorize by damage function here:
def categorize_by_damage(hurricane_dictionary):
    categorized_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for value in hurricane_dictionary.values():
        if type(value["Damage"]) == str:
            categorized_by_damage[0].append(value)
        elif value["Damage"] > 0 and value["Damage"] <= 100000000:
            categorized_by_damage[1].append(value)
        elif value["Damage"] > 100000000 and value["Damage"] <= 1000000000:
            categorized_by_damage[2].append(value)
        elif value["Damage"] > 1000000000 and value["Damage"] <= 10000000000:
            categorized_by_damage[3].append(value)
        elif value["Damage"] > 10000000000 and value["Damage"] <= 50000000000:
            categorized_by_damage[4].append(value)
        elif value["Damage"] > 50000000000:
            categorized_by_damage[5].append(value)
    return categorized_by_damage
    
categorized_by_damage = categorize_by_damage(hurricane_dictionary)
