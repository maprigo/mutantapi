from flask import render_template, session, flash, request, json, jsonify, abort

from functions.mutant import verificar, horizontal, vertical, diagOne, diagonal, isMutant
from models import Adn
from . import routes


@routes.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('main.html')
    else:
        return render_template('main.html')

@routes.route("/mutant/", methods=["POST"])
def ismutant():
    if request.is_json:
        content = request.get_json()
        if (verificar(content["dna"])):
            if (isMutant(content["dna"])):
                return jsonify({'status': 200, 'response': ' MUTANT '})
            else:
                return abort(403, description="HUMAN")
        else:
            return abort(403, description="PATTERN WRONG")
    return abort(403, description="JSON ERROR")


@routes.route("/stats/", methods=["POST"])
def stats():
    mutants = Adn.query.filter_by(type_id=1).count()
    humans = Adn.query.filter_by(type_id=2).count()
    if humans == 0:
        ratio = "NO DATA"
    else:
        ratio = mutants / humans
    return jsonify({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": ratio})
