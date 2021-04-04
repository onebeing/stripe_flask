import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
  'secret_key': 'sk_test_51IbR9lSB3ZNBO9n8gTMv1dt5KpRuAxMiLan1DeoeHGwEqQJUxwKBJngsedVk81wBZpiRZknQYhUvWHEH5XmsLvWd001YHmTHUu',
  'publishable_key': 'pk_test_51IbR9lSB3ZNBO9n8xt5VcoIt1Dvli4vVoR43wftcaGBzjgz90eHBZp8XPsLO6TV8bHBovJnSjUCnRWVUUcyPcyXN000LNdSo9d'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)