import json
from .economics import margins
from .markets import active
from .planning import next_plan


def run_workbench(action, directory, key, ledger):
    source = json.loads((directory / 'workbench.json').read_text())
    lots = active(source['catalog'], source['today'])
    if action == 'catalog':
        return lots
    value = margins(source)
    if action == 'margin':
        return value
    return next_plan(value, lots, source['budget_cents'], source['commitments'])
