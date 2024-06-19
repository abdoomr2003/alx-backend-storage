#!/usr/bin/env python3
"""
web.py

This module provides functions to fetch web pages, cache them with Redis,
and track access counts.

Dependencies:
    - requests
    - redis

Example usage:
    >>> url = "https://www.example.com"
    >>> content = get_page(url)
    >>> print(content)

Author: Your Name
Date: 2024-06-19
"""

import requests
import redis
import time
from typing import Callable

# Initialize Redis connection
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Fetches the HTML content from a URL.

    Args:
        url: The URL of the web page.

    Returns:
        str: The HTML content of the web page.

    Raises:
        requests.RequestException: If the request to the URL fails.
    """
    # Check if the content is cached in Redis
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, fetch content from URL
    response = requests.get(url)
    response.raise_for_status()
    html_content = response.text

    # Cache the content with expiration of 10 seconds
    redis_client.setex(url, 10, html_content)

    # Track access count
    redis_client.incr(f"count:{url}")

    return html_content

if __name__ == "__main__":
    # Example usage
    url = "https://www.example.com"
    print(get_page(url))
