from flask import Flask, request, jsonify, render_template, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.table import Table

app = Flask(__name__)

DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def populate(): 
    games = [
        Table(game_name='DEAD SPACE REMAKE', plataform='PS5', price=350, quantity=10),
        Table(game_name='FORSPOKEN', plataform='PC', price=299, quantity=8),
        Table(game_name='DEAD ISLAND 2', plataform='PS5', price=350, quantity=10),
        Table(game_name='HOGWARTS LEGACY', plataform='PC', price=219, quantity=7),
        Table(game_name='WILD HEARTS', plataform='XBox Series', price=350, quantity=7),
        Table(game_name='RESIDENT EVIL 4', plataform='PS5', price=289, quantity=10),
        Table(game_name='RESIDENT EVIL 4', plataform='Switch', price=350, quantity=10)]
    session.add_all(games)
    session.commit()



@app.route('/insert', methods=['POST'])
def insert():
    game_name = request.form['game_name']
    plataform = request.form['plataform']
    price = request.form['price']
    quantity = request.form['quantity']

    new_game = Table(game_name=game_name, plataform=plataform, price=price, quantity=quantity)
    session.add(new_game)
    session.commit()
    return redirect('/')

def get_games():
    games = session.query(Table).all()

    for game in games:
        print(f'ID: {id}, Nome: {game.game_name}, Preço: {game.price} , Quantidade: {game.quantity}, Plataforma: {game.plataform}')

@app.route('/')
def index():
    populate()
    get_games()
    return render_template('index.html')

# Executa o servidor Flask
if __name__ == '__main__':
    Base.metadata.create_all(bind = engine)
    app.run(debug=True)