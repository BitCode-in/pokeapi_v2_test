import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_habitats_endpoint
@pytest.mark.parametrize("habitat_id_or_name", ["cave", 3, "forest", "invalid_habitat"])
def test_pokemon_habitats_endpoint(api_client, fixinstance, habitat_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon-habitat/{habitat_id_or_name}/")
	if habitat_id_or_name == "invalid_habitat":
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