from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the specified product to the shopping bag """

    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
