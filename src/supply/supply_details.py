""" 
This module is used to get the supply details of the asset.
"""
from peerplays.asset import Asset
from src.supply.common import get_supplies
from peerplays_instance import peerplays


def get_supply_details(asset_id="1.3.0"):
    """ 
    returns the supply details of the asset 
    """
    A = Asset(asset_id, blockchain_instance=peerplays) # pylint: disable=invalid-name
    supplies = get_supplies(A)

    return supplies
