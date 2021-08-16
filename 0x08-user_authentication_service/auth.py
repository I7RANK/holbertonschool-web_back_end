#!/usr/bin/env python3
"""This module contains the _hash_password function
"""

from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """returns the hash encrypted password
    """
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers a new user if not exist
        """

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)

            return self._db.add_user(email, hashed_password)

        raise ValueError(
            "User {} already exists".format(email)
        )

    def valid_login(self, email: str, password: str) -> bool:
        """Validates if the user exist and the pass is correct
        """
        user = None

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """generate a new UUID
            and store it in the database as the user’s session_id,
            then return the session ID.
        """
        user = None

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return

        session_id = _generate_uuid()
        setattr(user, "session_id", session_id)

        self._db._session.commit()

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """If the session ID is None or no user is found, returns None.
            Otherwise returns the corresponding user.
        """
        user = None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            pass

        return user

    def destroy_session(self, user_id: int) -> None:
        """updates the corresponding user’s session ID to None
        """
        user = None

        try:
            user = self._db.find_user_by(user_id=user_id)
        except NoResultFound:
            pass

        setattr(user, "session_id", None)

    def get_reset_password_token(self, email: str) -> str:
        """generates a token to restore password if the user exist
        """
        user = None

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        new_uuid = _generate_uuid()

        setattr(user, "reset_token", new_uuid)

        self._db._session.commit()

        return new_uuid

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates the password. If the token is invalid
        """
        user = None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)

        self._db.update_user(
            user.user_id,
            hashed_password=hashed_password,
            reset_token=None
        )
