from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class GivenWhenThenDescription:
    test_title: str
    given: str
    when: str
    then: str


class GivenWhenThenTestScenario(ABC):
    description_given: str = ""
    description_when: str = ""
    description_then: str = ""

    def test(self) -> None:
        self.given()
        self.when()
        self.then()
        self.validate_descriptions()

    @abstractmethod
    def given(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} must implement the 'given' method.")

    @abstractmethod
    def when(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} must implement the 'when' method.")

    @abstractmethod
    def then(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} must implement the 'then' method.")

    def validate_descriptions(self) -> None:
        for field, value in [
            ("given", self.description_given),
            ("when", self.description_when),
            ("then", self.description_then),
        ]:
            if not value:
                raise ValueError(f"{self.__class__.__name__} is missing '{field}' description.")

    @classmethod
    def get_description(cls) -> GivenWhenThenDescription:
        return GivenWhenThenDescription(
            test_title=cls.__name__, given=cls.description_given, when=cls.description_when, then=cls.description_then
        )

    @classmethod
    def get_subclass_descriptions(cls) -> list[GivenWhenThenDescription]:
        return [sc.get_description() for sc in cls.__subclasses__()]

    @classmethod
    def render_as_markdown(cls) -> str:
        return f"""
            ### Test Scenario: {cls.__name__}

            **Given**: {cls.description_given}

            **When**: {cls.description_when}

            **Then**: {cls.description_then}
        """
