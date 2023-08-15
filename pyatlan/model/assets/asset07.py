# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.
# Based on original code from https://github.com/apache/atlas (under Apache-2.0 license)


from __future__ import annotations

from typing import ClassVar

from pydantic import Field, validator

from .asset00 import Asset


class Cloud(Asset, type_name="Cloud"):
    """Description"""

    type_name: str = Field("Cloud", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Cloud":
            raise ValueError("must be Cloud")
        return v

    def __setattr__(self, name, value):
        if name in Cloud._convience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convience_properties: ClassVar[list[str]] = []


Cloud.Attributes.update_forward_refs()
