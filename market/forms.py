from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # SECURITY: `is_staff` was previously an editable field here (relabeled
        # "Show my name on the department board"). That is a Django privilege
        # flag — it grants Django admin access and, in this app, the department
        # desk. Exposing it let any user promote themselves to staff from the
        # profile page. Privilege flags must never be user-editable, so the
        # field is removed. Staff status is granted only by an existing admin.
        fields = ["first_name", "last_name", "email"]
