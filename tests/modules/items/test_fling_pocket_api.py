import pytest

@pytest.mark.items
@pytest.mark.item_fling_pocket_endpoint
@pytest.mark.parametrize("item_pocket_id_or_name", [1, "misc", "invalid_pocket"])
def test_item_pocket_endpoint(api_client, item_pocket_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/item-pocket/{item_pocket_id_or_name}/")
	if item_pocket_id_or_name == "invalid_pocket":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "categories", list)
		for category in data["categories"]:
			assert isinstance(category, dict)
			NamedAPIResource(category)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)
	