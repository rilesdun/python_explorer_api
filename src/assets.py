#broken - need to implement https://gitlab.com/PBSA/peerplays-1.0/tools-libs/marketcap-api

from peerplays import PeerPlays
from peerplays.asset import Asset

# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

def list_all_assets():
    
    assets = peerplays.list_assets("", 100)  
    
    asset_info = []

    for asset in assets:
        asset_obj = Asset(asset["symbol"], blockchain_instance=peerplays)
        asset_info.append({
            "symbol": asset_obj["symbol"],
            "precision": asset_obj["precision"],
            "issuer": asset_obj["issuer"],
            "description": asset_obj["description"],
            "options": asset_obj["options"]
        })

    return asset_info