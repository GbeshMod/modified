---
title: Lydia
layout: default
parent: Modules
---

# {{ page.title }}

## Acquiring an API key

1. Visit [the website](https://coffeehouse.intellivoid.net "the website") and follow the instructions to get your API Key. Copy it to your clipboard

2. Enter [the configurator](/web/configuration#configuring-modules). Select: Modules -> Lydia Anti-PM -> CLIENT_KEY and paste the key from your clipboard. Exit the configurator and type `.restart` in Telegram.

## Commands

- **Enable**
[Syntax: `enlydia [user id]`]

   Enables Lydia AI for the specified user ID, or for the user you are messaging

 - **Disable**
[Syntax: `dislydia [user id]`]

   Disables Lydia for the specified user, or the user you are messaging

 - **Enable in Groups**
[Syntax: `forcelydia [user id]`]

   Forcibly enables Lydia for that user. If sent in a group, Lydia will be enabled for that user in the group.

 - **Remove all active sessions**
[Syntax: `cleanlydiasessions`]

   Resets all conversations that are ongoing with Lydia. It will lose all state and context and restart the conversation.

 - **Remove all allowed users**
[Syntax: `cleanlydiadisabled`]

   Re-enables Lydia for everyone. This will not override `IGNORE_NO_COMMON`.

## Configuration

 - **API Key**
[Key: `modified.modules.lydia.CLIENT_KEY`, Type: `str`]

   This is the API key, see [here](#acquiring-an-api-key "here")

 - **Ignore users with no common chats**
[Key: `modified.modules.lydia.IGNORE_NO_COMMON`, Type: `boolean`]

   If set to `True`, users who find you by username/search will not have Lydia enabled. Lydia will only apply for users who have groups in common with you. Note that `forcelydia` can still override this.
   
