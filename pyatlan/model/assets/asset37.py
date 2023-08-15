# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.
# Based on original code from https://github.com/apache/atlas (under Apache-2.0 license)


from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

from .asset17 import BI


class Sigma(BI):
    """Description"""

    type_name: str = Field("Sigma", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Sigma":
            raise ValueError("must be Sigma")
        return v

    def __setattr__(self, name, value):
        if name in Sigma._convience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convience_properties: ClassVar[list[str]] = [
        "sigma_workbook_qualified_name",
        "sigma_workbook_name",
        "sigma_page_qualified_name",
        "sigma_page_name",
        "sigma_data_element_qualified_name",
        "sigma_data_element_name",
    ]

    @property
    def sigma_workbook_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.sigma_workbook_qualified_name
        )

    @sigma_workbook_qualified_name.setter
    def sigma_workbook_qualified_name(
        self, sigma_workbook_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_workbook_qualified_name = sigma_workbook_qualified_name

    @property
    def sigma_workbook_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.sigma_workbook_name

    @sigma_workbook_name.setter
    def sigma_workbook_name(self, sigma_workbook_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_workbook_name = sigma_workbook_name

    @property
    def sigma_page_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.sigma_page_qualified_name
        )

    @sigma_page_qualified_name.setter
    def sigma_page_qualified_name(self, sigma_page_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_page_qualified_name = sigma_page_qualified_name

    @property
    def sigma_page_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.sigma_page_name

    @sigma_page_name.setter
    def sigma_page_name(self, sigma_page_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_page_name = sigma_page_name

    @property
    def sigma_data_element_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.sigma_data_element_qualified_name
        )

    @sigma_data_element_qualified_name.setter
    def sigma_data_element_qualified_name(
        self, sigma_data_element_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_data_element_qualified_name = (
            sigma_data_element_qualified_name
        )

    @property
    def sigma_data_element_name(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.sigma_data_element_name
        )

    @sigma_data_element_name.setter
    def sigma_data_element_name(self, sigma_data_element_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sigma_data_element_name = sigma_data_element_name

    class Attributes(BI.Attributes):
        sigma_workbook_qualified_name: Optional[str] = Field(
            None, description="", alias="sigmaWorkbookQualifiedName"
        )
        sigma_workbook_name: Optional[str] = Field(
            None, description="", alias="sigmaWorkbookName"
        )
        sigma_page_qualified_name: Optional[str] = Field(
            None, description="", alias="sigmaPageQualifiedName"
        )
        sigma_page_name: Optional[str] = Field(
            None, description="", alias="sigmaPageName"
        )
        sigma_data_element_qualified_name: Optional[str] = Field(
            None, description="", alias="sigmaDataElementQualifiedName"
        )
        sigma_data_element_name: Optional[str] = Field(
            None, description="", alias="sigmaDataElementName"
        )

    attributes: "Sigma.Attributes" = Field(
        default_factory=lambda: Sigma.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


Sigma.Attributes.update_forward_refs()
