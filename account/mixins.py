from django.http import Http404

class FieldMixins():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author', 'title', 'slug', 'description', 'image',  'published_time', 'status' ,'category']
            self.prepopulated_fields = {'slug': ('title',)}

        elif request.user.is_author:
            self.fields = ['title', 'slug', 'description', 'image', 'published_time', 'category']
            self.prepopulated_fields = {'slug': ('title',)}

        else:
            raise Http404('شما اجازه افزودن پست را ندارید')
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


