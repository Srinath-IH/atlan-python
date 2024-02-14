# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.


from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field, validator

from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .micro_strategy import MicroStrategy


class MicroStrategyReport(MicroStrategy):
    """Description"""

    type_name: str = Field(default="MicroStrategyReport", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "MicroStrategyReport":
            raise ValueError("must be MicroStrategyReport")
        return v

    def __setattr__(self, name, value):
        if name in MicroStrategyReport._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    MICRO_STRATEGY_REPORT_TYPE: ClassVar[KeywordField] = KeywordField(
        "microStrategyReportType", "microStrategyReportType"
    )
    """
    Type of report, for example: Grid or Chart.
    """

    MICRO_STRATEGY_METRICS: ClassVar[RelationField] = RelationField(
        "microStrategyMetrics"
    )
    """
    TBC
    """
    MICRO_STRATEGY_PROJECT: ClassVar[RelationField] = RelationField(
        "microStrategyProject"
    )
    """
    TBC
    """
    MICRO_STRATEGY_ATTRIBUTES: ClassVar[RelationField] = RelationField(
        "microStrategyAttributes"
    )
    """
    TBC
    """

    _convenience_properties: ClassVar[list[str]] = [
        "micro_strategy_report_type",
        "micro_strategy_metrics",
        "micro_strategy_project",
        "micro_strategy_attributes",
    ]

    @property
    def micro_strategy_report_type(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.micro_strategy_report_type
        )

    @micro_strategy_report_type.setter
    def micro_strategy_report_type(self, micro_strategy_report_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.micro_strategy_report_type = micro_strategy_report_type

    @property
    def micro_strategy_metrics(self) -> Optional[list[MicroStrategyMetric]]:
        return (
            None if self.attributes is None else self.attributes.micro_strategy_metrics
        )

    @micro_strategy_metrics.setter
    def micro_strategy_metrics(
        self, micro_strategy_metrics: Optional[list[MicroStrategyMetric]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.micro_strategy_metrics = micro_strategy_metrics

    @property
    def micro_strategy_project(self) -> Optional[MicroStrategyProject]:
        return (
            None if self.attributes is None else self.attributes.micro_strategy_project
        )

    @micro_strategy_project.setter
    def micro_strategy_project(
        self, micro_strategy_project: Optional[MicroStrategyProject]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.micro_strategy_project = micro_strategy_project

    @property
    def micro_strategy_attributes(self) -> Optional[list[MicroStrategyAttribute]]:
        return (
            None
            if self.attributes is None
            else self.attributes.micro_strategy_attributes
        )

    @micro_strategy_attributes.setter
    def micro_strategy_attributes(
        self, micro_strategy_attributes: Optional[list[MicroStrategyAttribute]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.micro_strategy_attributes = micro_strategy_attributes

    class Attributes(MicroStrategy.Attributes):
        micro_strategy_report_type: Optional[str] = Field(default=None, description="")
        micro_strategy_metrics: Optional[list[MicroStrategyMetric]] = Field(
            default=None, description=""
        )  # relationship
        micro_strategy_project: Optional[MicroStrategyProject] = Field(
            default=None, description=""
        )  # relationship
        micro_strategy_attributes: Optional[list[MicroStrategyAttribute]] = Field(
            default=None, description=""
        )  # relationship

    attributes: "MicroStrategyReport.Attributes" = Field(
        default_factory=lambda: MicroStrategyReport.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .micro_strategy_attribute import MicroStrategyAttribute  # noqa: E402
from .micro_strategy_metric import MicroStrategyMetric  # noqa: E402
from .micro_strategy_project import MicroStrategyProject  # noqa: E402
