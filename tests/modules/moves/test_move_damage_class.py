import pytest

@pytest.mark.moves
@pytest.mark.move_damage_class_endpoint
@pytest.mark.parametrize("move_damage_class_id_or_name", [1, "status", "invalid_move_damage_class"])
def test_move_damage_class_endpoint(api_client, fixinstance, move_damage_class_id_or_name, NamedAPIResource, Description, Name):
	response = api_client.get(f"{pytest.BASE_URL}/move-damage-class/{move_damage_class_id_or_name}/")
	if move_damage_class_id_or_name == "invalid_move_damage_class":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "descriptions", list)
		for description in data['descriptions']:
			assert isinstance(description, dict)
			Description(description)

		fixinstance(data, "moves", list)
		for move_info in data["moves"]:
			assert isinstance(move_info, dict)
			NamedAPIResource(move_info)

		fixinstance(data, "names", list)
		for names_info in data["names"]:
			assert isinstance(names_info, dict)
			Name(names_info)