import pytest

@pytest.mark.moves
@pytest.mark.move_category_endpoint
@pytest.mark.parametrize("move_category_id_or_name", [1, "ailment", "invalid_move_category"])
def test_move_category_endpoint(api_client, fixinstance, move_category_id_or_name, NamedAPIResource, Description):
	response = api_client.get(f"{pytest.BASE_URL}/move-category/{move_category_id_or_name}/")
	if move_category_id_or_name == "invalid_move_category":
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