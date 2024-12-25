from dataclasses import dataclass


@dataclass
class GivenWhenThenDescription:
    test_title: str
    given: str
    when: str
    then: str
