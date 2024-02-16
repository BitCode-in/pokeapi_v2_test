import pytest

@pytest.mark.moves
@pytest.mark.move_ailment_endpoint
@pytest.mark.parametrize("move_ailment_id_or_name", [1, "paralysis", "invalid_move_ailment"])
def test_move_ailment_endpoint(api_client, fixinstance, move_ailment_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/move-ailment/{move_ailment_id_or_name}/")
	if move_ailment_id_or_name == "invalid_move_ailment":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)

		fixinstance(data, "moves", list)
		for move_info in data["moves"]:
			assert isinstance(move_info, dict)
			NamedAPIResource(move_info)
			
		fixinstance(data, "names", list)
		assert len(data["names"]) > 0
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
		

