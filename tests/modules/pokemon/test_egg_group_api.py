import pytest

@pytest.mark.abilities
@pytest.mark.egg_group_endpoint
@pytest.mark.parametrize("egg_group_id_or_name", [1, "monster", "invalid_egg_group"])
def test_egg_group_endpoint(api_client, fixinstance, egg_group_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/egg-group/{egg_group_id_or_name}/")
	if egg_group_id_or_name == "invalid_egg_group":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)

		fixinstance(data, "pokemon_species", list)		
		for pokemon_species_info in data["pokemon_species"]:
			assert isinstance(pokemon_species_info, dict)
			NamedAPIResource(pokemon_species_info)