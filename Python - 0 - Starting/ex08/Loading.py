from typing import Generator, Any


def ft_tqdm(lst: range) -> Generator[Any, None, None]:
    """
    Mimics the functionality of the `tqdm` progress bar.

    This function displays a progress bar in the console, showing:
        - the completion percentage,
        - the number of iterations completed,

    It uses the `yield` operator to return each item from
        the provided range one by one while updating the progress bar.

    Args:
        lst (range): A range of values over which to iterate.

    Yields:
        item: The current item in the iteration from the range.
    """
    total = len(lst)
    if total == 0:
        return
    bar_len = 40
    for i, item in enumerate(lst):
        percent_done = (i + 1) / total
        filled_bar = int(percent_done * bar_len)
        bar = '█' * filled_bar + ' ' * (bar_len - filled_bar)

        progress_info = f"{int(percent_done * 100)}%|{bar}| {i+1}/{total}"

        print(f"{progress_info}", end="\r")
        yield item
