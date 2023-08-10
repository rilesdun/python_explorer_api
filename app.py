from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS
from src.blocks import get_block_info
from src.witnesses import list_active_witnesses
from src.allAccounts import list_all_accounts
from src.getLatestTransactions import get_latest_transactions

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def latest_block():
    block_info = get_block_info()
    if block_info is not None:
        return jsonify(block_info=block_info, should_refresh=True)
    else:
        return "Error fetching block information", 400

@app.route('/api/block/<int:block_num>', methods=['GET'])
def block(block_num):
    block_info = get_block_info(block_num)
    if block_info is not None:
        return jsonify(block_info=block_info, should_refresh=False)
    else:
        return "Error fetching block information", 400

@app.route('/api/transactions')
def transactions():
    transactions = get_latest_transactions()
    return jsonify(transactions=transactions)

@app.route('/api/accounts', methods=['GET'])
def accounts():
    witness_list = list_all_accounts()
    if witness_list is not None:
        return jsonify(witness_list=witness_list)
    else:
        return "Error fetching witness information", 400
    
@app.route('/api/accounts/witnesses', methods=['GET'])
def activeWitnesses():
    witness_list = list_active_witnesses()
    default_attributes = ['id', 'witness_account', 'signing_key', 'total_votes', 'url', 'total_missed', 'last_confirmed_block_num']

    if witness_list is not None:
        return jsonify(witness_list=witness_list, default_attributes=default_attributes)
    else:
        return "Error fetching witness information", 400

if __name__ == '__main__':
    app.run(debug=True)