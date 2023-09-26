"""
Rich list for a given coin
"""
from peerplays.asset import Asset
from flask import jsonify
from src.supply.common import sats_to_fixed,ASSET_IDS
from peerplays_instance import peerplays


def rich_list(coin_name, num="25"):
    """
    This endpoint returns the rich list for the given coin name.
    """
    asset_id = ASSET_IDS.get(coin_name)
    if asset_id is None:
        return jsonify({"error": "Invalid coin name"}), 400
    limit = int(num)
    A = Asset(asset_id, blockchain_instance=peerplays) # pylint: disable=invalid-name
    P = A["precision"] # pylint: disable=invalid-name
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
