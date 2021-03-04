from django.db import models
from django.urls import reverse
import uuid  # Required for unique item instances


class Category(models.Model):
    """
    Model representing an item category (e.g. Meat, Cheese).
    """
    name = models.CharField(max_length=200, help_text="Enter an item category (e.g. Meat, Cheese, Milk etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Item(models.Model):
    """
    Model representing an item (but not a specific copy of an item).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because item can only have one salesperson, but salesperson can have multiple items
    # Salesperson as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the item")
    # isbn = models.CharField('ISBN',max_length=13, help_text='13
    # Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    category = models.ManyToManyField(Category, help_text="Select a category for this item")

    # ManyToManyField used because category can contain many items. Items can cover many categories.
    # Category class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('item-detail', args=[str(self.title)])


class ItemInstance(models.Model):
    """
    Model representing a specific copy of an item (i.e. that can be borrowed from the marketplace).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular item across whole marketplace")
    item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(blank=False)
    tags = models.ManyToManyField('Tag', related_name='items')


    ITEM_STATUS = (
        ('a', 'Available'),
        ('n', 'Not Available'),
    )

    status = models.CharField(max_length=1, choices=ITEM_STATUS, blank=True, default='a', help_text='Item availability')

    class Meta:
        ordering = ["status"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return f'{self.item}'


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.last_name)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Tag(models.Model):
    """
    Model representing the tag for the goods category.
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        String for representing the Tag.
        """
        return self.name
