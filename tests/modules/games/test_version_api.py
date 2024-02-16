import pytest

@pytest.mark.games
@pytest.mark.version_endpoint
@pytest.mark.parametrize("version_id_or_name", ["red", "blue", "yellow", "invalid"])
def test_version_endpoint(api_client, version_id_or_name, fixinstance, Name, NamedAPIResource):
	response = api_client.get(f"https://pokeapi.co/api/v2/version/{version_id_or_name}/")
	if response.status_code == 404:
		assert version_id_or_name == "invalid"
	else:
		assert response.status_code == 200
		data = response.json()

		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		for name in data["names"]:
			Name(name)

		if fixinstance(data, "version_group", dict):
			NamedAPIResource(data["version_group"])