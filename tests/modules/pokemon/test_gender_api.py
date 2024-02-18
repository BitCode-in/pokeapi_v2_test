import pytest

@pytest.mark.abilities
@pytest.mark.gender_endpoint
@pytest.mark.parametrize("gender_id_or_name", [1, "female", "invalid_gender"])
def test_gender_endpoint(api_client, fixinstance, gender_id_or_name, NamedAPIResource):
	response = api_client.get(f"https://pokeapi.co/api/v2/gender/{gender_id_or_name}/")
	if gender_id_or_name == "invalid_gender":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "pokemon_species_details", list)
		for species_detail in data["pokemon_species_details"]:
			fixinstance(species_detail, "rate", int)
			NamedAPIResource(species_detail["pokemon_species"])

		fixinstance(data, "required_for_evolution", list)
		for required_species in data["required_for_evolution"]:
			NamedAPIResource(required_species)