""" 
This module contains the total supply endpoint.
"""
from peerplays.asset import Asset
from flask import Response
from src.supply.common import get_supplies, peerplays, ASSET_IDS


def total_supply(coin_name):
    """ 
    This endpoint returns the total supply for the given coin name. 
    """
    asset_id = ASSET_IDS.get(coin_name)
    if asset_id is None:
        return Response("Invalid coin name", status=400)
    A = Asset(asset_id, blockchain_instance=peerplays)
    supply = get_supplies(A)["total"]
    return Response(supply, content_type='text/plain')