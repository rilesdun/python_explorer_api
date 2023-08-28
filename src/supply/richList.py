from .common import sats_to_fixed, peerplays, ASSET_IDS
from peerplays.asset import Asset
from flask import jsonify

def rich_list(coin_name, num="25"):
    asset_id = ASSET_IDS.get(coin_name)
    if asset_id is None:
        return jsonify({"error": "Invalid coin name"}), 400
    limit = int(num)
    A = Asset(asset_id, blockchain_instance=peerplays)
    P = A["precision"]
    richlist = A.blockchain.rpc.get_asset_holders(asset_id, 0, limit, api="asset")
    result = [
        {
            **{k: i[k] for k in ["name", "account_id"]},
            "balance": sats_to_fixed(i["amount"], P),
            "symbol": A["symbol"]
        }
        for i in richlist
    ]
    return jsonify(result)