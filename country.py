import argparse
import requests


def list_to_string_comma_seperated(value):
    return ','.join(value)


parser = argparse.ArgumentParser(description='Get country information')

parser.add_argument(
    '--name', help='Common name of the country. Ex: United States', required=True)

args = parser.parse_args()

# The next line is a better API endpoint for this use case but is not in requirements stated.
# response = requests.get( 'https://restcountries.com/v3.1/name/{country}?fullText=true'.format( country = args.name ) )

if not args.name:
    print('Please provide a country name.')
    exit()

response = requests.get('https://restcountries.com/v3.1/all')
countries = response.json()

selected_country = None
for country in countries:
    if country['name']['common'].lower() == args.name:
        selected_country = country
        break

if (selected_country == None):
    print('No country named {country} found. Please try again with a different name.'.format(
        country=args.name))
    exit()

output = {
    'official_name': selected_country['name']['official'],
    'currencies': [selected_country['currencies'][currency_name]['name'] for currency_name in selected_country['currencies'].keys()],
    'capital': selected_country['capital'],
    'borders': selected_country['borders'],
    'car_signs': selected_country['car']['signs'],
    'timezones': selected_country['timezones'],
    'latlng': [str(latlng) for latlng in selected_country['latlng']]
}

print('Official Name: ' + output['official_name'])
print('Currencies: ' + list_to_string_comma_seperated(output['currencies']))
print('Capital: ' + list_to_string_comma_seperated(output['capital']))
print('Borders: ' + list_to_string_comma_seperated(output['borders']))
print('Car Signs: ' + list_to_string_comma_seperated(output['car_signs']))
print('Timezones: ' + list_to_string_comma_seperated(output['timezones']))
print('Latitude, Longitude: ' +
      list_to_string_comma_seperated(output['latlng']))
