import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_shapes_endpoint
@pytest.mark.parametrize("shape_id_or_name", ["ball", "2", "invalid_shape"])
def test_pokemon_shapes_endpoint(api_client, fixinstance, shape_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon-shape/{shape_id_or_name}/")
	if shape_id_or_name == "invalid_shape":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "awesome_names", list)
		for awesome_name_info in data["awesome_names"]:
			assert isinstance(awesome_name_info, dict)
			fixinstance(awesome_name_info, "awesome_name", str)
			NamedAPIResource(awesome_name_info["language"])
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
		fixinstance(data, "pokemon_species", list)
		for species in data["pokemon_species"]:
			NamedAPIResource(species)