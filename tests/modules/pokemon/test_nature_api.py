import pytest

@pytest.mark.abilities
@pytest.mark.nature_endpoint
@pytest.mark.parametrize("nature_id_or_name", [2, "bold", "invalid_nature"])
def test_nature_endpoint(api_client, fixinstance, nature_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/nature/{nature_id_or_name}/")
	if nature_id_or_name == "invalid_nature":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "decreased_stat", dict)
		if "decreased_stat" in data:
			NamedAPIResource(data["decreased_stat"])

		fixinstance(data, "increased_stat", dict)
		if "increased_stat" in data:
			NamedAPIResource(data["increased_stat"])

		fixinstance(data, "hates_flavor", dict)
		if "hates_flavor" in data:
			NamedAPIResource(data["hates_flavor"])

		fixinstance(data, "likes_flavor", dict)
		if "likes_flavor" in data:
			NamedAPIResource(data["likes_flavor"])

		fixinstance(data, "pokeathlon_stat_changes", list)
		for stat_change in data["pokeathlon_stat_changes"]:
			fixinstance(stat_change, "max_change", int)
			if fixinstance(stat_change, "pokeathlon_stat", dict):
				NamedAPIResource(stat_change["pokeathlon_stat"])

		fixinstance(data, "move_battle_style_preferences", list)
		for battle_style_pref in data["move_battle_style_preferences"]:
			fixinstance(battle_style_pref, "low_hp_preference", int)
			fixinstance(battle_style_pref, "high_hp_preference", int)
			if fixinstance(battle_style_pref, "move_battle_style", dict):
				NamedAPIResource(battle_style_pref["move_battle_style"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)
		
		
		
		
		
		
		
		
		
		
		
		