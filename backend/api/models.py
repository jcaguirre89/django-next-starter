import json

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
import numpy as np


class Client(models.Model):
    """ A Client created by a Contractor for a specific Proposal """
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('users.User',
                             on_delete=models.CASCADE,
                             related_name='clients')


class Product(models.Model):

    LDCF = 'ldcf'
    FINISHES = 'finishes'
    MEP = 'mep'
    EQUIPMENT = 'equipment'

    CATEGORY = (
        (LDCF, 'Lumber, Dryway, Compounds, Fasteners'),
        (FINISHES, 'Subcontracted Finishes'),
        (MEP, 'Subcontracted MEP'),
        (EQUIPMENT, 'Equipment Rentals'),
    )
    """ Products are uniquely named for each user that created them """
    name = models.CharField(max_length=100,
                            help_text='Short name for this product/service')
    description = models.TextField(blank=True,
                                   help_text="Product/service description")
    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return self.slug

    @property
    def slug(self):
        return '-'.join(self.name.strip().lower().split())


class Proposal(models.Model):
    user = models.ForeignKey('users.User',
                             on_delete=models.CASCADE,
                             related_name='proposals')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='proposals')
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=300)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    @property
    def product_ids(self):
        """ Returns a list of Product IDs of all responses in the current proposal """
        if self.responses.all():
            return self.responses.all().values_list('product', flat=True)
        return []

    @property
    def product_objects(self):
        """ Returns list of Product objects for all responses """
        return [Product.objects.get(pk=id) for id in self.product_ids]

    def _product_prices(self, product_id):
        """
        Return a list of prices of a product in a proposal
        :param: product_id: Product id
        """
        return [
            response.price for response in self.responses.all()
            if response.product.pk == product_id
        ]

    def avg_price_product(self, product):
        """ Average price for a product among respondents """
        prices = self._product_prices(product)
        if prices:
            return np.mean(prices)
        return 0

    @property
    def n_products(self):
        """ Number of unique products in proposal """
        products = self.responses.all().distinct('product')
        return len(products)

    @property
    def n_responses(self):
        """ number of responses to this proposal by individual vendors """
        vendors = self.responses.all().distinct('user')
        return len(vendors)


class Response(models.Model):
    """ Table with each bid from vendors to proposals """
    user = models.ForeignKey('users.User',
                             on_delete=models.CASCADE,
                             related_name="responses")
    proposal = models.ForeignKey(Proposal,
                                 on_delete=models.CASCADE,
                                 related_name="responses")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="responses")
    price = models.FloatField(default=0.0)
    date_responded = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)

    class Meta:
        # Each vendor can only bid once on a product in a proposal
        unique_together = ('user', 'proposal', 'product')
