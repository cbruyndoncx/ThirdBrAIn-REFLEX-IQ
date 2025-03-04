Project Path: database

Source Tree:

```
database
├── tables.md
├── queries.md
├── overview.md
└── relationships.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/database/tables.md`:

```md
# Tables

Tables are database objects that contain all the data in a database.

In tables, data is logically organized in a row-and-column format similar to a
spreadsheet. Each row represents a unique record, and each column represents a
field in the record.

## Creating a Table

To create a table make a class that inherits from `rx.Model`.

The following example shows how to create a table called `User`.

```python
class User(rx.Model, table=True):
    username: str
    email: str
```

The `table=True` argument tells Reflex to create a table in the database for
this class.

### Primary Key

By default, Reflex will create a primary key column called `id` for each table.

However, if an `rx.Model` defines a different field with `primary_key=True`, then the
default `id` field will not be created. A table may also redefine `id` as needed.

It is not currently possible to create a table without a primary key.

## Advanced Column Types

SQLModel automatically maps basic python types to SQLAlchemy column types, but
for more advanced use cases, it is possible to define the column type using
`sqlalchemy` directly. For example, we can add a last updated timestamp to the
post example as a proper `DateTime` field with timezone.

```python
import datetime

import sqlmodel
import sqlalchemy

class Post(rx.Model, table=True):
    ...
    update_ts: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update_ts",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
```

To make the `Post` model more usable on the frontend, a `dict` method may be provided
that converts any fields to a JSON serializable value. In this case, the dict method is
overriding the default `datetime` serializer to strip off the microsecond part.

```python
class Post(rx.Model, table=True):
    ...

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["update_ts"] = self.update_ts.replace(microsecond=0).isoformat()
        return d
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/database/queries.md`:

```md
# Queries

Queries are used to retrieve data from a database.

A query is a request for information from a database table or combination of
tables. A query can be used to retrieve data from a single table or multiple
tables. A query can also be used to insert, update, or delete data from a table.

## Session

To execute a query you must first create a `rx.session`. You can use the session
to query the database using SQLModel or SQLAlchemy syntax.

The `rx.session` statement will automatically close the session when the code
block is finished. **If `session.commit()` is not called, the changes will be
rolled back and not persisted to the database.** The code can also explicitly
rollback without closing the session via `session.rollback()`.

The following example shows how to create a session and query the database.
First we create a table called `User`.

```python
class User(rx.Model, table=True):
    username: str
    email: str
```

### Select

Then we create a session and query the User table.

```python
class QueryUser(rx.State):
    name: str
    users: list[User]

    @rx.event
    def get_users(self):
        with rx.session() as session:
            self.users = session.exec(
                User.select().where(
                    User.username.contains(self.name))).all()
```

The `get_users` method will query the database for all users that contain the
value of the state var `name`.

### Insert

Similarly, the `session.add()` method to add a new record to the
database or persist an existing object.

```python
class AddUser(rx.State):
    username: str
    email: str
    
    @rx.event
    def add_user(self):
        with rx.session() as session:
            session.add(User(username=self.username, email=self.email))
            session.commit()
```

### Update

To update the user, first query the database for the object, make the desired
modifications, `.add` the object to the session and finally call `.commit()`.

```python
class ChangeEmail(rx.State):
    username: str
    email: str

    @rx.event
    def modify_user(self):
        with rx.session() as session:
            user = session.exec(User.select().where(
                (User.username == self.username))).first()
            user.email = self.email
            session.add(user)
            session.commit()
```

### Delete

To delete a user, first query the database for the object, then call
`.delete()` on the session and finally call `.commit()`.

```python
class RemoveUser(rx.State):
    username: str

    @rx.event
    def delete_user(self):
        with rx.session() as session:
            user = session.exec(User.select().where(
                User.username == self.username)).first()
            session.delete(user)
            session.commit()
```

## ORM Object Lifecycle

The objects returned by queries are bound to the session that created them, and cannot generally
be used outside that session. After adding or updating an object, not all fields are automatically
updated, so accessing certain attributes may trigger additional queries to refresh the object.

To avoid this, the `session.refresh()` method can be used to update the object explicitly and
ensure all fields are up to date before exiting the session.

```python
class AddUserForm(rx.State):
    user: User | None = None
    
    @rx.event
    def add_user(self, form_data: dict[str, Any]):
        with rx.session() as session:
            self.user = User(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)
```

Now the `self.user` object will have a correct reference to the autogenerated
primary key, `id`, even though this was not provided when the object was created
from the form data.

If `self.user` needs to be modified or used in another query in a new session,
it must be added to the session. Adding an object to a session does not
necessarily create the object, but rather associates it with a session where it
may either be created or updated accordingly.

```python
class AddUserForm(rx.State):
    ...
    
    @rx.event
    def update_user(self, form_data: dict[str, Any]):
        if self.user is None:
            return
        with rx.session() as session:
            self.user.set(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)
```

If an ORM object will be referenced and accessed outside of a session, you
should call `.refresh()` on it to avoid stale object exceptions.

## Using SQL Directly

Avoiding SQL is one of the main benefits of using an ORM, but sometimes it is
necessary for particularly complex queries, or when using database-specific
features.

SQLModel exposes the `session.execute()` method that can be used to execute raw
SQL strings.  If parameter binding is needed, the query may be wrapped in
[`sqlalchemy.text`](https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.text),
which allows colon-prefix names to be used as placeholders.

```md alert info
# Never use string formatting to construct SQL queries, as this may lead to SQL injection vulnerabilities in the app.
```

```python
import sqlalchemy

import reflex as rx


class State(rx.State):

    @rx.event
    def insert_user_raw(self, username, email):
        with rx.session() as session:
            session.execute(
                sqlalchemy.text(
                    "INSERT INTO user (username, email) "
                    "VALUES (:username, :email)"
                ),
                \{"username": username, "email": email},
            )
            session.commit()

    @rx.var
    def raw_user_tuples(self) -> list[list]:
        with rx.session() as session:
            return [list(row) for row in session.execute("SELECT * FROM user").all()]
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/database/overview.md`:

```md
# Database

Reflex uses [sqlmodel](https://sqlmodel.tiangolo.com) to provide a built-in ORM wrapping SQLAlchemy.

The examples on this page refer specifically to how Reflex uses various tools to
expose an integrated database interface.  Only basic use cases will be covered
below, but you can refer to the
[sqlmodel tutorial](https://sqlmodel.tiangolo.com/tutorial/select/)
for more examples and information, just replace `SQLModel` with `rx.Model` and
`Session(engine)` with `rx.session()`

For advanced use cases, please see the
[SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/orm/quickstart.html) (v1.4).

```md alert info
# Using NoSQL Databases

If you are using a NoSQL database (e.g. MongoDB), you can work with it in Reflex by installing the appropriate Python client library. In this case, Reflex will not provide any ORM features.
```

## Connecting

Reflex provides a built-in SQLite database for storing and retrieving data.

You can connect to your own SQL compatible database by modifying the
`rxconfig.py` file with your database url.

```python
config = rx.Config(
    app_name="my_app",
    db_url="sqlite:///reflex.db",
)
```

For more examples of database URLs that can be used, see the [SQLAlchemy
docs](https://docs.sqlalchemy.org/en/14/core/engines.html#backend-specific-urls).
Be sure to install the appropriate DBAPI driver for the database you intend to
use.

## Tables

To create a table make a class that inherits from `rx.Model` with and specify
that it is a table.

```python
class User(rx.Model, table=True):
    username: str
    email: str
    password: str   
```

## Migrations

Reflex leverages [alembic](https://alembic.sqlalchemy.org/en/latest/)
to manage database schema changes.

Before the database feature can be used in a new app you must call `reflex db init`
to initialize alembic and create a migration script with the current schema.

After making changes to the schema, use
`reflex db makemigrations --message 'something changed'`
to generate a script in the `alembic/versions` directory that will update the
database schema. It is recommended that scripts be inspected before applying
them.

The `reflex db migrate` command is used to apply migration scripts to bring the
database up to date. During app startup, if Reflex detects that the current
database schema is not up to date, a warning will be displayed on the console.

## Queries

To query the database you can create a `rx.session()`
which handles opening and closing the database connection.

You can use normal SQLAlchemy queries to query the database.

```python
with rx.session() as session:
    session.add(User(username="test", email="admin@reflex.dev", password="admin"))
    session.commit()
```

```md video https://youtube.com/embed/ITOZkzjtjUA?start=6835&end=8225
# Video: Tutorial of Database Model with Forms, Model Field Changes and Migrations, and adding a DateTime Field
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/database/relationships.md`:

```md
# Relationships

Foreign key relationships are used to link two tables together. For example,
the `Post` model may have a field, `user_id`, with a foreign key of `user.id`,
referencing a `User` model. This would allow us to automatically query the `Post` objects
associated with a user, or find the `User` object associated with a `Post`.

To establish bidirectional relationships a model must correctly set the
`back_populates` keyword argument on the `Relationship` to the relationship
attribute in the _other_ model.

## Foreign Key Relationships

To create a relationship, first add a field to the model that references the
primary key of the related table, then add a `sqlmodel.Relationship` attribute
which can be used to access the related objects.

Defining relationships like this requires the use of `sqlmodel` objects as
seen in the example.

```python
from typing import List, Optional

import sqlmodel

import reflex as rx


class Post(rx.Model, table=True):
    title: str
    body: str
    user_id: int = sqlmodel.Field(foreign_key="user.id")

    user: Optional["User"] = sqlmodel.Relationship(back_populates="posts")
    flags: Optional[List["Flag"]] = sqlmodel.Relationship(back_populates="post")


class User(rx.Model, table=True):
    username: str
    email: str

    posts: List[Post] = sqlmodel.Relationship(back_populates="user")
    flags: List["Flag"] = sqlmodel.Relationship(back_populates="user")


class Flag(rx.Model, table=True):
    post_id: int = sqlmodel.Field(foreign_key="post.id")
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    message: str

    post: Optional[Post] = sqlmodel.Relationship(back_populates="flags")
    user: Optional[User] = sqlmodel.Relationship(back_populates="flags")
```

See the [SQLModel Relationship Docs](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/define-relationships-attributes/) for more details.

## Querying Relationships

### Inserting Linked Objects

The following example assumes that the flagging user is stored in the state as a
`User` instance and that the post `id` is provided in the data submitted in the
form.

```python
class FlagPostForm(rx.State):
    user: User

    @rx.event
    def flag_post(self, form_data: dict[str, Any]):
        with rx.session() as session:
            post = session.get(Post, int(form_data.pop("post_id")))
            flag = Flag(message=form_data.pop("message"), post=post, user=self.user)
            session.add(flag)
            session.commit()
```

### How are Relationships Dereferenced?

By default, the relationship attributes are in **lazy loading** or `"select"`
mode, which generates a query _on access_ to the relationship attribute. Lazy
loading is generally fine for single object lookups and manipulation, but can be
inefficient when accessing many linked objects for serialization purposes.

There are several alternative loading mechanisms available that can be set on
the relationship object or when performing the query.

* "joined" or `joinload` - generates a single query to load all related objects
  at once.
* "subquery" or `subqueryload` - generates a single query to load all related
  objects at once, but uses a subquery to do the join, instead of a join in the
  main query.
* "selectin" or `selectinload` - emits a second (or more) SELECT statement which
  assembles the primary key identifiers of the parent objects into an IN clause,
  so that all members of related collections / scalar references are loaded at
  once by primary key

There are also non-loading mechanisms, "raise" and "noload" which are used to
specifically avoid loading a relationship.

Each loading method comes with tradeoffs and some are better suited for different
data access patterns.
See [SQLAlchemy: Relationship Loading Techniques](https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html)
for more detail.

### Querying Linked Objects

To query the `Post` table and include all `User` and `Flag` objects up front,
the `.options` interface will be used to specify `selectinload` for the required
relationships. Using this method, the linked objects will be available for
rendering in frontend code without additional steps.

```python
import sqlalchemy


class PostState(rx.State):
    posts: List[Post]

    @rx.event
    def load_posts(self):
        with rx.session() as session:
            self.posts = session.exec(
                Post.select
                .options(
                    sqlalchemy.orm.selectinload(Post.user),
                    sqlalchemy.orm.selectinload(Post.flags).options(
                        sqlalchemy.orm.selectinload(Flag.user),
                    ),
                )
                .limit(15)
            ).all()
```

The loading methods create new query objects and thus may be linked if the
relationship itself has other relationships that need to be loaded. In this
example, since `Flag` references `User`, the `Flag.user` relationship must be
chain loaded from the `Post.flags` relationship.

### Specifying the Loading Mechanism on the Relationship

Alternatively, the loading mechanism can be specified on the relationship by
passing `sa_relationship_kwargs=\{"lazy": method}` to `sqlmodel.Relationship`,
which will use the given loading mechanism in all queries by default.

```python
from typing import List, Optional

import sqlmodel

import reflex as rx


class Post(rx.Model, table=True):
    ...
    user: Optional["User"] = sqlmodel.Relationship(
        back_populates="posts",
        sa_relationship_kwargs=\{"lazy": "selectin"},
    )
    flags: Optional[List["Flag"]] = sqlmodel.Relationship(
        back_populates="post",
        sa_relationship_kwargs=\{"lazy": "selectin"},
    )
```

```