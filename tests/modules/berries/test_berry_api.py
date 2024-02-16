import pytest

@pytest.mark.berries
@pytest.mark.berry_endpoint
@pytest.mark.parametrize("berry_id_or_name", [1, "cheri", "invalid_berry_name"])
def test_berry_endpoint(api_client, berry_id_or_name, fixinstance, NamedAPIResource):
	response = api_client.get(f"{pytest.BASE_URL}/berry/{berry_id_or_name}/")
	if berry_id_or_name == "invalid_berry_name":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "growth_time", int)
		fixinstance(data, "max_harvest", int)
		fixinstance(data, "natural_gift_power", int)
		fixinstance(data, "size", int)
		fixinstance(data, "smoothness", int)
		fixinstance(data, "soil_dryness", int)
		fixinstance(data, "firmness", dict)
		if data.get("firmness"):
			NamedAPIResource(data["firmness"])
		fixinstance(data, "flavors", list)
		if data.get("flavors"):
			assert len(data["flavors"]) > 0
			for flavor_entry in data["flavors"]:
				assert isinstance(flavor_entry, dict)
				fixinstance(flavor_entry, "potency", int)
				fixinstance(flavor_entry, "flavor", dict)
				if flavor_entry.get("flavor"):
					NamedAPIResource(flavor_entry["flavor"])
		fixinstance(data, "item", dict)
		if data.get("item"):
			NamedAPIResource(data["item"])
		fixinstance(data, "natural_gift_type", dict)
		if data.get("natural_gift_type"):
			NamedAPIResource(data["natural_gift_type"])