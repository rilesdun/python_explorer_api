import logging
import time
from config import api_url

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
from src.accounts.accountHistory import get_account_history
from src.accounts.sons.activeSons import get_active_sons


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

# need to get correct origins - bad practice for CORS "*"

CORS(app, resources={r"/*": {"origins": "*"}})
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
            logging.info(f"Background Task: Successfully fetched block {block_num}")
            self.emit('block update', {'block_num': block_num})
            time.sleep(1.5)

# Register the namespace at the desired endpoint
socketio.on_namespace(LatestBlockNamespace('/api/latest_block'))

@app.route('/api/latest_block_num', methods=['GET'])
def latest_block_num():
    latest_block = get_latest_block()
    return jsonify(latest_block_num=latest_block['block_num'])

@app.route('/api/supply/ppy', methods=['GET'])
def supply_ppy():
    asset_id = request.args.get("asset", "1.3.0")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/btfun', methods=['GET'])
def supply_btfun():
    asset_id = request.args.get("asset", "1.3.1")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/bitcoin', methods=['GET'])
def supply_btc():
    asset_id = request.args.get("asset", "1.3.22")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/hive', methods=['GET'])
def supply_hive():
    asset_id = request.args.get("asset", "1.3.24")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/hbd', methods=['GET'])
def supply_hbd():
    asset_id = request.args.get("asset", "1.3.23")
    supplies = get_supply_details(asset_id)
    return supplies

# max and total are the same, not sure why peerplays asset api has both
@app.route('/api/max_supply/<string:coin_name>', methods=['GET'])
def max_supply_route(coin_name):
    return max_supply(coin_name)

@app.route('/api/total_supply/<string:coin_name>', methods=['GET'])
def total_supply_route(coin_name):
    return total_supply(coin_name)

@app.route('/api/circulating_supply/<string:coin_name>', methods=['GET'])
def circulating_supply_route(coin_name):
    return circulating_supply(coin_name)

@app.route('/api/rich_list/<string:coin_name>', methods=['GET'])
def rich_list_route(coin_name):
    num = request.args.get("num", "25")
    return rich_list(coin_name, num)


@app.route('/api/block/<int:block_num>', methods=['GET'])
def block(block_num):
    block_info = get_block_info(block_num)
    if block_info is not None:
        logging.info(f"Page Load: Successfully fetched block {block_num}")
        return jsonify(block_info=block_info)
    else:
        return "Error fetching block information", 400

@app.route('/api/transactions')
def transactions():
    transactions = get_latest_transactions()
    return jsonify(transactions=transactions)

@app.route('/api/account_history/<account_name>')
def account_history(account_name):
    history = get_account_history(account_name)
    return jsonify(history)

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

@app.route('/api/accounts/active_sons', methods=['GET'])
def active_sons():
    sons = get_active_sons()
    return sons

if __name__ == '__main__':
    socketio.run(app, debug=True)