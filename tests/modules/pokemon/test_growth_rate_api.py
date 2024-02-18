import pytest

@pytest.mark.abilities
@pytest.mark.growth_rate_endpoint
@pytest.mark.parametrize("growth_rate_id_or_name", [1, "slow", "invalid_growth_rate"])
def test_growth_rate_endpoint(api_client, fixinstance, growth_rate_id_or_name, NamedAPIResource, Description):
	response = api_client.get(f"https://pokeapi.co/api/v2/growth-rate/{growth_rate_id_or_name}/")
	if growth_rate_id_or_name == "invalid_growth_rate":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "formula", str)
		fixinstance(data, "descriptions", list)
		for description in data['descriptions']:
			Description(description)

		fixinstance(data, "levels", list)
		for level_info in data["levels"]:
			fixinstance(level_info, "level", int)
			fixinstance(level_info, "experience", int)

		fixinstance(data, "pokemon_species", list)
		for pokemon_species_info in data["pokemon_species"]:
			NamedAPIResource(pokemon_species_info)