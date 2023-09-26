"""
Module to fetch active sons from PeerPlays
"""
import sys
from src.accounts.get_account import get_account_info
from peerplays_instance import peerplays

def get_active_sons():
    """
    Function to get active sons from PeerPlays
    """

    object_id_prefix = "1.33."
    object_id_number = 0
    results = []
    son_count = 0

    while True:
        try:
            object_id = object_id_prefix + str(object_id_number)
            obj = peerplays.rpc.get_object(object_id)
            if not obj:
                break
            if obj.get("status") == "active":
                account_info = get_account_info(obj["son_account"])
                account_name = account_info["name"]
                obj["son_account"] = account_name
                results.append(obj)
                son_count += 1
            object_id_number += 1
        except Exception as error: # pylint: disable=broad-except
            print(f"Error fetching object {object_id}: {error}", file=sys.stderr)
            break

    return {"active_sons": results, "son_count": son_count}
