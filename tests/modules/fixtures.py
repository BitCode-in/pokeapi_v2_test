import pytest
import requests
import warnings
import inspect

@pytest.fixture(scope="session")
def api_client():
	session = requests.Session()
	yield session
	session.close()

@pytest.fixture
def fixinstance():
	def check(object_dict, object_name, _type):
		assert object_name in object_dict and isinstance(object_dict[object_name], \
		(_type, type(None))), \
		f"Ошибка: {object_name} отсутствует в словаре или имеет неверный тип данных {_type}"
		
		if object_dict[object_name] is None:
			caller_frame = inspect.currentframe().f_back
			caller_module = caller_frame.f_globals['__file__']
			warnings.warn_explicit(
				f"{object_name} является None. А должен быть {_type}",
				category=UserWarning,
				filename=caller_module,
				lineno=caller_frame.f_lineno
			)
			return False
		return True
		
	return check

