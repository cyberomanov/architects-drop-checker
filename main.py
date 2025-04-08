import sys

from loguru import logger

from tools.other.add_logger import add_logger
from tools.other.read_file import read_file
from tools.requests.common import get_proxied_session
from tools.requests.get_collection_offers_req import get_cultdrop_proof
from tools.web3.wallet import get_wallet_from_mnemonic
from user_data import config

if __name__ == "__main__":
    add_logger()
    try:
        with get_proxied_session(proxy=config.proxy) as session:
            total_cult = 0

            strings = read_file(path="user_data/mnemonic.txt")
            for string in strings:
                address = string if ' ' in string else str(
                    get_wallet_from_mnemonic(mnemonic=string, prefix="osmo").address()
                )

                cultdrop = get_cultdrop_proof(session=session, address=address)
                if cultdrop.message:
                    logger.info(f"{address}: {cultdrop.message.lower()}.")
                else:
                    total_cult += cultdrop.amount
                    logger.success(f"{address}: {round(cultdrop.amount / 10 ** 6, 2)} $CULT.")

            logger.info(f"total: {round(total_cult / 10 ** 6, 2)} $CULT.")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        logger.exception(e)
