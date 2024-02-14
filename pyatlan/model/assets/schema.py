# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.


from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field, validator

from pyatlan.model.enums import AtlanConnectorType
from pyatlan.model.fields.atlan_fields import NumericField, RelationField
from pyatlan.utils import init_guid, validate_required_fields

from .s_q_l import SQL


class Schema(SQL):
    """Description"""

    @classmethod
    # @validate_arguments()
    @init_guid
    def create(cls, *, name: str, database_qualified_name: str) -> Schema:
        validate_required_fields(
            ["name", "database_qualified_name"], [name, database_qualified_name]
        )
        attributes = Schema.Attributes.create(
            name=name, database_qualified_name=database_qualified_name
        )
        return cls(attributes=attributes)

    type_name: str = Field(default="Schema", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Schema":
            raise ValueError("must be Schema")
        return v

    def __setattr__(self, name, value):
        if name in Schema._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    TABLE_COUNT: ClassVar[NumericField] = NumericField("tableCount", "tableCount")
    """
    Number of tables in this schema.
    """
    VIEWS_COUNT: ClassVar[NumericField] = NumericField("viewsCount", "viewsCount")
    """
    Number of views in this schema.
    """

    SNOWFLAKE_TAGS: ClassVar[RelationField] = RelationField("snowflakeTags")
    """
    TBC
    """
    FUNCTIONS: ClassVar[RelationField] = RelationField("functions")
    """
    TBC
    """
    TABLES: ClassVar[RelationField] = RelationField("tables")
    """
    TBC
    """
    DATABASE: ClassVar[RelationField] = RelationField("database")
    """
    TBC
    """
    PROCEDURES: ClassVar[RelationField] = RelationField("procedures")
    """
    TBC
    """
    VIEWS: ClassVar[RelationField] = RelationField("views")
    """
    TBC
    """
    MATERIALISED_VIEWS: ClassVar[RelationField] = RelationField("materialisedViews")
    """
    TBC
    """
    SNOWFLAKE_DYNAMIC_TABLES: ClassVar[RelationField] = RelationField(
        "snowflakeDynamicTables"
    )
    """
    TBC
    """
    SNOWFLAKE_PIPES: ClassVar[RelationField] = RelationField("snowflakePipes")
    """
    TBC
    """
    SNOWFLAKE_STREAMS: ClassVar[RelationField] = RelationField("snowflakeStreams")
    """
    TBC
    """

    _convenience_properties: ClassVar[list[str]] = [
        "table_count",
        "views_count",
        "snowflake_tags",
        "functions",
        "tables",
        "database",
        "procedures",
        "views",
        "materialised_views",
        "snowflake_dynamic_tables",
        "snowflake_pipes",
        "snowflake_streams",
    ]

    @property
    def table_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.table_count

    @table_count.setter
    def table_count(self, table_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.table_count = table_count

    @property
    def views_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.views_count

    @views_count.setter
    def views_count(self, views_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.views_count = views_count

    @property
    def snowflake_tags(self) -> Optional[list[SnowflakeTag]]:
        return None if self.attributes is None else self.attributes.snowflake_tags

    @snowflake_tags.setter
    def snowflake_tags(self, snowflake_tags: Optional[list[SnowflakeTag]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_tags = snowflake_tags

    @property
    def functions(self) -> Optional[list[Function]]:
        return None if self.attributes is None else self.attributes.functions

    @functions.setter
    def functions(self, functions: Optional[list[Function]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.functions = functions

    @property
    def tables(self) -> Optional[list[Table]]:
        return None if self.attributes is None else self.attributes.tables

    @tables.setter
    def tables(self, tables: Optional[list[Table]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.tables = tables

    @property
    def database(self) -> Optional[Database]:
        return None if self.attributes is None else self.attributes.database

    @database.setter
    def database(self, database: Optional[Database]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.database = database

    @property
    def procedures(self) -> Optional[list[Procedure]]:
        return None if self.attributes is None else self.attributes.procedures

    @procedures.setter
    def procedures(self, procedures: Optional[list[Procedure]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.procedures = procedures

    @property
    def views(self) -> Optional[list[View]]:
        return None if self.attributes is None else self.attributes.views

    @views.setter
    def views(self, views: Optional[list[View]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.views = views

    @property
    def materialised_views(self) -> Optional[list[MaterialisedView]]:
        return None if self.attributes is None else self.attributes.materialised_views

    @materialised_views.setter
    def materialised_views(self, materialised_views: Optional[list[MaterialisedView]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.materialised_views = materialised_views

    @property
    def snowflake_dynamic_tables(self) -> Optional[list[SnowflakeDynamicTable]]:
        return (
            None
            if self.attributes is None
            else self.attributes.snowflake_dynamic_tables
        )

    @snowflake_dynamic_tables.setter
    def snowflake_dynamic_tables(
        self, snowflake_dynamic_tables: Optional[list[SnowflakeDynamicTable]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_dynamic_tables = snowflake_dynamic_tables

    @property
    def snowflake_pipes(self) -> Optional[list[SnowflakePipe]]:
        return None if self.attributes is None else self.attributes.snowflake_pipes

    @snowflake_pipes.setter
    def snowflake_pipes(self, snowflake_pipes: Optional[list[SnowflakePipe]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_pipes = snowflake_pipes

    @property
    def snowflake_streams(self) -> Optional[list[SnowflakeStream]]:
        return None if self.attributes is None else self.attributes.snowflake_streams

    @snowflake_streams.setter
    def snowflake_streams(self, snowflake_streams: Optional[list[SnowflakeStream]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_streams = snowflake_streams

    class Attributes(SQL.Attributes):
        table_count: Optional[int] = Field(default=None, description="")
        views_count: Optional[int] = Field(default=None, description="")
        snowflake_tags: Optional[list[SnowflakeTag]] = Field(
            default=None, description=""
        )  # relationship
        functions: Optional[list[Function]] = Field(
            default=None, description=""
        )  # relationship
        tables: Optional[list[Table]] = Field(
            default=None, description=""
        )  # relationship
        database: Optional[Database] = Field(
            default=None, description=""
        )  # relationship
        procedures: Optional[list[Procedure]] = Field(
            default=None, description=""
        )  # relationship
        views: Optional[list[View]] = Field(
            default=None, description=""
        )  # relationship
        materialised_views: Optional[list[MaterialisedView]] = Field(
            default=None, description=""
        )  # relationship
        snowflake_dynamic_tables: Optional[list[SnowflakeDynamicTable]] = Field(
            default=None, description=""
        )  # relationship
        snowflake_pipes: Optional[list[SnowflakePipe]] = Field(
            default=None, description=""
        )  # relationship
        snowflake_streams: Optional[list[SnowflakeStream]] = Field(
            default=None, description=""
        )  # relationship

        @classmethod
        # @validate_arguments()
        @init_guid
        def create(
            cls, *, name: str, database_qualified_name: str
        ) -> Schema.Attributes:
            if not name:
                raise ValueError("name cannot be blank")
            validate_required_fields(
                ["database_qualified_name"], [database_qualified_name]
            )
            fields = database_qualified_name.split("/")
            if len(fields) != 4:
                raise ValueError("Invalid database_qualified_name")
            try:
                connector_type = AtlanConnectorType(fields[1])  # type:ignore
            except ValueError as e:
                raise ValueError("Invalid database_qualified_name") from e
            return Schema.Attributes(
                name=name,
                database_name=fields[3],
                connection_qualified_name=f"{fields[0]}/{fields[1]}/{fields[2]}",
                database_qualified_name=database_qualified_name,
                qualified_name=f"{database_qualified_name}/{name}",
                connector_name=connector_type.value,
                database=Database.ref_by_qualified_name(database_qualified_name),
            )

    attributes: "Schema.Attributes" = Field(
        default_factory=lambda: Schema.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .database import Database  # noqa
from .function import Function  # noqa
from .materialised_view import MaterialisedView  # noqa
from .procedure import Procedure  # noqa
from .snowflake_dynamic_table import SnowflakeDynamicTable  # noqa
from .snowflake_pipe import SnowflakePipe  # noqa
from .snowflake_stream import SnowflakeStream  # noqa
from .snowflake_tag import SnowflakeTag  # noqa
from .table import Table  # noqa
from .view import View  # noqa