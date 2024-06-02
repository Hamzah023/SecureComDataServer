from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1), error_messags={"required": "Name is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required."})
    missing_field = fields.String(missing='N/A please input')
