from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import stripe 
 

 
router = APIRouter(
    prefix='/stripe',
    tags=['Stripe']
)
 
YOUR_DOMAIN='http://localhost'
stripe.api_key='sk_test_51O9vUsGBGoeLY0IsEfMIjlbM7sUx8RfkCqhC2AE7NOqb2ziILyuZSip8LNk8fMbeAPbJrXEx8T8qh6KMczOogecZ00fjyAC0de'
 
@router.get('/checkout')
async def get_checkout():
    checkout_session = stripe.checkout.Session.create(
        success_url = YOUR_DOMAIN+'/success.html',
        cancel_url = YOUR_DOMAIN+'/cancel.html',
        line_items=[
            {
                "price": 'price_1O9w2EGBGoeLY0IsPEMR9Nl8',
                "quantity": 1,
            }
        ],
        mode="subscription",
        payment_method_types = ['card'],
    )
    return RedirectResponse(checkout_session['url'])
 
# @router.get('/webhook')
# async def retreive_webhook():
#     return