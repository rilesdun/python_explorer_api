""" 
This module is used to get the supply details of the asset.
"""
from peerplays.asset import Asset
from peerplays import PeerPlays
from src.supply.common import get_supplies


def get_supply_details(asset_id="1.3.0"):
    """ 
    returns the supply details of the asset 
    """
    peerplays = PeerPlays("wss://ca.peerplays.info/api")
    A = Asset(asset_id, blockchain_instance=peerplays)
    supplies = get_supplies(A)

    return supplies
