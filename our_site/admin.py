from django.contrib import admin
from django.utils.safestring import mark_safe
from our_site.models import Legend_IVT, Photo, Legend_on_photo, Comments


@admin.register(Legend_IVT)
class Legend_IVTAdmin(admin.ModelAdmin):
    list_display = ("name", "nickname","get_img")
    list_display_links = ("name","nickname")
    list_filter = ("name", "surname", "nickname", "date_of_born")
    search_fields = ("name","nickname", "surname")

    def get_img(self, obj):
        return mark_safe(f'<img src = {obj.photo.url} width = "100" height = "120">')
    get_img.short_description = 'Изображение Легенды'


class CommentsInLine(admin.StackedInline):
    model = Comments
    extra = 1

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_img')
    list_display_links = ("name",)
    list_filter = ("name", "date_of_post")
    search_fields = ("name","date_of_post")
    inlines = [CommentsInLine]

    def get_img(self, obj):
        return mark_safe(f'<img src = {obj.img.url} width = "100" height = "120">')
    get_img.short_description = 'Фотография'

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name_of_commentor", "date_of_comment",)
    readonly_fields = ("name_of_commentor",)
    list_display_links = ("name_of_commentor",)
    list_filter = ("date_of_comment",)


admin.site.register(Legend_on_photo)
