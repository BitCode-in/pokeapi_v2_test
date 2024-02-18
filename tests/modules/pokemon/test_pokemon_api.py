import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_endpoint
@pytest.mark.parametrize("pokemon_id_or_name", [35, "clefairy", "invalid_pokemon"])
def test_pokemon_endpoint(api_client, fixinstance, pokemon_id_or_name, NamedAPIResource, VersionGameIndex):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/")
	if pokemon_id_or_name == "invalid_pokemon":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "base_experience", int)
		fixinstance(data, "height", int)
		fixinstance(data, "is_default", bool)
		fixinstance(data, "order", int)
		fixinstance(data, "weight", int)
		
		fixinstance(data, "abilities", list)
		for ability_info in data['abilities']:
			assert isinstance(ability_info, dict)
			fixinstance(ability_info, "is_hidden", bool)
			fixinstance(ability_info, "slot", int)
			if fixinstance(ability_info, "ability", dict):
				NamedAPIResource(ability_info['ability'])

		fixinstance(data, "forms", list)
		for form_info in data['forms']:
			assert isinstance(form_info, dict)
			NamedAPIResource(form_info)
		
		fixinstance(data, "game_indices", list)
		for index_info in data['game_indices']:
			assert isinstance(index_info, dict)
			VersionGameIndex(index_info)
		
		fixinstance(data, "held_items", list)
		for item_info in data['held_items']:
			assert isinstance(item_info, dict)
			NamedAPIResource(item_info['item'])
			fixinstance(item_info, "version_details", list)
			for version_detail in item_info["version_details"]:
				assert isinstance(version_detail, dict)
				NamedAPIResource(version_detail['version'])
				fixinstance(version_detail, "rarity", int)

		fixinstance(data, "location_area_encounters", str)
		
		assert isinstance(data.get("location_area_encounters", ""), str)
		
		fixinstance(data, "moves", list)
		for move_info in data['moves']:
			assert isinstance(move_info, dict)
			NamedAPIResource(move_info['move'])
			fixinstance(move_info, "version_group_details", list)
			for version_info in move_info['version_group_details']:
				assert isinstance(version_info, dict)
				NamedAPIResource(version_info["move_learn_method"])
				NamedAPIResource(version_info["version_group"])
				fixinstance(version_info, "level_learned_at", int)

		fixinstance(data, "past_types", list)
		for past_type_info in data['past_types']:
			assert isinstance(past_type_info, dict)
			NamedAPIResource(past_type_info["generation"])
			fixinstance(past_type_info, "types", list)
			for type_info in past_type_info['types']:
				assert isinstance(type_info, dict)
				fixinstance(type_info, "slot", int)
				if fixinstance(type_info, "type", dict):
					NamedAPIResource(type_info['type'])

		if fixinstance(data, "sprites", dict):
			fixinstance(data['sprites'], "front_default", str)
			fixinstance(data['sprites'], "front_shiny", str)
			fixinstance(data['sprites'], "front_female", str)
			fixinstance(data['sprites'], "front_shiny_female", str)
			fixinstance(data['sprites'], "back_default", str)
			fixinstance(data['sprites'], "back_shiny", str)
			fixinstance(data['sprites'], "back_female", str)
			fixinstance(data['sprites'], "back_shiny_female", str)

		if fixinstance(data, "cries", dict):
			fixinstance(data['cries'], "latest", str)
			fixinstance(data['cries'], "legacy", str)

		if fixinstance(data, "species", dict):
			NamedAPIResource(data['species'])

		fixinstance(data, "stats", list)
		for stat_entry in data["stats"]:
			if fixinstance(stat_entry, "stat", dict):
				NamedAPIResource(stat_entry['stat'])
			fixinstance(stat_entry, "effort", int)
			fixinstance(stat_entry, "base_stat", int)

		fixinstance(data, "types", list)
		for type_entry in data["types"]:
			fixinstance(type_entry, "slot", int)
			if fixinstance(type_entry, "type", dict):
				NamedAPIResource(type_entry['type'])