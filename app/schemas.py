from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    missing_field = fields.String(missing='N/A please input.')
