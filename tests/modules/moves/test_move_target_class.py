import pytest

@pytest.mark.moves
@pytest.mark.move_targets_endpoint
@pytest.mark.parametrize("move_target_id_or_name", [1, "specific-move", "invalid_move_target"])
def test_move_target_endpoint(api_client, fixinstance, move_target_id_or_name, NamedAPIResource, Description, Name):
	response = api_client.get(f"{pytest.BASE_URL}/move-target/{move_target_id_or_name}/")
	if move_target_id_or_name == "invalid_move_target":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "descriptions", list)
		for description in data['descriptions']:
			Description(description)

		fixinstance(data, "moves", list)
		for move_info in data["moves"]:
			NamedAPIResource(move_info)

		fixinstance(data, "names", list)
		for names_info in data["names"]:
			Name(names_info)