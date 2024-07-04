def ft_tqdm(lst: range) -> None:
    length = len(lst)

    def print_progress(i):
        pourcent = round(i / length * 100)
        bar = '█' * pourcent
        bar += ' ' * (100 - pourcent)
        print(f'\r{pourcent:3d}%|{bar}| {i}/{length}', end='')

    print_progress(0)
    for i, item in enumerate(lst):
        yield item
        print_progress(i + 1)
