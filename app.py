import logging
import time
from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import Namespace

from peerplays.peerplays import PeerPlays
from peerplays.asset import Asset
from peerplays.amount import Amount

from src.blocks import get_block_info
from src.witnesses import list_active_witnesses
from src.allAccounts import list_all_accounts
from src.getLatestTransactions import get_latest_transactions
from src.latestBlock import get_latest_block
from src.max_supply import get_supply

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # You can specify your specific origins instead of "*"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
socketio = SocketIO(app, cors_allowed_origins="*") # You can specify your specific origins instead of "*"

class LatestBlockNamespace(Namespace):
    def on_connect(self):
        socketio.start_background_task(self.background_thread)

    def background_thread(self):
        while True:
            block = get_latest_block()
            block_num = block['block_num'] if block else None
            self.emit('block update', {'block_num': block_num})
            time.sleep(1) # Adjust this based on the actual block time

# Register the namespace at the desired endpoint
socketio.on_namespace(LatestBlockNamespace('/api/latest_block'))

@app.route('/api/latest_block_num', methods=['GET'])
def latest_block_num():
    latest_block = get_latest_block()
    return jsonify(latest_block_num=latest_block['block_num'])

@app.route('/api/supply', methods=['GET'])
def supply():
    asset_id = request.args.get("asset", "1.3.0")
    supplies = get_supply(asset_id)
    return jsonify(supplies)

@app.route('/api/block/<int:block_num>', methods=['GET'])
def block(block_num):
    block_info = get_block_info(block_num)
    if block_info is not None:
        return jsonify(block_info=block_info)
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

@app.route('/api/accounts/witness_count', methods=['GET'])
def get_witnesses():
    witness_list = list_active_witnesses()
    return jsonify(witness_count=len(witness_list), witnesses=witness_list)


if __name__ == '__main__':
    socketio.run(app, debug=True)