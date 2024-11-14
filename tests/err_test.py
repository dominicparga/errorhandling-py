from errorhandling import Result


def some_function() -> Result.Ok[int] | Result.Err[str]:
	return Result.err("Oh no this is an error!")


def test_obj():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert isinstance(result.obj, int | str)
	assert isinstance(result.obj, str)


def test_is_ok():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert not result.is_ok


def test_is_err():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert result.is_err
