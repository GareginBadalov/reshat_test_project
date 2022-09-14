import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Items, Orders


def get_product(name):
    search_result = stripe.Product.search(query=f"name:'{name}'")
    return stripe.Product.retrieve(search_result.data[0]['id'])


def get_price_id(name):
    return get_product(name).default_price


class ItemPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ItemPageView, self).get_context_data(**kwargs)
        context['item'] = Items.objects.get(pk=self.kwargs['pk'])
        return context


class OrderPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, pk, **kwargs):
        context = super(OrderPageView, self).get_context_data(**kwargs)
        order = Orders.objects.get(pk=self.kwargs['pk'])
        items_id = order.item_ids.all()
        context['items'] = Items.objects.filter(id__in=items_id)
        context['order'] = order
        return context


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


class CreateStripeSession(View):
    def get(self, request, pk):
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = Items.objects.get(pk=pk)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': get_price_id(item.name),
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=domain_url + 'success',
                cancel_url=domain_url + 'cancelled')
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class CreateStripeSessionForOrder(View):

    def get(self, request, pk):
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        order = Orders.objects.get(pk=pk)
        items_id = order.item_ids.all()
        items = Items.objects.filter(id__in=items_id)
        products_body = [{'price': get_price_id(item.name),
                          'quantity': 1} for item in items]
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=products_body,
                mode='payment',
                success_url=domain_url + 'success',
                cancel_url=domain_url + 'cancelled')
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    stripe.api_key = settings.STRIPE_SECRET_KEY

    def create(self, request, *args, **kwargs):
        req_data = request.data
        serializer = self.get_serializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        stripe.Product.create(
            name=req_data['name'],
            default_price_data={"unit_amount_decimal": str(int(req_data['price']) * 100), "currency": "usd"},
            expand=["default_price"],
        )
        return Response(serializer.data)
