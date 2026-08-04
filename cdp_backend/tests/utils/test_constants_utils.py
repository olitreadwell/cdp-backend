#!/usr/bin/env python

from typing import Any, List, Set, Type

import pytest

from cdp_backend.utils.constants_utils import get_all_class_attr_values

#############################################################################


class ExampleConstants:
    PASSED = "Passed"
    FAILED = "Failed"


class MixedMembers:
    # Public constants are returned.
    ALPHA = "a"
    BETA = "b"

    # Underscore attributes are excluded.
    _PRIVATE = "hidden"

    # Methods (routines) are excluded.
    def method(self) -> None:
        pass

    @staticmethod
    def static_method() -> None:
        pass

    @classmethod
    def class_method(cls) -> None:
        pass


@pytest.mark.parametrize(
    "cls, expected",
    [
        # All public, non-callable attribute values are returned.
        (ExampleConstants, {"Passed", "Failed"}),
        # Underscore attributes and methods are excluded.
        (MixedMembers, {"a", "b"}),
    ],
)
def test_get_all_class_attr_values(cls: Type, expected: Set[Any]) -> None:
    values: List[Any] = get_all_class_attr_values(cls)
    assert set(values) == expected
