# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Parse the coins."""

import re
from typing import List

from sdk.cosmpy.osmosis_protobuf.cosmos.base.v1beta1.coin_pb2 import Coin


def parse_coins(value: str) -> List[Coin]:
    """Parse the coins.

    :param value: coins
    :raises RuntimeError: If unable to parse the value
    :return: coins
    """
    coins = []

    parts = re.split(r",\s*", value)
    for part in parts:
        part = part.strip()
        if part == "":
            continue

        if 'ibc' not in value:
            match = re.match(r"(\d+)(\w+)", part)
            if match is None:
                raise RuntimeError(f"Unable to parse value {part}")

            amount, denom = match.groups()
        else:
            match = re.match(r'(\d+)(.*)', part)

            if match:
                amount = match.group(1)
                denom = match.group(2)

        coins.append(Coin(amount=amount, denom=denom))

    return coins
