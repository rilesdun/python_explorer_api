from flask import Flask, render_template
from flask import jsonify
from src.blocks import get_block_info
from src.witnesses import list_active_witnesses
from src.assets import list_all_assets
from src.allAccounts import list_all_accounts


app = Flask(__name__)

@app.route('/block/<int:block_num>', methods=['GET'])
def block(block_num):
    block_info = get_block_info(block_num)
    if block_info is not None:
        return render_template('block.html', block_info=block_info, should_refresh=False)
    else:
        return "Error fetching block information", 400

@app.route('/', methods=['GET'])
def latest_block():
    block_info = get_block_info()
    if block_info is not None:
        return render_template('block.html', block_info=block_info, should_refresh=True)
    else:
        return "Error fetching block information", 400

@app.route('/accounts', methods=['GET'])
def accounts():
    witness_list = list_all_accounts()
    if witness_list is not None:
        return render_template('allAccounts.html', witness_list=witness_list)
    else:
        return "Error fetching witness information", 400
    
@app.route('/accounts/witnesses', methods=['GET'])
def activeWitnesses():
    witness_list = list_active_witnesses()
    if witness_list is not None:
        return render_template('witnesses.html', witness_list=witness_list)
    else:
        return "Error fetching witness information", 400

@app.route('/assets', methods=['GET'])
def assets():
    asset_list = list_all_assets()
    if asset_list is not None:
        return render_template('assets.html', asset_list=asset_list)
    else:
        return "Error fetching asset information", 400

if __name__ == '__main__':
    app.run(debug=True)