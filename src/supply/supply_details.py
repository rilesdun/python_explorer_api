from .common import get_supplies
from peerplays.asset import Asset
from peerplays import PeerPlays

def get_supply_details(asset_id="1.3.0"):
    peerplays = PeerPlays("wss://ca.peerplays.info/api")
    A = Asset(asset_id, blockchain_instance=peerplays)
    supplies = get_supplies(A)

    return supplies