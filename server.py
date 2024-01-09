from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def guess():
    return "<body style='background-color:powderblue;'><h1 style='text-align: center'>Guess a number between 0 and 9:</h1>" \
            "<img src='https://media0.giphy.com/media/3o7aCSPqXE5C6T8tBC/200w.webp?cid=ecf05e47v8xxnexgm2ckb88etxuxwd4bpyi4ea9bhu0jp3se&ep=v1_gifs_search&rid=200w.webp&ct=g'></body>"

rand_num = random.randint(0, 9)

@app.route("/<int:number>")
def number_guessed(number):
    if number > rand_num:
        return "<body style='background-color:powderblue;'><h1 style='color: red'><b>Number is too high!</b></h1>" \
                "<img src='https://media1.giphy.com/media/3UkLhoyi553r2/giphy.webp?cid=ecf05e47ky005mo32bum6czwncana9qou1wqsb72xbdcy266&ep=v1_gifs_search&rid=giphy.webp&ct=g'></body>"
    elif number < rand_num:
        return "<body style='background-color:powderblue;'><h1 style='color: red'>Number is too low:</h1>" \
                "<img src='https://media1.giphy.com/media/3UkLhoyi553r2/giphy.webp?cid=ecf05e47ky005mo32bum6czwncana9qou1wqsb72xbdcy266&ep=v1_gifs_search&rid=giphy.webp&ct=g'></body>"
    else:
        return "<body style='background-color:powderblue;'><h2 style='color: green'>You guessed correctly!</h2>" \
                "<img src='https://media1.giphy.com/media/iJgoGwkqb1mmH1mES3/200w.webp?cid=ecf05e47legavycdkis2zbg0rjflyfyxtoungp9lyrw0vwme&ep=v1_gifs_search&rid=200w.webp&ct=g'></body>"

if __name__ == ("__main__"):
    app.run(debug=True)
