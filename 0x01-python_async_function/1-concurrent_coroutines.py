#!/usr/bin/env python3
"""This module contains the corrutine wait_random"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay"""
    new_list: List[float] = []

    for i in range(n):
        new_list.append(await wait_random(max_delay))

    return new_list
