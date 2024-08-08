israel_info = {
    'name': 'Israel',
    'born': 1948,
    'population_millions': 9.3,
    'capital': 'Jerusalem',
    'language': 'Hebrew',
    'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
    'currency': 'ILS',
    'area_kilometer': "22,145",
    'gdp_billion': 450}

print(israel_info)

capital_city = israel_info.get('capital')
print(capital_city)

keys = israel_info.keys()
print(keys)

capital_letters_key = [key.upper() for key in israel_info.keys()]
print(capital_letters_key)

values = israel_info.values()
print(values)

lengths = [len(str(value)) for value in israel_info.values()]
print(lengths)

for key, value in israel_info.items():
    print(f'{key}: {value}')


israel_info_copy = israel_info.copy()

print(israel_info_copy)


# Clear the new dictionary
israel_info_copy.clear()

print(israel_info_copy)


# Create a new dictionary with the same keys but all values set to None
keys = israel_info.keys()
new_dict_with_none = dict.fromkeys(keys, None)

print(new_dict_with_none)


# Delete the 'currency' key and its value
del israel_info['currency']

print(israel_info)


# Remove the 'area_kilometer' key and its value in one line
israel_info.pop('area_kilometer')

print(israel_info)

# Update the dictionary in one operation
israel_info.update({
    'Soccer': 'sport_national',
    'population_millions': 9.4
})

print(israel_info)


israel_info["population_millions"] = 9.4

print(israel_info)