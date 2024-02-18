import pytest

@pytest.mark.abilities
@pytest.mark.stats_endpoint
@pytest.mark.parametrize("stat_id_or_name", [1, "attack", "invalid_stat"])
def test_stat_endpoint(api_client, fixinstance, stat_id_or_name, NamedAPIResource, APIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/stat/{stat_id_or_name}/")
	if stat_id_or_name == "invalid_stat":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "game_index", int)
		fixinstance(data, "is_battle_only", bool)

		if fixinstance(data, "affecting_moves", dict):
			affecting_moves = data["affecting_moves"]
			increase_moves = affecting_moves["increase"]
			decrease_moves = affecting_moves["decrease"]
			for move_stat_affect in increase_moves + decrease_moves:
				fixinstance(move_stat_affect, "change", int)
				NamedAPIResource(move_stat_affect["move"])

		if fixinstance(data, "affecting_natures", dict):
			affecting_natures = data["affecting_natures"]
			increase_natures = affecting_natures["increase"]
			decrease_natures = affecting_natures["decrease"]
			for nature_stat_affect in increase_natures + decrease_natures:
				NamedAPIResource(nature_stat_affect)

		
		fixinstance(data, "characteristics", list)
		for characteristic in data["characteristics"]:
			APIResource(characteristic)

		if fixinstance(data, "move_damage_class", dict):
			NamedAPIResource(data["move_damage_class"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)