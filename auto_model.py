class AutoModel:
    """Represents an automodel class..."""



    @property
    def name(self) -> str:
        return self._name

    @property
    def in_production(self) -> bool:
        return self._in_production

    @property
    def years(self) -> list[int]:
        return self._years

    @property
    def __str__(self) -> str:
        return self._name
    