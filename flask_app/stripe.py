from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', key='pk_test_51IbR9lSB3ZNBO9n8xt5VcoIt1Dvli4vVoR43wftcaGBzjgz90eHBZp8XPsLO6TV8bHBovJnSjUCnRWVUUcyPcyXN000LNdSo9d')

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)