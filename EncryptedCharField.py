from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from Crypto.Cipher import Salsa20

from django import forms

#Requires pycrypto / pip install pycryptodome



class EncryptedCharField(models.BinaryField): 

    SALT_SIZE = 8

    def __init__(self, *args, **kwargs):
        self.widget = forms.TextInput       
        super(EncryptedCharField, self).__init__(*args, **kwargs)
        self.editable=True

    def get_internal_type(self):
        return 'EncryptedCharField'    

    def to_python(self, value):
        if isinstance(value, EncryptedCharField):
            return value
        if not value:
            return None
        return value

    def value_to_string(self, obj):
        # value = self.value_from_object(obj)
        return "********"

    def get_prep_value(self, value):
        return self.encrypt(value) if value else None

    def from_db_value(self, value, expression, connection):
        return self.decrypt(value) if value else None

    @staticmethod
    def encrypt(plaintext):
        if not plaintext:
            return None
        plaintext = plaintext.encode()
        cipher = Salsa20.new(key=settings.SECRET_KEY[:32].encode())
        msg = cipher.nonce + cipher.encrypt(plaintext)
        return msg

    @staticmethod
    def decrypt(ciphertext):
        msg_nonce = ciphertext[:8]
        ciphertext = ciphertext[8:]
        cipher = Salsa20.new(key=settings.SECRET_KEY[:32].encode(), nonce=msg_nonce)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode()
