# tuodaan tarvittavat kirjastot
import csv      # csv-tiedoston lukemiseen
import random   # satunnaisten lentoasemien valintaan
import os


# lentoasema-luokka, jossa on nimi ja maakoodi
class Airport:
    def __init__(self, name, country_code):
        # tallennetaan lentoaseman nimi ja maakoodi
        self.name = name
        self.country_code = country_code


# peli-luokka, jossa on kaikki pelin logiikka
class Game:
    def __init__(self):
        # alustetaan pelin muuttujat
        self.airports = []  # lista lentoasemista
        self.countries = {}  # maatiedot
        self.remaining_countries = set()  # jäljellä olevat maat
        self.correct_answers = 0  # oikeat vastaukset
        self.total_questions = 0  # kysymysten määrä
        
        # ladataan maadata ja lentoasemat
        self.load_country_data()
        self.load_airports_from_csv()
    
    def load_country_data(self):
        # ladataan euroopan maiden tiedot sanakirjaan
        # jokaisessa on nimi, väkiluku, lipun värit ja pääkaupunki
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
        # ladataan lentoasemat csv-tiedostosta
        # etsitään tiedosto skriptin kansiosta
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, 'airports.csv')
        file = open(csv_path, 'r', encoding='utf-8')
        csv_reader = csv.DictReader(file)
        
        # käydään läpi jokainen rivi csv-tiedostossa
        for row in csv_reader:
            # tarkistetaan, että lentoasema täyttää ehdot
            is_large_airport = row['type'] == 'large_airport'
            is_european = row['continent'] == 'EU'
            has_iata = row['iata_code'] != ''
            has_country = row['iso_country'] != ''
            has_name = row['name'] != ''
            
            # otetaan vain suuret eurooppalaiset lentoasemat
            if is_large_airport and is_european and has_iata and has_country and has_name:
                airport = Airport(row['name'], row['iso_country'])
                self.airports.append(airport)
                self.remaining_countries.add(row['iso_country'])
        
        file.close()
    
    def show_remaining_countries(self):
        # näytetään jäljellä olevat maat
        if len(self.remaining_countries) == 0:
            print("\nAll countries have been guessed!")
            return
        
        # luodaan lista maista
        country_list = []
        for code in self.remaining_countries:
            if code in self.countries:
                country_name = self.countries[code]['name']
                country_list.append(f"{country_name} ({code})")
        
        country_list.sort()
        
        # tulostetaan maat kolmessa sarakkeessa
        print(f"\nRemaining countries ({len(self.remaining_countries)}):")
        i = 0
        while i < len(country_list):
            line = country_list[i:i+3]
            print("  " + ", ".join(line))
            i = i + 3
    
    def get_hint_for_attempt(self, country_code, attempt_number):
        # annetaan vihje arvauskerran mukaan
        if country_code not in self.countries:
            return
        
        country_info = self.countries[country_code]
        print("\nHint:")
        
        # eri vihje jokaiselle arvaukselle
        if attempt_number == 1:
            print(f"   Population: {country_info['population']}")
        elif attempt_number == 2:
            print(f"   Flag colors: {country_info['flag_colors']}")
        elif attempt_number == 3:
            print(f"   Capital: {country_info['capital']}")
    
    def ask_for_guess(self):
        # kysytään pelaajalta arvaus
        while True:
            guess = input("\nEnter country code (2 letters) or 'quit' to exit: ")
            guess = guess.strip()
            
            # jos pelaaja haluaa lopettaa
            if guess.upper() == 'QUIT':
                return 'QUIT'
            
            # tarkistetaan, että syöte on kelvollinen (2 isoa kirjainta)
            if len(guess) == 2 and guess.isalpha() and guess.isupper():
                return guess
            
            print("Please enter exactly 2 uppercase letters (e.g., GB, FR, DE)")
    
    def play_one_question(self, airport):
        # pelataan yksi kysymyskierros
        country_code = airport.country_code
        country_name = self.countries[country_code]['name']
        
        # pelaajalla on 3 yritystä
        attempt = 0
        while attempt < 3:
            guess = self.ask_for_guess()
            
            # jos pelaaja haluaa lopettaa
            if guess == 'QUIT':
                return False
            
            attempt = attempt + 1
            
            # tarkistetaan vastaus
            if guess == country_code:
                print(f"\nCORRECT!")
                self.correct_answers = self.correct_answers + 1
                if country_code in self.remaining_countries:
                    self.remaining_countries.remove(country_code)
                return True
            else:
                print("\nWrong!")
                # annetaan vihje, jos yrityksiä jäljellä
                if attempt < 3:
                    self.get_hint_for_attempt(country_code, attempt)
                    remaining_attempts = 3 - attempt
                    print(f"   You have {remaining_attempts} attempt(s) remaining.")
                else:
                    print(f"\nThe correct answer was: {country_name} ({country_code})")
        
        return True
    
    def show_final_score(self):
        # näytetään loppupisteet
        print("\n" + "="*60)
        print("   GAME OVER")
        print("="*60)
        
        if self.total_questions > 0:
            print(f"\nCorrect answers: {self.correct_answers}/{self.total_questions}")
        else:
            print("\nNo questions answered.")
        
        print("\nThank you for playing!")
        print("="*60 + "\n")
    
    def start(self):
        # käynnistetään peli
        if len(self.airports) == 0:
            print("Cannot start game without airport data.")
            return
        
        # pääpelilooppi
        while True:
            # tarkistetaan onko kaikki maat arvattu
            if len(self.remaining_countries) == 0:
                print("\nCongratulations! You've guessed all countries!")
                self.show_final_score()
                return
            
            # valitaan vain jäljellä olevien maiden lentoasemat
            available_airports = []
            for airport in self.airports:
                if airport.country_code in self.remaining_countries:
                    available_airports.append(airport)
            
            if len(available_airports) == 0:
                print("\nNo more airports available!")
                self.show_final_score()
                return
            
            # valitaan satunnainen lentoasema
            airport = random.choice(available_airports)
            
            self.total_questions = self.total_questions + 1
            
            # näytetään kysymys
            print(f"\n{'-'*60}")
            print(f"Question #{self.total_questions}")
            print(f"{'-'*60}")
            print(f"\nAirport: {airport.name}")
            self.show_remaining_countries()
            
            # pelataan kysymyskierros
            continue_playing = self.play_one_question(airport)
            
            if not continue_playing:
                self.total_questions = self.total_questions - 1
                self.show_final_score()
                return
            
            print(f"\nCurrent score: {self.correct_answers}/{self.total_questions}")
            
            # kysytään haluaako pelaaja jatkaa
            answer = input("\nContinue to next airport? (y/n): ").strip().lower()
            if answer != 'y':
                self.show_final_score()
                return


# luodaan peli ja käynnistetään se
game = Game()
game.start()
