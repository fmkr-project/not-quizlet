
from flask import Flask, render_template, request, redirect, url_for
from db import Database
from werkzeug.security import generate_password_hash, check_password_hash
from structures import Card, Deck
import env

app = Flask(__name__)
# Initialize the database object
db = Database()

@app.route('/')
def index():
    # Fetch all cards to display
    cards = db.execute_query("SELECT * FROM cards", (), False)
    return render_template('index.html', cards=cards)

@app.route('/modify/<int:card_id>', methods=['GET', 'POST'])
def modify_card(card_id):
    if request.method == 'POST':
        # Get data from form
        front_side = request.form['front_side']
        back_side = request.form['back_side']
        
        # Update the card in the database
        db.modify_card(card_id, front_side, back_side)
        return redirect(url_for('index'))
    # Fetch card details for the given card_id
    card_details = db.execute_query("SELECT * FROM cards WHERE id = ?", (card_id,), False)
    if card_details:
        card_ = Card(*card_details[0])
        return render_template('modify_card.html', card=card_)
    else:
        return "Card not found", 404

if __name__ == '__main__':
    app.run("127.0.0.1",4000, debug=True)
