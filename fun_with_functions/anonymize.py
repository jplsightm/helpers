def rename_iterator(col, prefix={0: 'wieght', 5: 'temp', 15: 'speed', 25: 'pressure'}):
    """
    :param col: iterator of column names
    :param prefix: dictionary of index: prefix_in_rename
    
    This is typically used to mask data when created test datasets.
    
    Usage:
    
    df = df.rename(columns=dict(zip(df.columns, map(map_tag_type, [c[0] for c in enumerate(df.columns)]))))
    """
    keys = sorted(prefix.keys())
    if col in keys:
        return '{}_{}'.format(prefix[col], 0)
    k = filter(lambda x: x < col, keys)[-1]
    n = col - k
    return '{}_{}'.format(prefix[k], n)
