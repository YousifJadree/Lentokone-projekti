import csv
import random


class Airport:
    def init(self, name, country_code):
        self.name = name
        self.country_code = country_code

class Game:
    def init(self):
        self.airports = []
        self.countries = {}
        self.remaining_countries = set()
        self.correct_answers = 0
        self.total_questions = 0
        self.load_country_data()
        self.load_airports_from_csv()

  def load_country_data(self):
        self.countries = {
            'GB': {'name': 'United Kingdom', 'population': '67 million', 'flag_colors': 'Red, White, Blue', 'capital': 'London'},
            'FR': {'name': 'France', 'population': '67 million', 'flag_colors': 'Blue, White, Red', 'capital': 'Paris'},
            'DE': {'name': 'Germany', 'population': '83 million', 'flag_colors': 'Black, Red, Yellow', 'capital': 'Berlin'},
            'IT': {'name': 'Italy', 'population': '60 million', 'flag_colors': 'Green, White, Red', 'capital': 'Rome'},
            'ES': {'name': 'Spain', 'population': '47 million', 'flag_colors': 'Red, Yellow', 'capital': 'Madrid'},
            'NL': {'name': 'Netherlands', 'population': '17 million', 'flag_colors': 'Red, White, Blue', 'capital': 'Amsterdam'},
            'SE': {'name': 'Sweden', 'population': '10 million', 'flag_colors': 'Blue, Yellow', 'capital': 'Stockholm'},
            'NO': {'name': 'Norway', 'population': '5.5 million', 'flag_colors': 'Red, White, Blue', 'capital': 'Oslo'},
            'FI': {'name': 'Finland', 'population': '5.5 million', 'flag_colors': 'White, Blue', 'capital': 'Helsinki'},
            'DK': {'name': 'Denmark', 'population': '6 million', 'flag_colors': 'Red, White', 'capital': 'Copenhagen'},
            'BE': {'name': 'Belgium', 'population': '11.5 million', 'flag_colors': 'Black, Yellow, Red', 'capital': 'Brussels'},
            'CH': {'name': 'Switzerland', 'population': '8.7 million', 'flag_colors': 'Red, White', 'capital': 'Bern'},
            'AT': {'name': 'Austria', 'population': '9 million', 'flag_colors': 'Red, White', 'capital': 'Vienna'},
            'PL': {'name': 'Poland', 'population': '38 million', 'flag_colors': 'White, Red', 'capital': 'Warsaw'},
            'GR': {'name': 'Greece', 'population': '10.5 million', 'flag_colors': 'Blue, White', 'capital': 'Athens'},
            'PT': {'name': 'Portugal', 'population': '10 million', 'flag_colors': 'Green, Red', 'capital': 'Lisbon'},
            'IE': {'name': 'Ireland', 'population': '5 million', 'flag_colors': 'Green, White, Orange', 'capital': 'Dublin'},
            'CZ': {'name': 'Czech Republic', 'population': '10.5 million', 'flag_colors': 'White, Red, Blue', 'capital': 'Prague'},
            'HU': {'name': 'Hungary', 'population': '10 million', 'flag_colors': 'Red, White, Green', 'capital': 'Budapest'},
            'RO': {'name': 'Romania', 'population': '19 million', 'flag_colors': 'Blue, Yellow, Red', 'capital': 'Bucharest'},
            'BG': {'name': 'Bulgaria', 'population': '7 million', 'flag_colors': 'White, Green, Red', 'capital': 'Sofia'},
            'HR': {'name': 'Croatia', 'population': '4 million', 'flag_colors': 'Red, White, Blue', 'capital': 'Zagreb'},
            'IS': {'name': 'Iceland', 'population': '370,000', 'flag_colors': 'Blue, White, Red', 'capital': 'Reykjavik'},
            'SK': {'name': 'Slovakia', 'population': '5.5 million', 'flag_colors': 'White, Blue, Red', 'capital': 'Bratislava'},
            'SI': {'name': 'Slovenia', 'population': '2 million', 'flag_colors': 'White, Blue, Red', 'capital': 'Ljubljana'},
            'LT': {'name': 'Lithuania', 'population': '2.8 million', 'flag_colors': 'Yellow, Green, Red', 'capital': 'Vilnius'},
            'LV': {'name': 'Latvia', 'population': '1.9 million', 'flag_colors': 'Red, White', 'capital': 'Riga'},
            'EE': {'name': 'Estonia', 'population': '1.3 million', 'flag_colors': 'Blue, Black, White', 'capital': 'Tallinn'},
            'LU': {'name': 'Luxembourg', 'population': '630,000', 'flag_colors': 'Red, White, Blue', 'capital': 'Luxembourg City'},
            'MT': {'name': 'Malta', 'population': '520,000', 'flag_colors': 'White, Red', 'capital': 'Valletta'},
            'CY': {'name': 'Cyprus', 'population': '1.2 million', 'flag_colors': 'White, Orange, Green', 'capital': 'Nicosia'},
            'RS': {'name': 'Serbia', 'population': '7 million', 'flag_colors': 'Red, Blue, White', 'capital': 'Belgrade'},
            'BA': {'name': 'Bosnia and Herzegovina', 'population': '3.3 million', 'flag_colors': 'Blue, Yellow, White', 'capital': 'Sarajevo'},
            'MK': {'name': 'North Macedonia', 'population': '2 million', 'flag_colors': 'Red, Yellow', 'capital': 'Skopje'},
            'AL': {'name': 'Albania', 'population': '2.9 million', 'flag_colors': 'Red, Black', 'capital': 'Tirana'},
            'ME': {'name': 'Montenegro', 'population': '620,000', 'flag_colors': 'Red, Gold', 'capital': 'Podgorica'},
            'MD': {'name': 'Moldova', 'population': '2.6 million', 'flag_colors': 'Blue, Yellow, Red', 'capital': 'Chisinau'},
            'BY': {'name': 'Belarus', 'population': '9.4 million', 'flag_colors': 'Red, Green, White', 'capital': 'Minsk'},
            'UA': {'name': 'Ukraine', 'population': '41 million', 'flag_colors': 'Blue, Yellow', 'capital': 'Kyiv'},
            'RU': {'name': 'Russia', 'population': '144 million', 'flag_colors': 'White, Blue, Red', 'capital': 'Moscow'},
            'TR': {'name': 'Turkey', 'population': '85 million', 'flag_colors': 'Red, White', 'capital': 'Ankara'},
            'GE': {'name': 'Georgia', 'population': '3.7 million', 'flag_colors': 'White, Red', 'capital': 'Tbilisi'},
            'AM': {'name': 'Armenia', 'population': '3 million', 'flag_colors': 'Red, Blue, Orange', 'capital': 'Yerevan'},
            'AZ': {'name': 'Azerbaijan', 'population': '10 million', 'flag_colors': 'Blue, Red, Green', 'capital': 'Baku'},
            }

    def load_airports_from_csv(self):
        file = open('airports.csv', 'r', encoding='utf-8')
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            is_large_airport = row['type'] == 'large_airport'
            is_european = row['continent'] == 'EU'
            has_iata = row['iata_code'] != ''
            has_country = row['iso_country'] != ''
            has_name = row['name'] != ''
            
            if is_large_airport and is_european and has_iata and has_country and has_name:
                airport = Airport(row['name'], row['iso_country'])
                self.airports.append(airport)
                self.remaining_countries.add(row['iso_country'])
        
        file.close()

def show_remaining_countries(self):
        if len(self.remaining_countries) == 0:
            print("\nAll countries have been guessed!")
            return

        country_list = []
        for code in self.remaining_countries:
            if code in self.countries:
                country_name = self.countries[code]['name']
                country_list.append(f"{country_name} ({code})")

        country_list.sort()

        print(f"\nRemaining countries ({len(self.remaining_countries)}):")
        i = 0
        while i < len(country_list):
            line = country_list[i:i+3]
            print("  " + ", ".join(line))
            i = i + 3

def get_hint_for_attempt(self, country_code, attempt_number):
        if country_code not in self.countries:
            return
        
        country_info = self.countries[country_code]
        print("\nHint:")
        
        if attempt_number == 1:
            print(f"   Population: {country_info['population']}")
        elif attempt_number == 2:
            print(f"   Flag colors: {country_info['flag_colors']}")
        elif attempt_number == 3:
            print(f"   Capital: {country_info['capital']}")

def ask_for_guess(self):
        while True:
            guess = input("\nEnter country code (2 letters) or 'quit' to exit: ")
            guess = guess.strip().upper()
            
            if guess == 'QUIT':
                return 'QUIT'
            
            if len(guess) == 2 and guess.isalpha():
                return guess
            
            print("Please enter a valid 2-letter country code (e.g., GB, FR, DE)")

def play_one_question(self, airport):
        country_code = airport.country_code
        country_name = self.countries[country_code]['name']

        attempt = 0
        while attempt < 3:
            guess = self.ask_for_guess()

            if guess == 'QUIT':
                return False

            attempt = attempt + 1

            if guess == country_code:
                print(f"\nCORRECT!")
                self.correct_answers = self.correct_answers + 1
                if country_code in self.remaining_countries:
                    self.remaining_countries.remove(country_code)
                return True
            else:
                print("\nWrong!")
                if attempt < 3:
                    self.get_hint_for_attempt(country_code, attempt)
                    remaining_attempts = 3 - attempt
                    print(f"   You have {remaining_attempts} attempt(s) remaining.")
                else:
                    print(f"\nThe correct answer was: {country_name} ({country_code})")

        return True

