from collections import UserDict


class MaxValueDict(UserDict):
    def __init__(self, default_factory=int, value_getter=abs, **kwargs):
        super().__init__(**kwargs)
        self.default_factory = default_factory
        self.value_getter = value_getter

    def __setitem__(self, key, value):
        if key not in self.data:
            self.data[key] = self.default_factory() if self.default_factory else value

        if self.value_getter(value) > self.value_getter(self.data[key]):
            self.data[key] = value

    def __missing__(self, key):
        if not self.default_factory:
            raise KeyError(key)
        val = self.default_factory()
        self.data[key] = val
        return val

    def setdefault(self, key, default=None):
        if default is None and self.default_factory:
            default = self.default_factory()
        return super().setdefault(key, default)
