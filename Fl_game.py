import random, mysql.connector
from flask import Flask, request
from flask_cors import CORS
import json
import requests
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight',
    user='root',
    password='Ratgai#1!',
    autocommit=True
)

print("\n                                          ****************  Wel-Come To Game Treasure Hunt  ***************")
user = input("Enter Player Name: ")
print("Welcome to board " + user + "!\n")

user = input("How do you want to proceed ahead?"
             "\n1.Start Game"
             "\n2.Watch Tutorial\n ")

user = input("Choose difficulty level:"
             "\n1.Basic Version:"
             "\n2.Pro Version"
             "\n")
print("Let Play!")

app = Flask(__name__)
@app.route('/game')
def game():

    areaSelection = []
    returnlist = []

    i = 0
    while i < 5:
        name = input("\nEnter name of the country where you want to fly: ")
        print("\nHere are the list of 3 random airport from the country you have chosen:")

        def weather():
            name_city = input("\n Please guess the name of the city of this airport? ")
            request = f"https://api.openweathermap.org/data/2.5/weather?q={name_city}&appid=8614c7f206c8dabab99a14d0736a39d2"
            result = requests.get(request).json()
            tem_F = result['main']['temp']
            celsius = round((tem_F - 273.15), 2)
            print('\nWeather of the chosen city is:', result['weather'][0]['main'])
            print(f'Current temperature: {celsius} C')

        def map():


        def locations():
            sql = "select airport.name from airport " \
                  "inner join country on airport.iso_country=country.iso_country " \
                  "where country.name='" + name + "'"

            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()

            airports = []
            for x in range(len(result)):
                airports.append(result[x][0])
            return airports

        def airport_selection():
            airport = locations()
            chosen = random.sample(airport, 3)
            print(f"1. {chosen[0]}")
            areaSelection.append(chosen[0])
            print(f"2. {chosen[1]}")
            areaSelection.append(chosen[1])
            print(f"3. {chosen[2]}\n")
            areaSelection.append(chosen[2])
            return areaSelection


        def option():
            chosen = areaSelection
            while True:
                player = input("Enter number from the list of airport of your choice: ")

                if int(player) == 1:
                    print(f"You have chosen {chosen[0]}.\n")
                    returnlist.append(chosen[0])
                    weather()

                    break

                elif int(player) == 2:
                    print(f"You have chosen {chosen[1]}.\n")
                    returnlist.append(chosen[1])
                    weather()
                    break

                elif int(player) == 3:
                    print(f"You have chosen {chosen[2]}.\n")
                    returnlist.append(chosen[2])
                    weather()
                    break

                else:
                    print(f"OOPs! Wrong input.")
                    break
            return returnlist

        areaSelection.clear()
        returnlist.clear()

        def treasure():
            result = random.randint(1, 2)
            total_score = 0
            final_score = 0
            final_score += total_score
            if result == 1:
                print("Congratulation! You found the Treasure.")
                print("You got 500 points.")

                total_score += 500
                print("Your score is " + str(total_score))

            else:
                print("Unfortunately! No any Treasure. Try your luck in next destination.")
                print("no points.")

                total_score += 0
                print("Your score is " + str(total_score))

            return total_score

            print(final_score)

        airport_selection()
        option()
        treasure()
        i += 1

game()

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)