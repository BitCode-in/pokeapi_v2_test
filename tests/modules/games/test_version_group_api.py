import pytest

@pytest.mark.games
@pytest.mark.version_group_endpoint
@pytest.mark.parametrize("version_group_id_or_name", ["red-blue", "gold-silver", "ruby-sapphire", "invalid"])
def test_version_group_endpoint(api_client, version_group_id_or_name, fixinstance, NamedAPIResource):
	response = api_client.get(f"{pytest.BASE_URL}version-group/{version_group_id_or_name}/")
	if response.status_code == 404:
		assert version_group_id_or_name == "invalid"
	else:
		assert response.status_code == 200
		data = response.json()

		assert isinstance(data, dict)

		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "order", int)

		if fixinstance(data, "generation", dict):
			NamedAPIResource(data["generation"])

		fixinstance(data, "move_learn_methods", list)
		for move_learn_method in data["move_learn_methods"]:
			NamedAPIResource(move_learn_method)

		fixinstance(data, "pokedexes", list)
		for pokedex in data["pokedexes"]:
			NamedAPIResource(pokedex)

		fixinstance(data, "regions", list)
		for region in data["regions"]:
			NamedAPIResource(region)

		fixinstance(data, "versions", list)
		for version in data["versions"]:
			NamedAPIResource(version)