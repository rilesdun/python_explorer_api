from .witnesses import list_active_witnesses
from flask import jsonify

def witness_count():
    witness_list = list_active_witnesses()
    return jsonify(witness_count=len(witness_list), witnesses=witness_list)