import requests
from bs4 import BeautifulSoup
import os

def thesaurus(term):
    # Using bs4 to parse through the thesaurus.com html
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    ant = [span.text for span in soup.findAll('a', {'class': 'css-15bafsg eh475bn0'})]
    syn = [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]
    print("Synonyms:")
    print(syn)
    print("Antonyms:")
    print(ant)


def user_input():
    print("Welcome to the CLI thesaurus!")

    #initializing variables
    again = "Yes"
    run = 0
    words = ['Yes', 'yes', 'No', 'no', 'y', 'Y', 'n', 'n']

    #Main Loop
    while again == "Yes" or again == "yes" or again == "Y" or again == "y":
        term = input("Enter Word: ")
        print(term)
        thesaurus(term)
        again = input("Enter another word?(yes/no): ")
        run += 1
        if run > 0:
            os.system('clear')

    # making sure user inputs yes or no
        if again not in words:
            check = 1
            while check == 1:
                again = input("its a yes or no question (check spelling):")
                if again in words:
                    check = 0
        if again == "No" or again == "no" or again == "n" or again == "N":
            print("Good Bye!")
user_input()