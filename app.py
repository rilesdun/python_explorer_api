import logging
import time

from peerplays.exceptions import AccountDoesNotExistsException


from flask import Flask, render_template
from flask import jsonify
from flask import request
from cache_config import cache
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import Namespace

from peerplays.peerplays import PeerPlays
from peerplays.asset import Asset
from peerplays.amount import Amount

from src.accounts.getAccount import get_account_info
from src.accounts.witnesses.active_witnesses import list_active_witnesses
from src.accounts.witnesses.witness_count import witness_count

from src.blocks import get_block_info

from src.getLatestTransactions import get_latest_transactions
from src.latestBlock import get_latest_block

from src.supply.common import get_supplies, peerplays
from src.supply.supply_details import get_supply_details
from src.supply.max_supply import max_supply
from src.supply.total_supply import total_supply
from src.supply.circulating_supply import circulating_supply
from src.supply.richList import rich_list





app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # You can specify your specific origins instead of "*"
cache.init_app(app)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
socketio = SocketIO(app, cors_allowed_origins="*") # You can specify your specific origins instead of "*"

class LatestBlockNamespace(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.should_stop = False

    def on_connect(self):
        print('Client connected')
        self.should_stop = False
        socketio.start_background_task(self.background_thread)

    def on_disconnect(self):
        print('Client disconnected')
        self.should_stop = True

    def background_thread(self):
        while not self.should_stop:
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
    supplies = get_supply_details(asset_id)
    return supplies


# max and total are the same, not sure why peerplays asset api has both
@app.route('/api/max_supply', methods=['GET'])
def max_supply_route():
    return max_supply()

@app.route('/api/total_supply', methods=['GET'])
def total_supply_route():
    return total_supply()

@app.route('/api/circulating_supply', methods=['GET'])
def circulating_supply_route():
    return circulating_supply()

@app.route('/api/rich_list', methods=['GET'])
def rich_list_route():
    return rich_list()


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

@app.route('/api/accounts/<string:account_name>', methods=['GET'])
def account_info(account_name):
    try:
        account_info = get_account_info(account_name)
        return jsonify(account_info=account_info)
    except AccountDoesNotExistsException:
        return jsonify(error="Account does not exist"), 404
    except Exception as e:
        return str(e), 400


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
    return witness_count()


if __name__ == '__main__':
    socketio.run(app, debug=True)