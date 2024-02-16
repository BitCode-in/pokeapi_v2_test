import pytest

@pytest.mark.berries
@pytest.mark.berry_firmness_endpoint
@pytest.mark.parametrize("berry_firmness_id_or_name", [1, "very-soft", "invalid_berry_firmness"])
def test_berry_firmness_endpoint(api_client, berry_firmness_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/berry-firmness/{berry_firmness_id_or_name}/")
	if berry_firmness_id_or_name == "invalid_berry_firmness":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "berries", list)
		assert len(data["berries"]) > 0
		for berry_entry in data["berries"]:
			assert isinstance(berry_entry, dict)
			NamedAPIResource(berry_entry)
		fixinstance(data, "names", list)
		assert len(data["names"]) > 0
		for name_entry in data["names"]:
			assert isinstance(name_entry, dict)
			Name(name_entry)