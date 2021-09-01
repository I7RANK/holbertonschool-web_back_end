#!/usr/bin/env python3
"""This module contains the Cache class
"""

import redis
import uuid
from typing import Union, Callable


class Cache():
    """Cache class
    """
    def __init__(self):
        """Cache constructor
        """
        self._redis = redis.Redis()

        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """saves data in redis using an uniq uuid
        """
        new_key = str(uuid.uuid4())

        self._redis.set(new_key, data)

        return new_key

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        """gets data from redis and calls fn if is not None
            to format the data
        """
        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self):
        """automatically parametrize Cache.get
            with the correct conversion function.
        """

    def get_int(self):
        """automatically parametrize Cache.get
            with the correct conversion function.
        """
