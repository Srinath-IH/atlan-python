# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.
# Based on original code from https://github.com/apache/atlas (under Apache-2.0 license)


from __future__ import annotations

from typing import ClassVar

from pydantic import Field, validator

from .asset17 import BI


class Looker(BI):
    """Description"""

    type_name: str = Field("Looker", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Looker":
            raise ValueError("must be Looker")
        return v

    def __setattr__(self, name, value):
        if name in Looker._convience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convience_properties: ClassVar[list[str]] = []


Looker.Attributes.update_forward_refs()
