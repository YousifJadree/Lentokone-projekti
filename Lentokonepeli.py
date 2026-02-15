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
