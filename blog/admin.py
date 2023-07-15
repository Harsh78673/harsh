from django.contrib import admin
# Register your models here.
from blog.models import *
# To use html import html
from django.utils.html import format_html


# This is made to show some important things that you want to show on the admin post page
class PostAdmin(admin.ModelAdmin):
    # fields = ('title', 'content','user', 'dated', 'active')

    # Use exclude to tell the browser witch things yoy do not want to be shown
    exclude = ( )
    # Read only to see the content only on editor
    readonly_fields = ('img_preview',)

    #  Blog index
    list_display =('title', 'less_content', 'user', 'dated', 'image','is_deleted', 'click_me','sub_title',)
    # To open less content page by clicking on less content use this
    list_display_links = ('title','less_content',)  # It makes converts the value into the link to go the editer
    # To add filters on the admin panel  sub_title a filter to see only those posts that has certain field in them
    list_filter = ('is_deleted','created_at', ('sub_title', admin.EmptyFieldListFilter)) # admin.EmptyFieldListFilter thsi will shopw us only those posts that has the sub title or not empty or not
    # Radio field for tags inside post editor  default is ugly dropdown
    radio_fields = {"tags" :admin.HORIZONTAL}
    # To get save button on top of the page
    save_on_top = True
    # To add pagination on admin panel
    list_per_page = 2


    # Function to not show the complete content of the post in index only shows 30 words add less_content up there and remove content
    def less_content(self ,obj):
        # To change the color of the index content use return in html write the value inside curly brackets same as it is
        return format_html(f'<span style="color:grey">{obj.content[:30]}</span>') 

    # Add button to go to page you click on add the link of the page here {obj.id adds the id there} it tells the browser where to go
    def click_me(self, obj): 
        return format_html(f'<a href="admin/blog/post/{obj.id}/change/" class="default">View</a>')

    # To preview image in create post editor if you add this value in list_display it will show the preview on index page also
    def img_preview(self , obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:200px;width:200px">')


admin.site.register(Post,PostAdmin)

