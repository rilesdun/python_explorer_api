"""
This module is used to initiate the peerplays instance
"""
from peerplays import PeerPlays
from config import api_url

peerplays = PeerPlays(api_url)
