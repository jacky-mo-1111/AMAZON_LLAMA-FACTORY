# Write your function here
def average_temperature(cities):
    total_temperature = 0
    for city in cities:
        total_temperature += city['temperature']
    return total_temperature / len(cities)

# Write your function here
def load_city_temperature_data(filename):
    with open(filename) as file:
        contents = file.read()
        lines = contents.split('\n')
        data = [line.split(',') for line in lines]
        return [{line[0]: line[1]} for line in data]

# Write your function here
import logging

def load_city_temperature_data(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            lines = contents.split('\n')
            data = [line.split(',') for line in lines]
            return [{line[0]: line[1]} for line in data]
    except FileNotFoundError:
        logging.error("File not found: %s", filename)
    except OSError:
        logging.error("Error reading file: %s", filename)
    return []

# Write your function here
def find_max_temperature(cities):
    max_temperature = -100000
    max_city = None
    for city in cities:
        if city['temperature'] > max_temperature:
            max_temperature = city['temperature']
            max_city = city
    return max_city

# Write your function here
def average_temperature_min_temperature(cities):
    min_temperature = min([city['temperature'] for city in cities])
    filtered_cities = list(filter(lambda city: city['temperature'] == min_temperature, cities))
    total_temperature = sum([city['temperature'] for city in filtered_cities])
    return total_temperature / len(filtered_cities)

# Write your function here
def top_n_cities(cities, n):
    sorted_cities = sorted(cities, key=lambda city: city['average_temperature'], reverse=True)
    top_n_cities = []
    for city in sorted_cities:
        if len(top_n_cities) < n:
            top_n_cities.append(city)
    return top_n_cities

# Write your function here
import logging

def top_n_cities(cities, n):
    try:
        n = int(n)
    except ValueError:
        logging.error("User input is not an integer: %s", n)
        return []
    sorted_cities = sorted(cities, key=lambda city: city['average_temperature'], reverse=True)
    top_n_cities = []
    for city in sorted_cities:
        if len(top_n_cities) < n:
            top_n_cities.append(city)
    return top_n_cities