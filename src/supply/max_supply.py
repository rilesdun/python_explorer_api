"""
This module contains the max_supply function, which returns the maximum supply of a coin.
"""
from peerplays.asset import Asset
from flask import Response
from src.supply.common import get_supplies, peerplays, ASSET_IDS


ASSET_IDS = {
    "ppy": "1.3.0",
    "btfun": "1.3.1",
    "bitcoin": "1.3.22",
    "hive": "1.3.24",
    "hbd": "1.3.23",
    # Add more mappings as needed
}

def max_supply(coin_name):
    """ 
    This endpoint returns the maximum supply for the given coin name.
    """
    asset_id = ASSET_IDS.get(coin_name)
    if asset_id is None:
        return Response("Invalid coin name", status=400)
    A = Asset(asset_id, blockchain_instance=peerplays) # pylint: disable=invalid-name
    supply = get_supplies(A)["maximum"]
    return Response(supply, content_type='text/plain')
