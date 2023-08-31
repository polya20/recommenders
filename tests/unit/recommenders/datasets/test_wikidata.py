# Copyright (c) Recommenders contributors.
# Licensed under the MIT License.

import pytest


from recommenders.datasets.wikidata import (
    find_wikidata_id,
    query_entity_links,
    read_linked_entities,
    query_entity_description,
)


@pytest.fixture(scope="module")
def q():
    return {
        "correct": "the lord of the rings",
        "not_correct": "yXzCGhyFfWatQAPxeuRd09RqqWAMsCYRxZcxUDv",
        "entity_id": "Q15228",
    }


def test_find_wikidata_id(q):
    assert find_wikidata_id(q["correct"]) == "Q15228"
    assert find_wikidata_id(q["not_correct"]) == "entityNotFound"


@pytest.mark.skip(reason="Wikidata API is unstable")
def test_query_entity_links(q):
    resp = query_entity_links(q["entity_id"])
    assert "head" in resp
    assert "results" in resp


@pytest.mark.skip(reason="Wikidata API is unstable")
def test_read_linked_entities(q):
    resp = query_entity_links(q["entity_id"])
    related_links = read_linked_entities(resp)
    assert len(related_links) > 5


@pytest.mark.skip(reason="Wikidata API is unstable")
def test_query_entity_description(q):
    desc = query_entity_description(q["entity_id"])
    assert desc == "1954–1955 fantasy novel by J. R. R. Tolkien"


def test_search_wikidata():
    # TODO
    pass
