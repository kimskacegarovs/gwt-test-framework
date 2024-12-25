# gwt-test-framework

A Python framework for declaring **Given-When-Then** tests. This library helps you organize and structure your tests based on the Given-When-Then methodology, making your tests more readable, maintainable, and descriptive.

## Features
- Declarative **Given-When-Then** test structure.
- Easy-to-use framework for defining tests with clear descriptions.
- Provides mechanisms for validation and test execution.
- Supports extension via subclassing.

## Installation

To install `gwt-test-framework`, you can use `pip`:

```bash
pip install gwt-test-framework
```

## Usage

### Basic Usage

To create a Given-When-Then test scenario, you need to create a class that inherits from `GivenWhenThenTestScenario` and implement the `given()`, `when()`, and `then()` methods.

Example:

```python
from gwt_test_framework import GivenWhenThenTestScenario

class MyTestScenario(GivenWhenThenTestScenario):
    description_given = "User is logged in"
    description_when = "User clicks on the submit button"
    description_then = "A success message is displayed"

    def given(self):
        # Setup your test environment (e.g., log in user)
        pass

    def when(self):
        # Simulate the action (e.g., click the button)
        pass

    def then(self):
        # Verify the outcome (e.g., check success message)
        pass
```

### Running the Test

Once you've defined your test scenario, you can run it with the `test()` method, which will execute the `given()`, `when()`, and `then()` methods in sequence, ensuring that the descriptions are provided.

```python
test_scenario = MyTestScenario()
test_scenario.test()  # Run the test
```

### Validation

The `test()` method will automatically check that the `given`, `when`, and `then` descriptions are defined. If any of the descriptions are missing, a `ValueError` will be raised.

### Getting Test Descriptions

You can also retrieve the description for your test scenario using the `get_description()` and `get_subclass_descriptions()` methods.

```python
# Get the description for a single test scenario
description = MyTestScenario.get_description()

# Get descriptions for all subclasses
all_descriptions = MyTestScenario.get_subclass_descriptions()
```

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
