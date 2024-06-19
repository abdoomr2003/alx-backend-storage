#!/usr/bin/env python3
"""
Module for caching and tracking web pages
"""
import requests
import redis
import time
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_and_track(method: Callable) -> Callable:
    """
    Decorator that caches the result of a function and tracks the number of
    times it's called.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that caches and tracks the result of the decorated
        function.

        Args:
            url (str): The URL to be fetched.

        Returns:
            str: The HTML content of the URL.
        """
        key = f"cache:{url}"
        count_key = f"count:{url}"

        # Check if the page is cached
        cached_page = r.get(key)
        if cached_page:
            r.incr(count_key)
            return cached_page.decode("utf-8")

        # Get the page from the URL
        page = method(url)

        # Cache the page for 10 seconds
        r.setex(key, 10, page)
        r.incr(count_key)

        return page

    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.

    Args:
        url (str): The URL to be fetched.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://google.com"
    for _ in range(5):
        start_time = time.time()
        page = get_page(url)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print(f"Access count: {r.get(f'count:{url}').decode('utf-8')}")
        print("---")
