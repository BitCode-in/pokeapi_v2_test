import pytest

@pytest.mark.items
@pytest.mark.item_attribute_endpoint
@pytest.mark.parametrize("item_attribute_id_or_name", [1, "countable", "invalid_attribute"])
def test_item_attribute_endpoint(api_client, item_attribute_id_or_name, fixinstance, NamedAPIResource, Description, Name):
	response = api_client.get(f"{pytest.BASE_URL}item-attribute/{item_attribute_id_or_name}/")
	if item_attribute_id_or_name == "invalid_attribute":
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

		fixinstance(data, "descriptions", list)
		for description_info in data["descriptions"]:
			Description(description_info)
		
	