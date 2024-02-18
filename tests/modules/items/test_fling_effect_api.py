import pytest

@pytest.mark.items
@pytest.mark.item_fling_effect_endpoint
@pytest.mark.parametrize("item_fling_effect_id_or_name", [1, "badly-poison", "invalid_fling_effect"])
def test_item_fling_effect_endpoint(api_client, item_fling_effect_id_or_name, fixinstance, NamedAPIResource, Effect):
	response = api_client.get(f"{pytest.BASE_URL}item-fling-effect/{item_fling_effect_id_or_name}/")
	if item_fling_effect_id_or_name == "invalid_fling_effect":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		assert "id" in data and isinstance(data["id"], int)
		assert "name" in data and isinstance(data["name"], str)
		assert "effect_entries" in data and isinstance(data["effect_entries"], list)
		for effect_entry in data["effect_entries"]:
			Effect(effect_entry)
			
		fixinstance(data, "items", list)
		for item in data["items"]:
			NamedAPIResource(item)
	