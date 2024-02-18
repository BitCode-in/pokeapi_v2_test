import pytest

@pytest.mark.abilities
@pytest.mark.ability_endpoint
@pytest.mark.parametrize("ability_id_or_name", [1, "stench", "invalid_ability"])
def test_ability_endpoint(api_client, fixinstance, ability_id_or_name, NamedAPIResource, VerboseEffect, Name, Effect):
	response = api_client.get(f"https://pokeapi.co/api/v2/ability/{ability_id_or_name}/")
	if ability_id_or_name == "invalid_ability":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "is_main_series", bool)
		if fixinstance(data, "generation", dict):
			NamedAPIResource(data["generation"])

		fixinstance(data, "names", list)
		for names_info in data["names"]:
			assert isinstance(names_info, dict)
			Name(names_info)

		fixinstance(data, "effect_entries", list)
		for effect_entries in data["effect_entries"]:
			assert isinstance(effect_entries, dict)
			VerboseEffect(effect_entries)

		fixinstance(data, "effect_changes", list)
		for effect_change in data["effect_changes"]:
			assert isinstance(effect_change, dict)
			NamedAPIResource(effect_change["version_group"])
			for effect_entry in effect_change["effect_entries"]:
				assert isinstance(effect_entry, dict)
				Effect(effect_entry)

		fixinstance(data, "flavor_text_entries", list)
		for flavor_text_entries in data["flavor_text_entries"]:
			assert isinstance(flavor_text_entries, dict)
			fixinstance(flavor_text_entries, "flavor_text", str)
			if fixinstance(flavor_text_entries, "language", dict):
				NamedAPIResource(flavor_text_entries["language"])
			if fixinstance(flavor_text_entries, "version_group", dict):
				NamedAPIResource(flavor_text_entries["version_group"])

		fixinstance(data, "pokemon", list)
		for pokemon_entry in data["pokemon"]:
			assert isinstance(pokemon_entry, dict)
			fixinstance(pokemon_entry, "is_hidden", bool)
			fixinstance(pokemon_entry, "slot", int)
			NamedAPIResource(pokemon_entry["pokemon"])