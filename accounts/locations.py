from Countrydetails import countries

def CountryData():
    data=[{
        "name":country['name'],
        "phone_code":country['phone_code'],
        "country_code":country['iso2'],
        "states":[state['name'] for state in country['states']],
        'flag':f'https://flagcdn.com/16x12/{country["iso2"].lower()}.png'
    } for country in countries.all_countries().states_file if len(country['states'])!=0
      ]
    
    return data

# print(countries.all_countries().states_file[0:2])
