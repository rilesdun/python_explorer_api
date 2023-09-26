"""
Common functions for supply endpoints
"""

ASSET_IDS = {
    "ppy": "1.3.0",
    "btfun": "1.3.1",
    "bitcoin": "1.3.22",
    "hive": "1.3.24",
    "hbd": "1.3.23"
    }

def sats_to_fixed(amount, P): # pylint: disable=invalid-name
    """
    Convert an amount in satoshis to a fixed point number
    """
    V = int(amount) / 10**P # pylint: disable=invalid-name
    return f"{V:.{P}f}"

def get_supplies(asset):
    """
    Get the supply details for an asset
    """
    P = asset["precision"] # pylint: disable=invalid-name
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
