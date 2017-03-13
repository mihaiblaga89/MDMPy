'''
Project : MDMPy2
File : settings
Author : Lego
Date : 27/02/2017
'''
import models.dbtool as DB
import traceback
from peewee import IntegrityError


class Settings:

    @staticmethod
    def set(key="", value=""):
        if not key or not value:
            raise Exception("Please provide a key and a value")

        try:
            newrecord = DB.Settings(key=key, value=value)
            newrecord.save()
        except IntegrityError:
            update = DB.Settings.get(DB.Settings.key == key)
            if update.value != value:
                update.value = value
                update.save()
        except:
            traceback.print_exc()
            raise Exception("Can't add setting")


    @staticmethod
    def get(key="", default=None):
        if not key:
            raise Exception("Please provide a key")

        try:
            result = DB.Settings.get(DB.Settings.key == key)
            return result.value
        except DB.Settings.DoesNotExist:
            return default
        except:
            raise Exception("Can't get setting")