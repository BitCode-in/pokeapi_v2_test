import pytest

@pytest.mark.games
@pytest.mark.generations_endpoint
@pytest.mark.parametrize("generation_id_or_name", [1, "generation-i", "invalid_generation"])
def test_generation_endpoint(api_client, fixinstance, generation_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/generation/{generation_id_or_name}/")
	if generation_id_or_name == "invalid_generation":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "abilities", list)
		for abilities in data["abilities"]:
			assert isinstance(abilities, dict)
			NamedAPIResource(abilities)
		if fixinstance(data, "main_region", dict):
			NamedAPIResource(data["main_region"])
		fixinstance(data, "moves", list)
		for moves in data["moves"]:
			assert isinstance(moves, dict)
			NamedAPIResource(moves)
		fixinstance(data, "names", list)
		assert len(data["names"]) > 0
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
		fixinstance(data, "pokemon_species", list)
		for species in data["pokemon_species"]:
			assert isinstance(species, dict)
			NamedAPIResource(species)
		fixinstance(data, "types", list)
		for pokemon_type in data["types"]:
			assert isinstance(pokemon_type, dict)
			NamedAPIResource(pokemon_type)
		fixinstance(data, "version_groups", list)
		for version_group in data["version_groups"]:
			assert isinstance(version_group, dict)
			NamedAPIResource(version_group)
