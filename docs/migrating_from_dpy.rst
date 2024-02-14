.. currentmodule:: discord

.. _migrating_from_dpy:

Migrating to This Library
==========================

| This library is designed to be compatible with discord.py.
| However, the user and bot APIs are *not* the same.

Most things bots can do, users can (in some capacity) as well. The biggest difference is the amount of added things: users can do a lot more things than bots can.

However, a number of things have been removed.
For example:

- ``Intents``: While the gateway technically accepts intents for user accounts, they are—for the most part—useless and can break things.
- ``Shards``: Just like intents, users can utilize sharding but it is not very useful.
- ``discord.ui``: Users cannot utilize the bot UI kit.
- ``discord.app_commands``: Users cannot register application commands.

However, even in features that are shared between user and bot accounts, there may be variance in functionality or simply different design choices that better reflect a user account implementation.
An effort is made to minimize these differences and avoid migration pain, but it is not always the first priority.

Guild Subscriptions
-------------------

Guild Members
~~~~~~~~~~~~~~
The concept of privileged intents does not exist for user accounts, so guild member access for user accounts is limited in different ways.

Implementation
~~~~~~~~~~~~~~~
The library offers two avenues to get the "entire" member list of a guild.

- :func:`Guild.chunk`: If a guild has less than 1,000 members, and has at least one channel that everyone can view, you can use this method to fetch the entire member list by scraping the member sidebar. With this method, you also get events.
- :func:`Guild.fetch_members`: If you have the permissions to request all guild members, you can use this method to fetch the entire member list. Else, this method scrapes the member sidebar (which can become very slow), this only returns online members if the guild has more than 1,000 members. This method does not get events.

AutoMod
--------

The following Gateway events are not dispatched to user accounts:

- ``on_automod_rule_create``
- ``on_automod_rule_update``
- ``on_automod_rule_delete``
- ``on_automod_action``

The first three can be replaced by listening to the :func:`discord.on_audit_log_entry_create` event and checking the :attr:`~discord.AuditLogEntry.action` attribute.
The last one is partially replaceable by listening to the :func:`discord.on_message` event and checking for AutoMod system messages, but it is not a perfect replacement.
