import pytest

@pytest.mark.moves
@pytest.mark.move_learn_method_endpoint
@pytest.mark.parametrize("move_learn_method_id_or_name", [1, "level-up", "invalid_move_learn_method"])
def test_move_learn_method_endpoint(api_client, fixinstance, move_learn_method_id_or_name, NamedAPIResource, Description, Name):
	response = api_client.get(f"{pytest.BASE_URL}/move-learn-method/{move_learn_method_id_or_name}/")
	if move_learn_method_id_or_name == "invalid_move_learn_method":
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

		fixinstance(data, "names", list)
		for names_info in data["names"]:
			Name(names_info)

		fixinstance(data, "version_groups", list)
		for move_info in data["version_groups"]:
			NamedAPIResource(move_info)