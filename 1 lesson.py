def count_string(string):
    resoult = {}
    for symbol in string:
        resoult[symbol] = resoult.get(symbol, 0) + 1
    for s in resoult:
        print(s, resoult[s])

count_string('aaaaag')
