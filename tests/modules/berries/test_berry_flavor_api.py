import pytest

@pytest.mark.berries
@pytest.mark.berry_flavor_endpoint
@pytest.mark.parametrize("flavor_id_or_name", ["spicy", "sweet", "invalid_flavor"])
def test_berry_flavor_endpoint(api_client, flavor_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/berry-flavor/{flavor_id_or_name}/")
	if flavor_id_or_name == "invalid_flavor":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "berries", list)
		for berry_map in data["berries"]:
			fixinstance(berry_map, "potency", int)
			if fixinstance(berry_map, "berry", dict):
				NamedAPIResource(berry_map["berry"])
		if fixinstance(data, "contest_type", dict):
			NamedAPIResource(data["contest_type"])
		fixinstance(data, "names", list)
		for name_entry in data["names"]:
			Name(name_entry)