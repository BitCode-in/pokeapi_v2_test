import pytest

@pytest.mark.encounters
@pytest.mark.encounter_condition_values_endpoint
@pytest.mark.parametrize("encounter_condition_value_id_or_name", [1, "swarm-yes", "invalid_encounter_condition_value"])
def test_encounter_condition_values_endpoint(api_client, fixinstance, encounter_condition_value_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/encounter-condition-value/{encounter_condition_value_id_or_name}/")
	if encounter_condition_value_id_or_name == "invalid_encounter_condition_value":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		if fixinstance(data, "condition", dict):
			NamedAPIResource(data["condition"])
		fixinstance(data, "names", list)
		assert len(data["names"]) > 0
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)