import time


def format_time(seconds):
    """
    Converts a given time in seconds to a string formatted as "MM:SS".

    Args:
        seconds (int): The time in seconds to be formatted.

    Returns:
        A string representing the time in "MM:SS" format.
    """
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Mimics the functionality of the `tqdm` progress bar.

    This function displays a progress bar in the console, showing:
        - the completion percentage,
        - the number of iterations completed,
        - the elapsed time,
        - the estimated time of arrival (ETA)
        - the processing speed (iterations per second).

    It uses the `yield` operator to return each item from
        the provided range one by one while updating the progress bar.

    Args:
        lst (range): A range of values over which to iterate.

    Yields:
        item: The current item in the iteration from the range.
    """
    total = len(lst)
    bar_len = 79
    start_time = time.time()
    for i, item in enumerate(lst):
        percent_done = (i + 1) / total
        filled_bar = int(percent_done * bar_len)
        bar = '█' * filled_bar + '-' * (bar_len - filled_bar)

        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        eta_time = (total - i) / speed if speed > 0 else 0

        elapsed_format = format_time(elapsed_time)
        eta_format = format_time(eta_time)

        progress_info = f"{int(percent_done * 100)}%|{bar}| {i+1}/{total}"
        time_info = f"[{elapsed_format}<{eta_format}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item
