import pytest

@pytest.mark.locations
@pytest.mark.location_area_endpoint
@pytest.mark.parametrize("location_area_id_or_name", [1, "canalave-city-area", "invalid_location_area"])
def test_location_area_endpoint(api_client, fixinstance, location_area_id_or_name, NamedAPIResource, Name, VersionEncounterDetail):
	response = api_client.get(f"{pytest.BASE_URL}/location-area/{location_area_id_or_name}/")
	if location_area_id_or_name == "invalid_location_area":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "game_index", int)
		fixinstance(data, "encounter_method_rates", list)
		for encounter_method_rate_info in data["encounter_method_rates"]:
			assert isinstance(encounter_method_rate_info, dict)
			NamedAPIResource(encounter_method_rate_info["encounter_method"])
			for version_detail_info in encounter_method_rate_info["version_details"]:
				assert isinstance(version_detail_info, dict)
				fixinstance(version_detail_info, "rate", int)
				NamedAPIResource(version_detail_info["version"])

		if fixinstance(data, "location", dict):
			NamedAPIResource(data["location"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)

		fixinstance(data, "pokemon_encounters", list)
		for pokemon_encounter_info in data["pokemon_encounters"]:
			assert isinstance(pokemon_encounter_info, dict)
			NamedAPIResource(pokemon_encounter_info["pokemon"])
			for version_detail_info in pokemon_encounter_info["version_details"]:
				assert isinstance(version_detail_info, dict)
				VersionEncounterDetail(version_detail_info)
		