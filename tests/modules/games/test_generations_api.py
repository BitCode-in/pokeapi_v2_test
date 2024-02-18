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
			NamedAPIResource(abilities)

		if fixinstance(data, "main_region", dict):
			NamedAPIResource(data["main_region"])
		fixinstance(data, "moves", list)

		for moves in data["moves"]:
			NamedAPIResource(moves)
		fixinstance(data, "names", list)
		
		for name_info in data["names"]:
			Name(name_info)

		fixinstance(data, "pokemon_species", list)
		for species in data["pokemon_species"]:
			NamedAPIResource(species)
			
		fixinstance(data, "types", list)
		for pokemon_type in data["types"]:
			NamedAPIResource(pokemon_type)

		fixinstance(data, "version_groups", list)
		for version_group in data["version_groups"]:
			NamedAPIResource(version_group)
