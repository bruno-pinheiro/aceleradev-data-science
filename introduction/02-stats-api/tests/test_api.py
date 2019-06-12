import pytest
import requests


class TestAPI:

    # unittest.mock
    # Scopes: function, class, module
    @pytest.fixture(scope="class")
    def url(self):
        return "http://localhost:5000/data"

    @pytest.fixture(scope="class")
    def data(self):
        return [1, 2, 3, 4]

    @pytest.fixture(scope="class")
    def uuid(self, url, data):
        # sent data
        response = requests.post(url, json={"data": data})
        # get an uuid
        return response.json()["uuid"]

    def test_save_data(self, uuid):
        assert uuid is not None

    def test_get_data(self, url, uuid, data):
        response = requests.get(url + f"/{uuid}")

        assert response.ok
        assert response.json()["data"] == data

    def test_calc_mean(self, url, uuid):
        response = requests.get((url + f"/{uuid}/mean"))

        assert response.ok
        assert response.json()["result"] == pytest.approx(2.5)

    def test_calc_min(self, url, uuid):
        response = requests.get((url + f"/{uuid}/min"))

        assert response.ok
        assert response.json()["result"] == pytest.approx(1)

    def test_calc_max(self, url, uuid):
        response = requests.get((url + f"/{uuid}/max"))

        assert response.ok
        assert response.json()["result"] == pytest.approx(4)

    # parametrize similar tests
    @pytest.mark.parametrize("operation, expected_result",
                             [("mean", 2.5), ("min", 1), ("max", 4)])
    def test_calc_parameterized(self, url, uuid, operation, expected_result):
        response = requests.get(url + f"/{uuid}/{operation}")

        assert response.ok
        assert response.json()["result"] == pytest.approx(expected_result)
