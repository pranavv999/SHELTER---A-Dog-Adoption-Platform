from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField,
                     BooleanField, TextAreaField)
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)
from shelter.models import User
from flask_login import current_user


class SignUpForm(FlaskForm):
    name = StringField(label='Firstname',
                       validators=[DataRequired(), Length(min=1, max=20)])

    surname = StringField(label='Surname',
                          validators=[DataRequired(), Length(min=1, max=20)])

    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])

    mobile_number = StringField(label='Mobile Number',
                                validators=[
                                            DataRequired(),
                                            Length(min=10, max=10)
                                            ]
                                )

    password = PasswordField(label='Password',
                             validators=[DataRequired()])

    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[
                                                 DataRequired(),
                                                 EqualTo('password')
                                                 ]
                                     )

    submit = SubmitField(label='Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already exists')

    def validate_mobile_number(self, mobile_number):
        user = User.query.filter_by(mobile_number=mobile_number.data).first()

        if user:
            raise ValidationError('Mobile number already exists')


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField(label='Password',
                             validators=[DataRequired()])

    remember = BooleanField(label='Remember me', default='checked')

    submit = SubmitField(label='Login')


class UpdateAccountForm(FlaskForm):
    name = StringField(label='Firstname',
                       validators=[DataRequired(), Length(min=1, max=20)])

    surname = StringField(label='Surname',
                          validators=[DataRequired(), Length(min=1, max=20)])

    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])

    mobile_number = StringField(label='Mobile Number',
                                validators=[
                                            DataRequired(),
                                            Length(min=10, max=10)
                                            ]
                                )

    submit = SubmitField(label='Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email already exists')

    def validate_mobile_number(self, mobile_number):
        if mobile_number.data != current_user.mobile_number:
            user = User.query.filter_by(mobile_number=mobile_number.data).\
                   first()

            if user:
                raise ValidationError('Mobile number already exists')


class AdvertiseForm(FlaskForm):
    dog_breed = StringField(label='Dog Breed',
                            validators=[DataRequired(), Length(min=1, max=20)]
                            )

    location = StringField(label='Location of Dog',
                           validators=[DataRequired()]
                          )

    description = TextAreaField(label='Description of Dog',
                                validators=[DataRequired()]
                                )

    dog_pic = FileField(label='Dog image',
                        validators=[FileRequired(),
                                    FileAllowed(['jpg', 'png', 'jpeg'],
                                                'Images only!')
                                    ]
                        )

    submit = SubmitField(label='Post Ad')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()

    #     if user:
    #         raise ValidationError('Email already exists')

    # def validate_mobile_number(self, mobile_number):
    #     user = User.query.filter_by(mobile_number=mobile_number.data).first()

    #     if user:
    #         raise ValidationError('Mobile number already exists')
