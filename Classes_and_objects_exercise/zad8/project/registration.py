from project.user import User
from project.library import Library

class Registration:

    @staticmethod
    def add_user(user: User, library: Library) -> str | None:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library) -> str | None:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        user = next((u for u in library.user_records if user_id == u.user_id), None)

        if not user:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return ("Please check again the provided username - "
                    "it should be different than the username used so far!")

        if user.username in library.rented_books.keys():
            old_rentals = library.rented_books.pop(user.username)

            if new_username in library.rented_books.keys():
                library.rented_books[new_username].update(old_rentals)
            else:
                library[new_username] = old_rentals


        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"