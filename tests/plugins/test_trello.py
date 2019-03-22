# coding: utf-8
# Test Board: https://trello.com/b/YcOfywBd/did-testing

""" Tests for the Trello plugin """



import pytest
import did.cli
import did.base
import did.plugins.trello as trello

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Constants
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

INTERVAL = "--since 2018-12-19 --until 2018-12-19"

CONFIG = """
[general]
email = "Did Tester" <the.did.tester@gmail.com>
[trello]
type = trello
user = didtester
"""


def stats_for(stats_type):
    for stats in did.cli.main(INTERVAL)[0][0].stats[0].stats:
        if type(stats) == stats_type:
            return stats.stats
    return []


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Tests
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_trello_cards_created():
    """ Created cards """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCardsCreated)
    print(stats)
    assert any([
        stat == "CreatedCard" for stat in stats])


def test_trello_cards_updated():
    """ Updated cards """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCardsUpdated)
    print(stats)
    assert any([
        stat == "UpdatedCard" for stat in stats])


def test_trello_cards_closed():
    """ Closed cards """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCardsClosed)
    print(stats)
    assert any([
        stat == "ClosedCard: closed" for stat in stats])


def test_trello_cards_commented():
    """ Commented cards """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCardsCommented)
    print(stats)
    assert any([
        stat == "CommentedCard" for stat in stats])


def test_trello_cards_moved():
    """ Moved cards """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCardsMoved)
    print(stats)
    assert any([
        stat == "[MovedCard] moved from [new] to [active]" for stat in stats])


def test_trello_checklists_checkitem():
    """ Completed Checkitems in checklists """
    did.base.Config(CONFIG)
    stats = stats_for(trello.TrelloCheckItem)
    print(stats)
    assert any([
        stat == "ChecklistCard: CheckItem" for stat in stats])


def test_trello_missing_username():
    """ Missing username """
    did.base.Config("[trello]\ntype = trello")
    with pytest.raises(did.base.ReportError):
        did.cli.main(INTERVAL)
