from itertools import count
from typing import Callable, Generator

import pytest

from pyatlan.client.atlan import AtlanClient
from pyatlan.model.assets import AtlasGlossary, AtlasGlossaryTerm, Connection, Database

iter_count = count(1)


@pytest.fixture(scope="module")
def client() -> AtlanClient:
    return AtlanClient()


@pytest.fixture(scope="module")
def connection(client: AtlanClient) -> Connection:
    return client.get_asset_by_guid("b3a5c49a-0c7c-4e66-8453-f4da8d9ce222", Connection)


@pytest.fixture(scope="module")
def glossary(client: AtlanClient) -> Generator[AtlasGlossary, None, None]:
    glossary = AtlasGlossary.create(name="Integration Test Glossary")
    glossary = client.upsert(glossary).assets_created(asset_type=AtlasGlossary)[0]
    yield glossary
    client.purge_entity_by_guid(guid=glossary.guid)


@pytest.fixture()
def database(
    client: AtlanClient, connection: Connection
) -> Generator[Database, None, None]:

    database = Database.create(
        name="Integration_Test_Entity_DB",
        connection_qualified_name=connection.attributes.qualified_name,
    )
    database = client.upsert(database).assets_created(Database)[0]

    yield database

    client.purge_entity_by_guid(guid=database.guid)


@pytest.fixture()
def make_term(
    client: AtlanClient, glossary
) -> Generator[Callable[[str], AtlasGlossaryTerm], None, None]:
    created_term_guids = []

    def _make_term(name: str) -> AtlasGlossaryTerm:
        term = AtlasGlossaryTerm.create(
            name=f"Integration Test Glossary Term {name}", anchor=glossary
        )
        term = client.upsert(term).assets_created(AtlasGlossaryTerm)[0]
        created_term_guids.append(term.guid)
        return term

    yield _make_term

    for guid in created_term_guids:
        client.purge_entity_by_guid(guid=guid)


def test_register_client_with_bad_parameter_raises_valueerror():
    with pytest.raises(ValueError, match="client must be an instance of AtlanClient"):
        AtlanClient.register_client("")
    assert AtlanClient.get_default_client() is None


def test_register_client():
    client = AtlanClient(base_url="http://mark.atlan.com", api_key="123")
    AtlanClient.register_client(client)
    assert AtlanClient.get_default_client() == client


def test_append_terms(
    client: AtlanClient,
    make_term: Callable[[str], AtlasGlossaryTerm],
    database: Database,
):
    term = make_term("Term1")

    assert (
        database := client.append_terms(
            guid=database.guid, asset_type=Database, terms=[term]
        )
    )
    database = client.get_asset_by_guid(guid=database.guid, asset_type=Database)
    assert len(database.terms) == 1
    assert database.terms[0].guid == term.guid
