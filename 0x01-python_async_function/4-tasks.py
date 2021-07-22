#!/usr/bin/env python3
"""This module contains the corrutine wait_random"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay"""
    new_list: List[float] = []

    for i in range(n):
        num: float = await task_wait_random(max_delay)
        new_list.append(num)

    return new_list
