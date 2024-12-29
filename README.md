# gwt-test-framework

A Python framework for declaring **Given-When-Then** tests.

This library helps you organize and structure your tests using the **Given-When-Then** methodology, making them more readable, maintainable, and descriptive. It enables you to **bind the actual code to verbose logic descriptions**, fostering a better understanding of test scenarios.

Additionally, it is fully compatible with **BDD** (Behavior-Driven Development) practices, allowing teams to write tests that reflect the business logic in a **clear, human-readable format**.
## Features
- Declarative **Given-When-Then** test structure.
- Easy-to-use framework for defining tests with clear descriptions.
- Export test scenarios as Markdown for documentation.

## Installation

To install `gwt-test-framework`, you can use `pip`:

```bash
pip install gwt-test-framework
```

## Usage

Most up-to-date examples of usage can be found in the tests directory.

### Basic Usage

To create a Given-When-Then test scenario, you need to create a class that inherits from `GivenWhenThenTestScenario` and:
- define the `description` class attribute.
- implement the `given()`, `when()`, and `then()` methods.

Example:

```python
from gwt_test_framework import GivenWhenThenTestScenario, GivenWhenThenDescription

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
```

### Running the Test

To run the test scenario, you can call the `test()` method on the test scenario class:

```python
TestValidScenario.test()
```

This will execute the `given()`, `when()`, and `then()` methods in order and run the test scenario.

Is compatible with `pytest`.

### Validation

The `test()` method includes a validation step that ensures the test scenario is correctly defined. 

The validation checks:
- if the `given()`, `when()`, and `then()` methods are implemented.
- if the `description` attribute is defined.


### Rendering Test Scenarios as Markdown

To render a test scenario as a Markdown string, you can use the `render_as_markdown()` method on your test scenario class. This method will generate a nicely formatted Markdown string that describes the `given`, `when`, and `then` parts of the scenario.

```python
TestValidScenario.render_as_markdown()
```

This will return a Markdown string in the following format:

### Example

```markdown
> ### TestValidScenario
    
> **Given:** Given value is 1

> **When:** When value is incremented

> **Then:** Then value is 2
```

> ### TestValidScenario
> 
> **Given:** Given value is 1
> 
> **When:** When value is incremented
> 
> **Then:** Then value is 2


### Rendering Test Scenarios on web page

While this library doesn't offer built-in support for rendering test scenarios on a web page, you can easily implement this functionality by:

- Using a Markdown rendering library such as `markdown2` or `mistune`.
- Employing an HTML templating engine like `Jinja2` or `FastHTML` to render the descriptions.

#### Example using `FastHTML`:
![Project Screenshot](gwt_test_framework/assets/web_page_render_example.jpg)


## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request. Make sure your code passes all tests and includes adequate documentation.

### Steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request against the `main` branch of the original repository.

## License

This project is licensed under the Apache License 2.0 License - see the [LICENSE](LICENSE) file for details.
