"""
This is the main application module.
"""

import logging

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from peerplays.exceptions import AccountDoesNotExistsException
from cache_config import cache

from src.accounts.get_account import get_account_info
from src.accounts.witnesses.active_witnesses import list_active_witnesses
from src.accounts.witnesses.witness_count import witness_count
from src.accounts.sons.active_sons import get_active_sons
from src.accounts.account_history import get_account_history

from src.blocks import get_block_info

from src.get_latest_transactions import get_latest_transactions
from src.latest_block import get_latest_block

from src.supply.supply_details import get_supply_details
from src.supply.max_supply import max_supply
from src.supply.total_supply import total_supply
from src.supply.circulating_supply import circulating_supply
from src.supply.rich_list import rich_list

app = Flask(__name__)

# need to get correct origins - bad practice for CORS "*"

CORS(app, resources={r"/*": {"origins": "*"}})
cache.init_app(app)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s')
@app.route('/api/latest_block_num', methods=['GET'])
def latest_block_num():
    """
    This endpoint returns the latest block number.
    """
    latest_block = get_latest_block()
    return jsonify(latest_block_num=latest_block['block_num'])

@app.route('/api/supply/ppy', methods=['GET'])
def supply_ppy():
    """
    This endpoint returns the supply details for the asset 'ppy'.
    """
    asset_id = request.args.get("asset", "1.3.0")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/btfun', methods=['GET'])
def supply_btfun():
    """
    This endpoint returns the supply details for the asset 'btfun'.
    """
    asset_id = request.args.get("asset", "1.3.1")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/bitcoin', methods=['GET'])
def supply_btc():
    """
    This endpoint returns the supply details for the asset 'bitcoin'.
    """
    asset_id = request.args.get("asset", "1.3.22")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/hive', methods=['GET'])
def supply_hive():
    """
    This endpoint returns the supply details for the asset 'hive'.
    """
    asset_id = request.args.get("asset", "1.3.24")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/supply/hbd', methods=['GET'])
def supply_hbd():
    """
    This endpoint returns the supply details for the asset 'hbd'.
    """
    asset_id = request.args.get("asset", "1.3.23")
    supplies = get_supply_details(asset_id)
    return supplies

@app.route('/api/max_supply/<string:coin_name>', methods=['GET'])
def max_supply_route(coin_name):
    """
    This endpoint returns the maximum supply for the given coin name.
    """
    return max_supply(coin_name)

@app.route('/api/total_supply/<string:coin_name>', methods=['GET'])
def total_supply_route(coin_name):
    """
    This endpoint returns the total supply for the given coin name.
    """
    return total_supply(coin_name)

@app.route('/api/circulating_supply/<string:coin_name>', methods=['GET'])
def circulating_supply_route(coin_name):
    """
    This endpoint returns the circulating supply for the given coin name.
    """
    return circulating_supply(coin_name)

@app.route('/api/rich_list/<string:coin_name>', methods=['GET'])
def rich_list_route(coin_name):
    """
    This endpoint returns the rich list for the given coin name.
    """
    num = request.args.get("num", "25")
    return rich_list(coin_name, num)

@app.route('/api/block/<int:block_num>', methods=['GET'])
def block(block_num):
    """
    This endpoint returns the block information for the given block number.
    """
    block_info = get_block_info(block_num)
    if block_info is not None:
        logging.info("Page Load: Successfully fetched block %s", block_num)
        return jsonify(block_info=block_info)
    return "Error fetching block information", 400

@app.route('/api/transactions')
def transactions():
    """
    This endpoint returns the latest transactions.
    """
    latest_transactions = get_latest_transactions()
    return jsonify(transactions=latest_transactions)

@app.route('/api/account_history/<account_name>')
def account_history(account_name):
    """
    This endpoint returns the account history for the given account name.
    """
    history = get_account_history(account_name)
    return jsonify(history)

@app.route('/api/accounts/<string:account_name>', methods=['GET'])
def account_info(account_name):
    """
    This endpoint returns the account information for the given account name.
    """
    try:
        info = get_account_info(account_name)
        return jsonify(account_info=info)
    except AccountDoesNotExistsException:
        return jsonify(error="Account does not exist"), 404
    except Exception as error: # pylint: disable=broad-except
        return str(error), 400

@app.route('/api/accounts/witnesses', methods=['GET'])
def active_witnesses():
    """
    This endpoint returns the list of active witnesses.
    """
    witness_list = list_active_witnesses()
    default_attributes = [
    'id', 'witness_account', 'signing_key', 'total_votes', 
    'url', 'total_missed', 'last_confirmed_block_num'
]
    if witness_list is not None:
        return jsonify(witness_list=witness_list, default_attributes=default_attributes)
    return "Error fetching witness information", 400

@app.route('/api/accounts/witness_count', methods=['GET'])
def get_witnesses():
    """
    This endpoint returns the count of witnesses.
    """
    return witness_count()

@app.route('/api/accounts/active_sons', methods=['GET'])
def active_sons():
    """
    This endpoint returns the list of active sons.
    """
    sons = get_active_sons()
    return sons

if __name__ == '__main__':
    app.run()
