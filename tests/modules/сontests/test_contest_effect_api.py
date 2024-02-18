import pytest

@pytest.mark.contests
@pytest.mark.contest_effect_endpoint
@pytest.mark.parametrize("contest_effect_id", [1, 2, -1, 'none_effect'])
def test_contest_effect_endpoint(api_client, fixinstance, contest_effect_id, Effect, FlavorText):
	response = api_client.get(f"{pytest.BASE_URL}/contest-effect/{contest_effect_id}/")
	if contest_effect_id in (-1, 'none_effect'):
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "appeal", int)
		fixinstance(data, "jam", int)
		fixinstance(data, "effect_entries", list)
		for effect_entry in data["effect_entries"]:
			Effect(effect_entry)
		fixinstance(data, "flavor_text_entries", list)
		for flavor_text_entry in data["flavor_text_entries"]:
			FlavorText(flavor_text_entry)