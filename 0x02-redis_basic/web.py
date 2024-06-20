#!/usr/bin/env python3
"""
This module provides a function to fetch and cache HTML content of a URL.
It also tracks the number of times a particular URL was accessed.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_with_count(func: Callable) -> Callable:
    """
    Decorator to cache the result of a function and track access count.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache result and track access count.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content of the URL.
        """
        # Track the number of times the URL is accessed
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Check if the page content is already cached
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch the HTML content from the URL
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text

            # Cache the HTML content with an expiration time of 10 seconds
            redis_client.setex(url, 10, html_content)

            return html_content
        except requests.RequestException as e:
            return f"An error occurred: {e}"

    return wrapper

# Apply the decorator to the get_page function
@cache_with_count
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches it for 10 seconds.
    Tracks the number of times the URL was accessed.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    return url  # Placeholder return; actual fetching is handled by the decorator

if __name__ == "__main__":
    test_url = 'http://slowwly.robertomurray.co.uk/delay/5000/url/https://slowwly.robertomurray.co.uk'

    print("Fetching URL for the first time:")
    print(get_page(test_url))

    print("Fetching URL for the second time (should be cached):")
    print(get_page(test_url))
