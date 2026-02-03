from tii_client.tii_client import Client as TiiClient


class TestTiiClient:
    def test_init(self):
        client = TiiClient(token="test")
        assert client.token == "test"
        assert client.base_url == "https://tii.qibo.science"
