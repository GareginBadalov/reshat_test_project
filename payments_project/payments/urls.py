from django.urls import path
from . import views

list_actions = {
    'get': 'list',

}
create_action = {
    'post': 'create',
}
detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}


item_list = views.ItemViewSet.as_view(list_actions)
item_create = views.ItemViewSet.as_view(create_action)
item_detail = views.ItemViewSet.as_view(detail_actions)

urlpatterns = [
    path('item/<int:pk>', views.ItemPageView.as_view(), name='buy-item'),
    path('order/<int:pk>', views.OrderPageView.as_view(), name='buy-multiple-item-by-oreder'),
    path('buy/<int:pk>', views.CreateStripeSession.as_view(), name='create-session'),
    path('buy/order/<int:pk>', views.CreateStripeSessionForOrder.as_view(), name='create-session-by-order'),
    path('success/', views.SuccessView.as_view(), name='success-page'),
    path('cancelled/', views.CancelledView.as_view(), name='cancel-page'),
    path('itemList/', item_list, name='item-list'),
    path('item/create', item_create, name='item-create'),
    path('itemDetail/<int:pk>/', item_detail, name='item-detail'),
]
