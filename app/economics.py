from collections import Counter
from .markets import destination


def margins(source):
    returns = Counter()
    for refund in source['returns']:
        if refund['received'] <= source['today']:
            returns[refund['order']] += refund['cost']
    totals = Counter()
    for order in source['orders']:
        if order['ordered'] <= source['today']:
            market = destination(source['mapping'], order['channel'], source['today']) or 'unmapped'
            totals[market + '/' + order['lot']] += order['net_before_return'] - returns[order['id']]
    return dict(totals)
