from .common import sats_to_fixed, peerplays
from peerplays.asset import Asset
from flask import jsonify, request

def rich_list():
    asset_id = request.args.get("asset", "1.3.0")
    limit = int(request.args.get("num", "25"))
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
