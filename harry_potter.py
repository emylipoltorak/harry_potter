discount_structure = {1:0, 2:0.95, 3:0.9, 4:0.8, 5:0.75}

class Book:
    '''
    A book, in this case a Harry Potter Book. Books are created with an id and a price.
    '''
    def __init__(self, book_id, price=8):
        self.book_id = book_id
        self.price = price

    def __repr__(self):
        return str(self.book_id)

def calculate_price(grouped_cart, discounts):
    '''
    Takes in a list of lists. Each sub-list contains a distinct grouping of books.
    '''
    cart_total = 0
    for group in grouped_cart:
        cart_total += sum([book.price for book in group]) * discount_structure[len(group)]
    return cart_total

def best_set_size(discounts):
    '''
    This tries to find the set size we should aim for.
    '''
    discount_comparison = {}
    for key in discounts.keys():
        if discounts[key] == 0:
            discount_comparison[key] = 0
        else:
            discount_comparison[key] = (100-discounts[key]*100)/key
    print(discount_comparison)
    best = max(discount_comparison.values())
    return min([k for k, v in discount_comparison.items() if v == best])

def best_price(cart, discounts):
    '''
    This should print out the final grouped cart and return our guess at the best price.
    '''
    best_size = best_set_size(discounts)
    grouped_cart = []
    while True:
        temp_cart = cart[:]
        new_group = []
        for book in cart:
            while len(new_group) < best_size:
                if book not in new_group:
                    new_group.append(book)
                    temp_cart.remove(book)
                else:
                    break
        grouped_cart.append(new_group)
        cart = temp_cart[:]
        new_group = []
        if len(cart) >= best_size:
            continue
        else:
            break
    print('After first optimization, grouped_cart is {}, remaining in cart is {}'.format(grouped_cart, cart))
    while cart:
        grouped_cart.sort(key=len)
        temp_cart = cart[:]
        print('cart: {}'.format(cart))
        print('temp cart: {}'.format(temp_cart))
        for book in cart:
            print('book: {}'.format(book))
            for group in grouped_cart:
                if book not in group and book in temp_cart:
                    group.append(book)
                    temp_cart.remove(book)
                    print('removed {}'.format(book))
        cart = temp_cart[:]
    print('cart: {}'.format(grouped_cart))
    return calculate_price(grouped_cart,discount_structure)



if __name__ == '__main__':
    '''
    The test case outlined in the problem description.
    Misc other test cases.
    '''
    one = Book(1)
    two = Book(2)
    three = Book(3)
    four = Book(4)
    five = Book(5)

    print(best_price([one,one,two,two,three,three,four,five], discount_structure))
    print(best_price([one,one,two,two,three,three,four,four,five], discount_structure))
    print(best_price([one, one, one, two, two, three, three, three, four, four, five, five, five], discount_structure))
