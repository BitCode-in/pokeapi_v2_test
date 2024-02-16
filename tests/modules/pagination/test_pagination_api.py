import pytest

@pytest.mark.pagination
@pytest.mark.parametrize("endpoint_name", ["ability", "invalid_endpoint"])
def test_named_endpoint(api_client, endpoint_name, fixinstance, NamedAPIResource):
	response = api_client.get(f"{pytest.BASE_URL}/{endpoint_name}/")
	if endpoint_name == "invalid_endpoint":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "count", int)
		fixinstance(data, "next", str)
		fixinstance(data, "previous", str)
		fixinstance(data, "results", list)
		assert len(data["results"]) > 0
		for result in data["results"]:
			assert isinstance(result, dict)
			NamedAPIResource(result)

@pytest.mark.pagination
@pytest.mark.parametrize("limit, offset", [(10, 0), (20, 10), (5, 15)])
def test_named_endpoint_with_limit_and_offset(api_client, fixinstance, limit, offset, NamedAPIResource):
	response = api_client.get(f"{pytest.BASE_URL}/ability/?limit={limit}&offset={offset}")
	assert response.status_code == 200
	data = response.json()
	assert isinstance(data, dict)
	fixinstance(data, "count", int)
	fixinstance(data, "next", str)
	fixinstance(data, "previous", str)
	fixinstance(data, "results", list)
	assert len(data["results"]) <= limit
	for result in data["results"]:
		assert isinstance(result, dict)
		NamedAPIResource(result)