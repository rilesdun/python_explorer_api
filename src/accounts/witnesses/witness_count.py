"""
Returns the number of active witnesses and a list of their names.
"""
from flask import jsonify
from src.accounts.witnesses.witnesses import list_active_witnesses


def witness_count():
    """
    This endpoint returns the number of active witnesses and a list of their names.
    """
    witness_list = list_active_witnesses()
    return jsonify(witness_count=len(witness_list), witnesses=witness_list)
