from .witnesses import list_active_witnesses
from flask import jsonify

def active_witnesses():
    witness_list = list_active_witnesses()
    default_attributes = ['id', 'witness_account', 'signing_key', 'total_votes', 'url', 'total_missed', 'last_confirmed_block_num']

    if witness_list is not None:
        return jsonify(witness_list=witness_list, default_attributes=default_attributes)
    else:
        return "Error fetching witness information", 400