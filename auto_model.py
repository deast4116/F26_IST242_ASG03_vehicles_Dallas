class AutoModel:
    def __init__(self, name: str, in_production: bool, years: list[int]) -> None:
        if not years:
            raise ValueError("years list needs at least one year")

        self._name = name
        self._in_production = in_production
        self._years = list(years)

    @property
    def name(self) -> str:
        return self._name

    @property
    def in_production(self) -> bool:
        return self._in_production

    @property
    def years(self) -> list[int]:
        return list(self._years)

    @property
    def first_year(self) -> int:
        return self._years[0]

    def __str__(self) -> str:
        return (
            f"{self._name} in production = {self._in_production},  "
            f"release year: {self.first_year}"
        )
    