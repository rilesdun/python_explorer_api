from .common import get_supplies, peerplays, ASSET_IDS
from peerplays.asset import Asset
from flask import Response

def total_supply(coin_name):
    asset_id = ASSET_IDS.get(coin_name)
    if asset_id is None:
        return Response("Invalid coin name", status=400)
    A = Asset(asset_id, blockchain_instance=peerplays)
    supply = get_supplies(A)["total"]
    return Response(supply, content_type='text/plain')