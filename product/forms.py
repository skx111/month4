from django import forms

from product.models import Product, Category, Review

class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        min_length=3,
        label='Название продукта',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Описание продукта',
        required=False,
    )
    image = forms.ImageField(
        required=False,
        label='Картинка',
    )


    def clean_title(self):
        title = self.cleaned_data['title']

        if 'python' not in title.lower():
            raise forms.ValidationError('В заголовке должно быть слово "python"')

        return title


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'text', 'image')
        labels = {
            'title': 'Название поста',
            'text': 'Текст поста',
            'image': 'Картинка',
        }
        help_texts = {
            'title': 'Введите название поста',
            'text': 'Введите текст поста',
            'image': 'Загрузите картинку',
        }

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

