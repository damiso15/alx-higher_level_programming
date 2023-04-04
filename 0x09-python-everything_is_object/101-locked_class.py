#!/usr/bin/python3


class LockedClass:
    """LockedClass prevents dynamic creation of attributes other than
    `first_name`
    """
    __slots__ = ['first_name']
