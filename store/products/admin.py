from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category') #отображение на главной
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category') # отображение в позиции
    readonly_fields = ('description',) # только для чтения
    search_fields = ('name',) #поиск
    ordering = ('name',) #сортировка


class BasketAdmin(admin.TabularInline): #для связи с админ юзер и показа корзины в профиле
    model = Basket
    fields = ('product', 'quantity', )
    extra = 0 #убрать доп поля