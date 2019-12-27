def uniques_only(iter_):
    seen_hash = set()
    seen_unhash = []
    for item in iter_:
        try:
            hash(item)
            if item not in seen_hash:
                yield item
                seen_hash.add(item)
        except:
            if item not in seen_unhash:
                yield item
                seen_unhash.append(item)

