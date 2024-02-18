import pytest

@pytest.mark.items
@pytest.mark.item_category_endpoint
@pytest.mark.parametrize("item_category_id_or_name", [1, "stat-boosts", "invalid_category"])
def test_item_category_endpoint(api_client, item_category_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}item-category/{item_category_id_or_name}/")
	if item_category_id_or_name == "invalid_category":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "items", list)
		for item in data["items"]:
			NamedAPIResource(item)

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)
			
		if fixinstance(data, "pocket", dict):
			NamedAPIResource(data["pocket"])
		
	