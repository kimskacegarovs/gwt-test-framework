from abc import ABC, abstractmethod
from dataclasses import dataclass


class GWTMissingDescriptionException(BaseException):
    pass


@dataclass
class GivenWhenThenDescription:
    test_title: str
    given: str
    when: str
    then: str

    def render_as_markdown(self) -> str:
        return f"""
            ### Test Scenario: {self.test_title}

            **Given**: {self.given}

            **When**: {self.when}

            **Then**: {self.then}
        """


class GivenWhenThenTestScenario(ABC):
    description: GivenWhenThenDescription

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
        try:
            description = self.description
        except AttributeError:
            raise GWTMissingDescriptionException("Description not provided for the scenario")

        if not isinstance(description, GivenWhenThenDescription):
            raise GWTMissingDescriptionException(f"Description must be of type {GivenWhenThenDescription.__name__}")

    @classmethod
    def get_subclass_descriptions(cls) -> list[GivenWhenThenDescription]:
        descriptions = []
        for subclass in cls.__subclasses__():
            try:
                descriptions.append(subclass.description)
            except AttributeError:
                pass
        return descriptions

    @classmethod
    def render_as_markdown(cls) -> str:
        return cls.description.render_as_markdown()
