countries = [ {'name': 'Israel', 'population': 9.3, 'birth': 1948},
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan',
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901},
{'name': 'Canada', 'population': 38.0, 'birth': 1867} ]

# Filter countries with population greater than 30 million
large_population_countries = list(filter(lambda country: country['population'] > 30, countries))

print(large_population_countries)

# Filter countries established after 1800
countries_established_after_1800 = list(filter(lambda country: country['birth'] > 1800, countries))

print(countries_established_after_1800)

# Create a list of only the names of the countries
country_names = list(map(lambda country: country['name'], countries))

print(country_names)

# Create a list of only the years of establishment of the countries
country_birth_years = list(map(lambda country: country['birth'], countries))

print(country_birth_years)

# Sort the list of countries by their year of establishment
countries.sort(key=lambda country: country['birth'])

print(countries)

# Sort the list of countries by their population
countries.sort(key=lambda country: country['population'])

print(countries)
