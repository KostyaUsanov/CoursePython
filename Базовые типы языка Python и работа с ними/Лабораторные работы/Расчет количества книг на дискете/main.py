disc_size = 1.44
book_page = 100
line_in_perpage = 50
symbol_in_perline = 25
size_symbol = 4

size_all_symbols = size_symbol * symbol_in_perline * line_in_perpage * book_page
disc_size_in_kb = disc_size * 1024
size_all_symbols_in_kb = round((size_all_symbols / 1024), 2)
books_in_disc = round(disc_size_in_kb / size_all_symbols_in_kb)


# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_in_disc)
