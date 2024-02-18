import pytest

@pytest.mark.abilities
@pytest.mark.characteristic_endpoint
@pytest.mark.parametrize("characteristic_id", [1, 2, 3, "invalid_characteristic"])
def test_characteristic_endpoint(api_client, fixinstance, characteristic_id, NamedAPIResource, Description):
	response = api_client.get(f"{pytest.BASE_URL}/characteristic/{characteristic_id}/")
	if characteristic_id == "invalid_characteristic":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "gene_modulo", int)
		fixinstance(data, "possible_values", list)
		for possible_value in data["possible_values"]:
			assert isinstance(possible_value, int)

		if fixinstance(data, "highest_stat", dict):
			NamedAPIResource(data["highest_stat"])

		fixinstance(data, "descriptions", list)		
		for description in data["descriptions"]:
			Description(description)