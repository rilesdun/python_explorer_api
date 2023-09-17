"""
This module contains the API endpoint for fetching the list of active witnesses.
"""
from flask import jsonify
from src.accounts.witnesses.witnesses import list_active_witnesses

def active_witnesses():
    """
    This endpoint returns the list of active witnesses.
    """
    witness_list = list_active_witnesses()
    default_attributes = ['id', 'witness_account','signing_key', 'total_votes',
                          'url', 'total_missed', 'last_confirmed_block_num']

    if witness_list is not None:
        return jsonify(witness_list=witness_list, default_attributes=default_attributes)
    return "Error fetching witness information", 400
    