import os, secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
	random = secrets.token_hex(8)
	'''os.path.splitext function returns name of file without extension 
	and extension of file, we do not need original file name so variable is _ ''' 
	_ , file_ext = os.path.splitext(form_picture.filename)
	picture_fn = random + file_ext
	picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
	output_size = (125,125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
	msg.body = f''' To reset your password, visit the following link:
{url_for('users.reset_token',token=token,_external=True)}

Please ignore this email if you have not made this request. 
	'''
	mail.send(msg)