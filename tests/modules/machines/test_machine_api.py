import pytest

@pytest.mark.machines
@pytest.mark.machine_endpoint
@pytest.mark.parametrize("machine_id", [1, 2, 3])
def test_machine_endpoint(api_client, fixinstance, machine_id, NamedAPIResource, VerboseEffect):
	response = api_client.get(f"{pytest.BASE_URL}/machine/{machine_id}/")
	assert response.status_code == 200
	data = response.json()
	assert isinstance(data, dict)
	fixinstance(data, "id", int)
	if fixinstance(data, "item", dict):
		NamedAPIResource(data["item"])
	if fixinstance(data, "move", dict):
		NamedAPIResource(data["move"])
	if fixinstance(data, "version_group", dict):
		NamedAPIResource(data["version_group"])
	