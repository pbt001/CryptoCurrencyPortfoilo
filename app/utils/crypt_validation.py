from app.models.crypt_db import Crypt
from app.models.user_db import User


class CryptValidation():
    """
    Validate input data
    """

    def validate(self, user_id, crypt_name):
        """
        Check currency name is in db
        """
        crypt = Crypt.find_currency_name(crypt_name)
        # get user info
        user = User.update_user_info(user_id)

        if crypt is not None and user != False:
            return crypt, user
        return False