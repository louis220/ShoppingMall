from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegisterForm
from .models import Product, Photo


# Create your views here.


class UpdateView(FormView):
    template_name = "product/update.html"
    form_class = RegisterForm
    success_url = '/'


    def form_valid(self, form):


        title = form.data.get('title')
        price = form.data.get('price')
        discount = form.data.get('discount')
        description = form.data.get('description')


        product = Product(
            title=title,
            price=price,
            discount=discount,
            description=description,

        )

        product.save()
        # photo_list = self.request.FILES.getlist('imgs')
        # for item in photo_list:
        #     photo = Photo(
        #         item
        #     )

        if(self.request.method == 'POST'):


            for img in self.request.FILES.getlist('imgs'):

                photo = Photo()
                photo.post = product
                photo.image = img

                photo = Photo(

                    image = photo.image,
                    post = photo.post
                )
                photo.save()


        # self.request.session['user'] = id
        return super().form_valid(form)
    # def PhotoUpload(request):
    #     if(request.method == 'POST'):
    #         post = Product()
    #
    #
    #         for img in request.FILES.getlist('imgs'):
    #             photo = Photo()
    #             photo.post = post
    #             photo.image = img
    #             photo.save()
    #         return redirect('/' +str(post.id))
    #     else:
    #         return render(request, 'product/update.html')


def ProductView(request):
    products = Product.objects.all()
    context = {'products' : products}

    return render(request, "product/list.html", context)



