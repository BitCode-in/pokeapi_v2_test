import pytest

@pytest.mark.locations
@pytest.mark.location_endpoint
@pytest.mark.parametrize("location_id_or_name", [1, "canalave-city", "invalid_location"])
def test_location_endpoint(api_client, fixinstance, location_id_or_name, NamedAPIResource, GenerationGameIndex, Name):
	response = api_client.get(f"{pytest.BASE_URL}/location/{location_id_or_name}/")
	if location_id_or_name == "invalid_location":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		if fixinstance(data, "region", dict):
			NamedAPIResource(data["region"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)

		fixinstance(data, "game_indices", list)
		for game_indices in data['game_indices']:
			GenerationGameIndex(game_indices)
			
		fixinstance(data, "areas", list)
		for area_info in data["areas"]:
			NamedAPIResource(area_info)
		
		