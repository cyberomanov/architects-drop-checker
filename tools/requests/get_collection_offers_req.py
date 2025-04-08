import requests

from datatypes.responses.get_cultdrop_proof import CultDropProofResponse
from tools.requests.common import process_request


def get_cultdrop_proof(
        session: requests.Session,
        address: str
) -> CultDropProofResponse:
    url = f"https://app.architectsnft.io/api/getCultdropProof?address={address}"
    data = process_request(session=session, url=url)
    if data:
        return CultDropProofResponse.parse_obj(data)
