setcommands = {'.add()', '.remove()', '.clear()', '.update()', '.difference()', '.discard()', '.intersection()', '.intersection_update()', '.pop()'}
dictcommands = {'.clear()', '.get()', '.keys()', '.values()', '.items()', '.update()'}
a = setcommands.intersection(dictcommands)
print(a)