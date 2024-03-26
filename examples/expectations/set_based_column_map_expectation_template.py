"""
This is a template for creating custom SetBasedColumnMapExpectations.
For detailed instructions on how to use it, please see:
    https://docs.greatexpectations.io/docs/guides/expectations/creating_custom_expectations/how_to_create_custom_set_based_column_map_expectations
"""

from great_expectations.expectations.set_based_column_map_expectation import (
    SetBasedColumnMapExpectation,
)


# This class defines the Expectation itself
class ExpectColumnValuesToBeInSomeSet(SetBasedColumnMapExpectation):
    """TODO: Add a docstring here"""

    # These values will be used to configure the metric created by your expectation
    set_ = []

    set_camel_name = "SetName"
    set_semantic_name = None

    # These examples will be shown in the public gallery.
    # They will also be executed as unit tests for your Expectation.
    examples = []

    # Here your set is used to create a custom metric for this expectation
    map_metric = SetBasedColumnMapExpectation.register_metric(
        set_camel_name=set_camel_name,
        set_=set_,
    )

    # This object contains metadata for display in the public Gallery
    library_metadata = {
        "tags": ["set-based"],  # Tags for this Expectation in the Gallery
        "contributors": [  # Github handles for all contributors to this Expectation.
            "@your_name_here",  # Don't forget to add your github handle here!
        ],
    }


if __name__ == "__main__":
    ExpectColumnValuesToBeInSomeSet().print_diagnostic_checklist()
