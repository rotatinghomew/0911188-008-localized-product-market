def next_plan(margins, active, limit, books):
    committed = [row for row in books if row['state'] == 'booked']
    available = limit - sum(row['cents'] for row in committed)
    if available < 0:
        raise ValueError('已承诺预算超过预算上限')
    candidates = [key for key, value in margins.items() if key.split('/')[1] in active and value > 0]
    winner = min(candidates, key=lambda key: (-margins[key], key)) if candidates else None
    return {'committed': [row['id'] for row in committed], 'available': available, 'candidate': winner}
