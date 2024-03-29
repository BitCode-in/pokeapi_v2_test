import pytest

@pytest.mark.evolution
@pytest.mark.evolution_triggers_endpoint
@pytest.mark.parametrize("evolution_trigger_id_or_name", [1, "level-up", "invalid_trigger"])
def test_evolution_trigger_endpoint(api_client, evolution_trigger_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/evolution-trigger/{evolution_trigger_id_or_name}/")
	if evolution_trigger_id_or_name == "invalid_trigger":
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
		for pokemon_species_info in data["pokemon_species"]:
			NamedAPIResource(pokemon_species_info)