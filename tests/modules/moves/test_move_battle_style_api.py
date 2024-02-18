import pytest

@pytest.mark.moves
@pytest.mark.move_battle_style_endpoint
@pytest.mark.parametrize("move_battle_style_id_or_name", [1, "attack", "invalid_move_battle_style"])
def test_move_battle_style_endpoint(api_client, fixinstance, move_battle_style_id_or_name, Name):
	response = api_client.get(f"{pytest.BASE_URL}/move-battle-style/{move_battle_style_id_or_name}/")
	if move_battle_style_id_or_name == "invalid_move_battle_style":
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
