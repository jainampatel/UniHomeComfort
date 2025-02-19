from django import forms
from .models import CommunityPost,Category, Property,Bidding, AppUser
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Password'}))


class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder': 'Content', 'rows': '4'}),
            'category': forms.Select(  # Change TextInput to Select
                choices=(),  # Initialize with empty choices
            )
        }

    def __init__(self, *args, **kwargs):
        super(CommunityPostForm, self).__init__(*args, **kwargs)
        # Dynamically populate category choices
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]



class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full rounded-md py-3 px-4 bg-gray-100 text-sm outline-[#007bff]', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full rounded-md py-3 px-4 bg-gray-100 text-sm outline-[#007bff]', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full rounded-md py-3 px-4 bg-gray-100 text-sm outline-[#007bff]', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(choices=[('owner', 'Owner'), ('student', 'Student')], widget=forms.Select(attrs={'class': 'inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full rounded-md px-4 bg-gray-100 text-sm py-3 mt-4 outline-[#007bff]', 'placeholder': 'Message', 'rows': '6'}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2', 'country_code', 'mobile_no', 'age', 'address', 'state',
                  'city', 'zip_code', 'gender', 'offer_letter', 'country', 'institute', 'identification', 'occupation',
                  'is_student', 'is_owner']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'Password'}),
            # Corrected
            'first_name': forms.TextInput(attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true',
                                                 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true',
                                                'placeholder': 'Last name'}),
            'email': forms.EmailInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Email'}),
            'country_code': forms.NumberInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl w-16', 'required': 'true', 'placeholder': '1'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true',
                                                  'placeholder': 'Mobile no.'}),
            'age': forms.NumberInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Age'}),
            'address': forms.TextInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl', 'required': 'true', 'placeholder': 'Address'}),
            'state': forms.Select(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'State'}),
            'city': forms.TextInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'City'}),
            'zip_code': forms.TextInput(
                attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'Zip code'}),
            'gender': forms.RadioSelect(attrs={'class': 'border-2 py-2 px-3 rounded-xl flex gap-2 flex-1'},
                                        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
            'offer_letter': forms.FileInput(attrs={'class': 'border-2 py-2 px-3 rounded-xl flex gap-2 flex-1'}),
            'country': forms.TextInput(attrs={'class': 'border-2 py-2 px-3 rounded-xl'}),
            'institute': forms.Select(attrs={'class': 'border-2 py-2 px-3 rounded-xl'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'border-2 py-2 px-3 rounded-xl flex-1', 'required': 'true', 'placeholder': 'Confirm Password'})



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'address']


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type']
        widgets = {
            'property_type': forms.Select(attrs={'class': 'flex-1 border border-gray-300 rounded-lg py-2 px-4'},
                                          choices=Property.property_type)
        }
        labels = {
            'property_type': ''
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['owner','created_at', 'expire', 'lease_required']
        labels = {
            'number_of_bedrooms': 'No. Bedrooms:',
            'number_of_bathrooms': 'No. Bathrooms:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'common-input w-full'}),
            'address': forms.TextInput(attrs={'class': 'common-input w-full'}),
            'city': forms.TextInput(attrs={'class': 'common-input w-full'}),
            'zipcode': forms.TextInput(attrs={'class': 'common-input w-full'}),
            'property_type': forms.Select(attrs={'class': 'common-input w-full'}),
            'number_of_bedrooms': forms.NumberInput(attrs={'class': 'common-input w-full'}),
            'number_of_bathrooms': forms.NumberInput(attrs={'class': 'common-input w-full'}),
            'amenities': forms.Textarea(attrs={'class': 'common-input w-full h-20'}),
            'price': forms.NumberInput(attrs={'class': 'common-input w-full'}),
            'availability_status': forms.Select(attrs={'class': 'common-input w-full'}),
            'available_from': forms.DateTimeInput(attrs={'class': 'common-input w-full'}),
            'available_to': forms.DateTimeInput(attrs={'class': 'common-input w-full'}),
            'is_biddable': forms.CheckboxInput(attrs={'class': 'common-checkbox w-full'}),
            'bidding_min_limit': forms.NumberInput(attrs={'class': 'common-input w-full'}),
            'lease_duration': forms.NumberInput(attrs={'class': 'common-input'}),
            'allowed_lease_people': forms.NumberInput(attrs={'class': 'common-input'}),
            'rules': forms.Textarea(attrs={'class': 'common-input w-full h-20'}),
            'prop_image1': forms.FileInput(attrs={'class': 'common-input w-full '}),
            'prop_image2': forms.FileInput(attrs={'class': 'common-input w-full '}),
            'prop_image3': forms.FileInput(attrs={'class': 'common-input w-full '}),
            'prop_image4': forms.FileInput(attrs={'class': 'common-input'}),
            'prop_image5': forms.FileInput(attrs={'class': 'common-input'}),
            'house_build_date': forms.DateInput(attrs={'class': 'common-input'}),
        }
class BidForm(forms.ModelForm):
    class Meta:
        model = Bidding
        fields = ['bidding_amount','bidding_status']


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'address']

class PropertyOwnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['username', 'password', 'email', 'country_code', 'mobile_no', 'age', 'address', 'state', 'city', 'zip_code', 'occupation', 'identification']
