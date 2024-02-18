import pytest

@pytest.mark.encounters
@pytest.mark.encounter_methods_endpoint
@pytest.mark.parametrize("encounter_method_id_or_name", [1, "walk", "invalid_encounter_method"])
def test_encounter_methods_endpoint(api_client, fixinstance, encounter_method_id_or_name, Name):
	response = api_client.get(f"{pytest.BASE_URL}/encounter-method/{encounter_method_id_or_name}/")
	if encounter_method_id_or_name == "invalid_encounter_method":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "order", int)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)