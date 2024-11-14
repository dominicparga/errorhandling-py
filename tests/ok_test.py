from errorhandling import Result


def some_function() -> Result.Ok[int] | Result.Err[str]:
	return Result.ok(24)


def test_obj():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert isinstance(result.obj, int | str)
	assert isinstance(result.obj, int)


def test_is_ok():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert result.is_ok


def test_is_err():
	result: Result.Ok[int] | Result.Err[str] = some_function()
	assert not result.is_err
