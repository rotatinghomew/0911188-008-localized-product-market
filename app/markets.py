def destination(mapping, channel, date):
    applicable = [row for row in mapping if row['channel'] == channel and row['starts'] <= date]
    return max(applicable, key=lambda row: row['starts'])['market'] if applicable else None


def active(catalog, day):
    return {row['lot']: row['formula'] for row in catalog if row['state'] == 'active' and row['from'] <= day
            and (row['until'] is None or day < row['until'])}
