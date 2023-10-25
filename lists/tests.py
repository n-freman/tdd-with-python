from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1') # type: ignore
        Item.objects.create(text='itemey 2') # type: ignore

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode()) # type: ignore
        self.assertIn('itemey 2', response.content.decode()) # type: ignore


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item' # type: ignore
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second' # type: ignore
        second_item.save()

        saved_items = Item.objects.all() # type: ignore
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1') # type: ignore
        Item.objects.create(text='itemey 2') # type: ignore

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1) # type: ignore
        new_item = Item.objects.first() # type: ignore
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, 'lists/the-only-list-in-the-world/')

