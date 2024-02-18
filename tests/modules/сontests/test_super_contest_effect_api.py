import pytest

@pytest.mark.contests
@pytest.mark.super_contest_effect_endpoint
@pytest.mark.parametrize("super_contest_effect_id", [1, 2, -1, 'none_effect'])
def test_super_contest_effect_endpoint(api_client, super_contest_effect_id, fixinstance, NamedAPIResource, FlavorText):
	response = api_client.get(f"{pytest.BASE_URL}/super-contest-effect/{super_contest_effect_id}/")
	if super_contest_effect_id in (-1, 'none_effect'):
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "appeal", int)
		fixinstance(data, "flavor_text_entries", list)
		for flavor_text_entry in data["flavor_text_entries"]:
			FlavorText(flavor_text_entry)
		fixinstance(data, "moves", list)
		for move in data["moves"]:
			NamedAPIResource(move)