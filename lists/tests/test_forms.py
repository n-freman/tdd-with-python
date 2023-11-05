from django.test import TestCase

from lists.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p()) # type: ignore
        self.assertIn('class="form-control form-control-lg"', form.as_p()) # type: ignore

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'], # type: ignore
            [EMPTY_ITEM_ERROR]
        )

