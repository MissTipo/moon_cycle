"""Define the GraphQL schema for the API."""

import graphene
from .types import UserType
from .models import User


class User(graphene.ObjectType):
    """Define the User type."""
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()


class Query(graphene.ObjectType):
    """Define the Query type."""

    user = graphene.Field(User)

    def resolve_user(self, info):
        """Resolve the user query."""
        pass


class CreateUserMutation(graphene.Mutation):
    """Define the CreateUser mutation."""

    user = graphene.Field(User)

    class Arguments:
        """Define the CreateUser mutation arguments."""

        username = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        """Mutate the CreateUser mutation."""
        # Logic to create a user
        user = User.objects.create(
            username=username, password=password, email=email)
        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    """Define the UpdateUser mutation."""

    user = graphene.Field(User)

    class Arguments:
        """Define the UpdateUser mutation arguments."""

        class Arguments:
            """Define the CreateUser mutation arguments."""

            user_id = graphene.ID(required=True)
            username = graphene.String()
            email = graphene.String()
            password = graphene.String()

        user = graphene.Field(UserType)

        def mutate(self, info, user_id, username=None, email=None, password=None):
            """Mutate the UpdateUser mutation."""
            user = User.objects.get(id=user_id)
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            user.save()
            return UpdateUserMutation(user=user)


class Mutation(graphene.ObjectType):
    """Define the mutation type."""

    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
