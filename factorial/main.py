def factorial(x, progress_callback=None):
    if x < 0:
        raise ValueError("x must be > 0")

    result = 1
    for i in range(2, x + 1):
        progress = i / x * 100.0
        if progress_callback is not None:
            progress_callback(progress)

        result *= i

    if progress_callback is not None:
        progress_callback(100.0)

    return result
