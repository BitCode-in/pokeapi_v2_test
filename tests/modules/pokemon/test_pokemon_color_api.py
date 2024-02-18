import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_colors_endpoint
@pytest.mark.parametrize("color_id_or_name", [1, "black", "invalid_color"])
def test_pokemon_colors_endpoint(api_client, fixinstance, color_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon-color/{color_id_or_name}/")
	if color_id_or_name == "invalid_color":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)
		fixinstance(data, "pokemon_species", list)
		for species in data["pokemon_species"]:
			NamedAPIResource(species)