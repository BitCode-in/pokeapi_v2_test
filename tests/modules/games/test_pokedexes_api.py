import pytest

@pytest.fixture
def PokemonEntry(fixinstance, NamedAPIResource):
	def check(entry):
		assert isinstance(entry, dict)
		fixinstance(entry, "entry_number", int)
		if fixinstance(entry, "pokemon_species", dict):
			NamedAPIResource(entry['pokemon_species'])
	return check

@pytest.mark.games
@pytest.mark.pokedexes_endpoint
@pytest.mark.parametrize("pokedex_id_or_name", [1, 2, "kanto", "invalid_pokedex"])
def test_pokedex_endpoint(api_client, pokedex_id_or_name, fixinstance, NamedAPIResource, Description, PokemonEntry, Name):
	response = api_client.get(f"{pytest.BASE_URL}/pokedex/{pokedex_id_or_name}/")
	if pokedex_id_or_name == "invalid_pokedex":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "is_main_series", bool)
		
		fixinstance(data, "descriptions", list)
		for description in data["descriptions"]:
			Description(description)
		
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)
		
		fixinstance(data, "pokemon_entries", list)
		for entry in data["pokemon_entries"]:
			PokemonEntry(entry)
		
		if fixinstance(data, "region", dict):
			NamedAPIResource(data["region"])
		
		fixinstance(data, "version_groups", list)
		for version_group in data["version_groups"]:
			NamedAPIResource(version_group)