from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators  import DataRequired, Length

class PostForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		]
	)

	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		]
	)

	title = StringField('Title',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		]
	)

	content = StringField('content',
		validators=[
			DataRequired(),
			Length(min=2,max=100)
		]
	)

	submit = SubmitField('Post Content')
