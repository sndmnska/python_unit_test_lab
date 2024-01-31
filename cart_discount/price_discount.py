def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    # Check for number of items
    if len(item_prices) < 3:
        return 0
    else:
        # If more than 3 items, return lowest priced item. 
        lowest_price = min(item_prices)
        return lowest_price



    

if __name__ == '__main__':
    main()