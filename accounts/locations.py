from Countrydetails import countries

def CountryData():
    data=[{
        "name":key,
        "phone_code":value,
    } for key,value in countries.all_countries().phone_code().items() ]
    
    return data

CountryData()
