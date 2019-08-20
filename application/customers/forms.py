from flask_wtf import FlaskForm
from wtforms import StringField, validators
from application.customers.models import Customer


class CustomerForm(FlaskForm):
    name = StringField("Asiakkaan nimi", [validators.Length(min=1)])
    erp_id = StringField("Asiakasnumero", [validators.Length(min=4)])
    route = StringField("Reitti")
    contact_person = StringField("Yhteyshenkilöt (erottele nimet pilkulla)")
    phone_number = StringField("Puhelinnumerot (erottele numerot pilkulla)")
    email = StringField("Sähköposti")

    class Meta:
        csrf = False

