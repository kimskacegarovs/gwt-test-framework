from gwt_test_framework.base import (
    GivenWhenThenTestScenario,
    GivenWhenThenDescriptionException,
    GivenWhenThenDescription,
)
import pytest


class TestValidScenario(GivenWhenThenTestScenario):
    description = GivenWhenThenDescription(
        test_title="TestValidScenario",
        given="Given value is 1",
        when="When value is incremented",
        then="Then value is 2",
    )

    def given(self):
        self.given_value = 1

    def when(self):
        self.given_value += 1

    def then(self):
        assert self.given_value == 2


class TestFailingScenario(GivenWhenThenTestScenario):
    description = GivenWhenThenDescription(
        test_title="TestFailingScenario",
        given="Given value is 1",
        when="When value is incremented",
        then="Then value is 3",
    )

    def given(self):
        self.given_value = 1

    def when(self):
        self.given_value += 1

    def then(self):
        assert self.given_value == 3

    def test(self):
        with pytest.raises(AssertionError):
            super().test()


class TestMissingDescriptions(GivenWhenThenTestScenario):
    def given(self):
        pass

    def when(self):
        pass

    def then(self):
        pass

    def test(self):
        with pytest.raises(GivenWhenThenDescriptionException):
            super().test()


class TestInvalidDescriptionType(GivenWhenThenTestScenario):
    description = "Invalid description type"

    def given(self):
        pass

    def when(self):
        pass

    def then(self):
        pass

    def test(self):
        with pytest.raises(GivenWhenThenDescriptionException):
            super().test()


class TestDescriptionExtraction:
    def test_get_description(self):
        description = TestValidScenario.description
        assert isinstance(description, GivenWhenThenDescription)
        assert description.test_title == "TestValidScenario"
        assert description.given == "Given value is 1"
        assert description.when == "When value is incremented"
        assert description.then == "Then value is 2"

    def test_get_subclass_descriptions(self):
        descriptions = GivenWhenThenTestScenario.get_subclass_descriptions()
        assert len(descriptions) == 2
        assert all(isinstance(desc, GivenWhenThenDescription) for desc in descriptions)
        assert descriptions[0].test_title == "TestValidScenario"
        assert descriptions[1].test_title == "TestFailingScenario"

    def test_render_as_markdown(self):
        markdown = TestValidScenario.render_as_markdown()
        assert isinstance(markdown, str)
        assert (
            markdown
            == """
            ### Test Scenario: TestValidScenario

            **Given**: Given value is 1

            **When**: When value is incremented

            **Then**: Then value is 2
        """
        )
