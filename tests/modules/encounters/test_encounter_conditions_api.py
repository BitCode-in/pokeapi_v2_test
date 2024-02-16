import pytest

@pytest.mark.encounters
@pytest.mark.encounter_conditions_endpoint
@pytest.mark.parametrize("encounter_condition_id_or_name", [1, "swarm", "invalid_encounter_condition"])
def test_encounter_conditions_endpoint(api_client, fixinstance, encounter_condition_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/encounter-condition/{encounter_condition_id_or_name}/")
	if encounter_condition_id_or_name == "invalid_encounter_condition":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		assert len(data["names"]) > 0
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
		fixinstance(data, "values", list)
		assert len(data["values"]) > 0
		for value_entry in data["values"]:
			assert isinstance(value_entry, dict)
			NamedAPIResource(value_entry)