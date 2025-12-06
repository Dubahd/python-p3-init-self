#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        """
        Initialize a Dog with a name and optional breed.
        If no breed is provided, defaults to "Mutt".
        """
        self.name = name
        self.breed = breed