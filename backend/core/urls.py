from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CardViewSet, LoanViewSet, predict_loan

# Create API router for ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cards', CardViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Registers API routes
    path('api/loan-predict/', predict_loan, name="loan-predict"),  # Loan prediction endpoint
]
