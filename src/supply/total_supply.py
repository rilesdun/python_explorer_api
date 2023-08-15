from .common import get_supplies, peerplays
from peerplays.asset import Asset
from flask import Response, request

def total_supply():
    asset_id = request.args.get("asset", "1.3.0")
    A = Asset(asset_id, blockchain_instance=peerplays)
    supply = get_supplies(A)["total"]
    return Response(supply, content_type='text/plain')
