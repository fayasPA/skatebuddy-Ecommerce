from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('/admindashboard',views.admindashboard,name='admindashboard'),
    path('/adminuser',views.adminuser,name='adminuser'),
    path('/adminblock/<int:id>/',views.adminblock,name='adminblock'),
    path('/adminlogout',views.adminlogout,name='adminlogout'),
    path('/admincategory',views.admincategory,name='admincategory'),
    path('/adminproduct',views.adminproduct,name='adminproduct'),
    path('/admin_addproduct',views.admin_addproduct,name='admin_addproduct'),
    path('/edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('/delete_product/<int:id>/',views.delete_product,name='delete_product'),
    path('/edit_category/<int:id>/',views.edit_category,name='edit_category'),
    path('/delete_category/<int:id>/',views.delete_category,name='delete_category'),
    path('/order_list',views.order_list,name='order_list'),
    path('/status_update',views.status_update,name='status_update'),
    path('/coupon',views.coupon,name='coupon'),
    path('/edit_coupon/<int:id>/',views.edit_coupon,name='edit_coupon'),
    path('/delete_coupon/<int:id>/',views.delete_coupon,name='delete_coupon'),
    path('/block_coupon/<int:id>/',views.block_coupon,name='block_coupon'),
    path('/offer',views.offer,name='offer'),
    path('/edit_productoffer/<int:id>/',views.edit_productoffer,name='edit_productoffer'),
    path('/removePoffer/<int:id>/',views.removePoffer,name='removePoffer'),
    path('/add_category_offer',views.add_category_offer,name='add_category_offer'),
    path('/edit_categoryoffer/<int:id>/',views.edit_categoryoffer,name='edit_categoryoffer'),   
    path('/removeCoffer/<int:id>/',views.removeCoffer,name='removeCoffer'),
    path('/salesreport',views.salesreport,name='salesreport'),
    path('/yearly_sales',views.yearly_sales,name='yearly_sales'),
    path('/monthly_sales',views.monthly_sales,name='monthly_sales'),
    path('/dailysaleschart',views.dailysaleschart,name='dailysaleschart'),

]