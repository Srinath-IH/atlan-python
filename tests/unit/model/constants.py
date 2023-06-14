DEFAULT = "default"
CONNECTOR_TYPE = "snowflake"
TIME_STAMP = "1686532494"
CONNECTION_NAME = "MyConnection"
DATABASE_NAME = "MyDB"
SCHEMA_NAME = "MySchema"
TABLE_NAME = "MyTable"
VIEW_NAME = "MyView"
COLUMN_NAME = "MyColumn"
CONNECTION_QUALIFIED_NAME = f"{DEFAULT}/{CONNECTOR_TYPE}/{TIME_STAMP}"
DATABASE_QUALIFIED_NAME = f"{CONNECTION_QUALIFIED_NAME}/{DATABASE_NAME}"
SCHEMA_QUALIFIED_NAME = f"{DATABASE_QUALIFIED_NAME}/{SCHEMA_NAME}"
TABLE_QUALIFIED_NAME = f"{SCHEMA_QUALIFIED_NAME}/{TABLE_NAME}"
VIEW_QUALIFIED_NAME = f"{SCHEMA_QUALIFIED_NAME}/{VIEW_NAME}"
TABLE_COLUMN_QUALIFIED_NAME = f"{TABLE_QUALIFIED_NAME}/{COLUMN_NAME}"
VIEW_COLUMN_QUALIFIED_NAME = f"{VIEW_QUALIFIED_NAME}/{COLUMN_NAME}"
