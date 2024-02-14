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