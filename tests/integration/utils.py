import time

from pyatlan.client.atlan import AtlanClient
from pyatlan.errors import AtlanError, ErrorCode, NotFoundError
from pyatlan.model.assets import Asset
from pyatlan.model.enums import EntityStatus


def retrieve_and_check_assets(
    client: AtlanClient, to_check: list[Asset], retry_count: int
):
    """
    Retrieve and check the status of a list of assets and retry if needed.
    """
    leftovers = []
    for one in to_check:
        try:
            candidate = client.asset.get_by_guid(one.guid, asset_type=type(one))
            if candidate and candidate.status == EntityStatus.ACTIVE:
                leftovers.append(candidate)
        except NotFoundError:
            # If it is not found, it was successfully deleted (purged), so we
            # do not need to look for it any further
            print("Asset no longer exists.")
        except AtlanError:
            leftovers.append(one)
    if leftovers:
        if retry_count == 20:
            raise ErrorCode.RETRY_OVERRUN.exception_with_parameters()
        time.sleep(2)
        retrieve_and_check_assets(client, leftovers, retry_count + 1)
