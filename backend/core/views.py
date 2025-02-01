from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Card, Loan
from .serializers import UserSerializer, CardSerializer, LoanSerializer

# User, Card, and Loan API endpoints
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

# Loan Prediction Endpoint
@api_view(['POST'])
def predict_loan(request):
    """
    Loan approval prediction API.
    Uses a simple rule-based system instead of AI.
    """
    data = request.data
    income = data.get("income", 0)
    credit_score = data.get("credit_score", 0)
    loan_amount = data.get("loan_amount", 0)

    # Simple rule-based logic for loan approval, because OpenAI wasn't an option for me.
    if income >= 5000 and credit_score >= 700 and loan_amount <= (income * 5):
        prediction = "Approved"
    else:
        prediction = "Rejected"

    return Response({"prediction": prediction})
