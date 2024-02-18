import pytest

@pytest.mark.contests
@pytest.mark.contest_type_endpoint
@pytest.mark.parametrize("contest_type_id_or_name", [1, "cool", "invalid_contest_type"])
def test_contest_type_endpoint(api_client, contest_type_id_or_name, fixinstance, NamedAPIResource, Name):
	response = api_client.get(f"{pytest.BASE_URL}/contest-type/{contest_type_id_or_name}/")
	if contest_type_id_or_name == "invalid_contest_type":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		if fixinstance(data, "berry_flavor", dict):
			NamedAPIResource(data["berry_flavor"])
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)