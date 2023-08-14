from peerplays.asset import Asset
from peerplays import PeerPlays

def sats_to_fixed(amount, P):
    V = int(amount) / 10**P
    return "{:.{prec}f}".format(V, prec=P)

def get_supplies(asset):
    P = asset["precision"]
    max_supply = sats_to_fixed(asset["options"]["max_supply"], P)
    ddo = asset.blockchain.rpc.get_objects([asset["dynamic_asset_data_id"]])[0]
    current_supply = sats_to_fixed(ddo["current_supply"], P)
    return {
        "id": asset["id"],
        "symbol": asset["symbol"],
        "maximum": max_supply,
        "total": max_supply,
        "circulating": current_supply
    }


def get_supply(asset_id="1.3.0"):
    peerplays = PeerPlays("wss://ca.peerplays.info/api")
    A = Asset(asset_id, blockchain_instance=peerplays)
    supplies = get_supplies(A)

    return supplies