"""fyle_qbo URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import VendorView, EmployeeView, AccountView, CreditCardAccountView, ClassView, DepartmentView, BillView, \
    BillScheduleView, CustomerView, ChequeScheduleView, ChequeView, CreditCardPurchaseView, \
    CreditCardPurchaseScheduleView, JournalEntryView, JournalEntryScheduleView, BankAccountView, AccountsPayableView, \
    PreferencesView

urlpatterns = [
    path('preferences/', PreferencesView.as_view()),
    path('vendors/', VendorView.as_view()),
    path('employees/', EmployeeView.as_view()),
    path('accounts/', AccountView.as_view()),
    path('credit_card_accounts/', CreditCardAccountView.as_view()),
    path('bank_accounts/', BankAccountView.as_view()),
    path('accounts_payables/', AccountsPayableView.as_view()),
    path('classes/', ClassView.as_view()),
    path('departments/', DepartmentView.as_view()),
    path('customers/', CustomerView.as_view()),
    path('bills/', BillView.as_view()),
    path('bills/trigger/', BillScheduleView.as_view()),
    path('checks/', ChequeView.as_view()),
    path('checks/trigger/', ChequeScheduleView.as_view()),
    path('credit_card_purchases/', CreditCardPurchaseView.as_view()),
    path('credit_card_purchases/trigger/', CreditCardPurchaseScheduleView.as_view()),
    path('journal_entries/', JournalEntryView.as_view()),
    path('journal_entries/trigger/', JournalEntryScheduleView.as_view())
]
