"""The module implementing the Client class."""

import qibo_client


class Client(qibo_client.Client):
    """Class to manage the interaction with the remote server."""

    def __init__(
        self,
        token: str,
    ):
        """
        :param token: the authentication token associated to the webapp user
        :type token: str
        """
        super().__init__(
            token=token,
            url="https://q-cloud.tii.ae",
        )
