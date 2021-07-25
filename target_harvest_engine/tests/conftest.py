import pytest
import responses


@pytest.fixture
def sample_config():
    return {
        "api_url": "http://localhost/image_objects",
        "connection_id": "abc123"
    }


@pytest.fixture()
def mock_response():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as resp:
        resp.add(
            responses.POST,
            url="http://localhost/image_objects",
            status=200
        )
        yield resp
