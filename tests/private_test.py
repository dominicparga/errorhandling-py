from errorhandling import do, private


@private
def some_function() -> int:
	return 24


@private
def some_function_with_args(some_arg: bool) -> int:
	return some_function(True) + int(some_arg)


def test_private():
	is_exception_triggered: bool = False
	try:
		some_function(False)
		assert False
	except Exception as e:
		is_exception_triggered = True
		assert f"{e}" == "This constructor shall be called privately only."
	assert is_exception_triggered, "This unit test is wrong."

	is_exception_triggered: bool = False
	try:
		some_function_with_args(False, some_arg=True)
		assert False
	except Exception as e:
		is_exception_triggered = True
		assert f"{e}" == "This constructor shall be called privately only."
	assert is_exception_triggered, "This unit test is wrong."


def test_ignoring_private():
	assert isinstance(do(some_function)(), int), "Using 'do' does not provide expected return value."

	assert isinstance(
		do(some_function_with_args)(some_arg=True), int
	), "Using 'do' does not provide expected return value."
