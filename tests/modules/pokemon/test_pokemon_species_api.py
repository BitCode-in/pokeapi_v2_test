import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_species_endpoint
@pytest.mark.parametrize("species_id_or_name", ["wormadam", "413", "invalid_species"])
def test_pokemon_species_endpoint(api_client, fixinstance, species_id_or_name, NamedAPIResource, APIResource, Name, Description, FlavorText):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon-species/{species_id_or_name}/")
	if species_id_or_name == "invalid_species":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "order", int)
		fixinstance(data, "gender_rate", int)
		fixinstance(data, "capture_rate", int)
		fixinstance(data, "base_happiness", int)
		fixinstance(data, "is_baby", bool)
		fixinstance(data, "is_legendary", bool)
		fixinstance(data, "is_mythical", bool)
		fixinstance(data, "hatch_counter", int)
		fixinstance(data, "has_gender_differences", bool)
		fixinstance(data, "forms_switchable", bool)
		if fixinstance(data, "growth_rate", dict):
			NamedAPIResource(data["growth_rate"])

		fixinstance(data, "pokedex_numbers", list)
		for pokedex_entry in data["pokedex_numbers"]:
			fixinstance(pokedex_entry, "entry_number", int)
			NamedAPIResource(pokedex_entry["pokedex"])

		fixinstance(data, "egg_groups", list)
		for egg_group in data["egg_groups"]:
			NamedAPIResource(egg_group)
			
		if fixinstance(data, "color", dict):
			NamedAPIResource(data["color"])

		if fixinstance(data, "shape", dict):
			NamedAPIResource(data["shape"])

		if fixinstance(data, "evolves_from_species", dict):
			NamedAPIResource(data["evolves_from_species"])

		if fixinstance(data, "evolution_chain", dict):
			APIResource(data["evolution_chain"])

		if fixinstance(data, "habitat", dict):
			NamedAPIResource(data["habitat"])

		if fixinstance(data, "generation", dict):
			NamedAPIResource(data["generation"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)

		fixinstance(data, "pal_park_encounters", list)
		for encounter_area in data["pal_park_encounters"]:
			fixinstance(encounter_area, "base_score", int)
			fixinstance(encounter_area, "rate", int)
			NamedAPIResource(encounter_area["area"])

		fixinstance(data, "flavor_text_entries", list)
		for flavor_text in data["flavor_text_entries"]:
			FlavorText(flavor_text)

		fixinstance(data, "form_descriptions", list)
		for description in data["form_descriptions"]:
			fixinstance(description, "description", str)

		fixinstance(data, "genera", list)
		for genus in data["genera"]:
			fixinstance(genus, "genus", str)
			NamedAPIResource(genus["language"])

		fixinstance(data, "varieties", list)
		for variety in data["varieties"]:
			fixinstance(variety, "is_default", bool)
			NamedAPIResource(variety["pokemon"])