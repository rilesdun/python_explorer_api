import json
from peerplays import PeerPlays
from src.accounts.getAccount import get_account_info

def get_active_sons():
    from peerplays import PeerPlays

    peerplays = PeerPlays("wss://ca.peerplays.info")

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
        except Exception as e:
            print(f"Error fetching object {object_id}: {e}", file=sys.stderr)
            break

    return {"active_sons": results, "son_count": son_count}  # Return results and son_count