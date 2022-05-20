def q_hof_seq(num_list):
    seq_list = num_list[:]
    if seq_list == [1, 2]:
        raise StopIteration
    for elem in num_list:
        yield elem
    while True:
        n = len(seq_list)
        q = seq_list[n - seq_list[n - 1]] + seq_list[n - seq_list[n - 2]]
        yield q
        seq_list.append(q)


for i in q_hof_seq([1, 1]):
    print(i)
