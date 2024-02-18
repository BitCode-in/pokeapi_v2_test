import pytest

@pytest.mark.utility
@pytest.mark.language_endpoint
@pytest.mark.parametrize("language_id_or_name", [1, "ja", "invalid_language"])
def test_language_endpoint(api_client, fixinstance, language_id_or_name, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/language/{language_id_or_name}/")
	if language_id_or_name == "invalid_language":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "official", bool)
		fixinstance(data, "iso639", str)
		fixinstance(data, "iso3166", str)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)