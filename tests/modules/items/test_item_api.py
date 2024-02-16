import pytest

@pytest.mark.items
@pytest.mark.item_endpoint
@pytest.mark.parametrize("item_id_or_name", ["master-ball", "ultra-ball", "great-ball", "invalid"])
def test_item_endpoint(api_client, item_id_or_name, fixinstance, NamedAPIResource, VerboseEffect, Name, VersionGroupFlavorText, GenerationGameIndex, APIResource, MachineVersionDetail):
	response = api_client.get(f"https://pokeapi.co/api/v2/item/{item_id_or_name}/")
	if response.status_code == 404:
		assert item_id_or_name == "invalid"
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "cost", int)
		fixinstance(data, "fling_power", int)
		if fixinstance(data, "fling_effect", dict):
			NamedAPIResource(data["fling_effect"])
		fixinstance(data, "attributes", list)
		for attribute in data["attributes"]:
			NamedAPIResource(attribute)
		if fixinstance(data, "category", dict):
			NamedAPIResource(data["category"])
		fixinstance(data, "effect_entries", list)
		for effect_entry in data["effect_entries"]:
			VerboseEffect(effect_entry)
		fixinstance(data, "flavor_text_entries", list)
		for flavor_text_entry in data["flavor_text_entries"]:
			VersionGroupFlavorText(flavor_text_entry)
		fixinstance(data, "game_indices", list)
		for game_index in data["game_indices"]:
			GenerationGameIndex(game_index)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)
		if fixinstance(data, "sprites", dict):
			fixinstance(data["sprites"], "default", str)
		fixinstance(data, "held_by_pokemon", list)
		for holder_pokemon in data["held_by_pokemon"]:
			fixinstance(holder_pokemon, "pokemon", dict)
			NamedAPIResource(holder_pokemon["pokemon"])
			fixinstance(holder_pokemon, "version_details", list)
			for version_detail in holder_pokemon["version_details"]:
				fixinstance(version_detail, "rarity", int)
				fixinstance(version_detail, "version", dict)
				NamedAPIResource(version_detail["version"])
		if fixinstance(data, "baby_trigger_for", dict):
			APIResource(data["baby_trigger_for"])
		fixinstance(data, "machines", list)
		for machines in data['machines']:
			MachineVersionDetail(machines)
	