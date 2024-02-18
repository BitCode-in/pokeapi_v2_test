import pytest

@pytest.mark.locations
@pytest.mark.pal_park_area_endpoint
@pytest.mark.parametrize("pal_park_area_id_or_name", [1, "forest", "invalid_pal_park_area"])
def test_pal_park_area_endpoint(api_client, fixinstance, pal_park_area_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/pal-park-area/{pal_park_area_id_or_name}/")
	if pal_park_area_id_or_name == "invalid_pal_park_area":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)

		fixinstance(data, "pokemon_encounters", list)
		for pokemon_encounter_info in data["pokemon_encounters"]:
			fixinstance(pokemon_encounter_info, "base_score", int)
			fixinstance(pokemon_encounter_info, "rate", int)
			if fixinstance(pokemon_encounter_info, "pokemon_species", dict):
				NamedAPIResource(pokemon_encounter_info["pokemon_species"])