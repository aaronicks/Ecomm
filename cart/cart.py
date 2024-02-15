from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session

        # get the current session ket if it exist
        cart = self.session.get('session_key')

        # if the user is new no session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure the cart functions on all pages of site
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # some logic if product is in the cart or not
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        # getting product ids
        product_ids = self.cart.keys()
        # look up those keys in our product databse
        products = Product.objects.filter(id__in=product_ids)
        # get quantities
        quantities = self.cart
        # start counting
        total = 0
        for key, value in quantities.items():
            # convert string into int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.is_sale * int(value))
                    else:
                        total = total + (product.price * int(value))

        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prod(self):

        # get ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup product in the database
        products = Product.objects.filter(id__in=product_ids)

        # return lookup product
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # {'4':3, '5':6} product looks like this
        # get cart
        ourcart = self.cart
        # updating the cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

            self.session.modified = True
