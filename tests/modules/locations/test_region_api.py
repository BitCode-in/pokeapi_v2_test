import pytest

@pytest.mark.locations
@pytest.mark.region_endpoint
@pytest.mark.parametrize("region_id_or_name", [1, "kanto", "invalid_region"])
def test_region_endpoint(api_client, fixinstance, region_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/region/{region_id_or_name}/")
	if region_id_or_name == "invalid_region":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "locations", list)
		for location_info in data["locations"]:
			assert isinstance(location_info, dict)
			NamedAPIResource(location_info)
		if fixinstance(data, "main_generation", dict):
			NamedAPIResource(data["main_generation"])
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
		fixinstance(data, "pokedexes", list)
		for pokedex_info in data["pokedexes"]:
			assert isinstance(pokedex_info, dict)
			NamedAPIResource(pokedex_info)
		fixinstance(data, "version_groups", list)
		for version_group_info in data["version_groups"]:
			assert isinstance(version_group_info, dict)
			NamedAPIResource(version_group_info)