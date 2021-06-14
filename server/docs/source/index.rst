.. Langman documentation master file, created by
   sphinx-quickstart on Mon Jun 14 15:07:48 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Langman documentation
===================================

Flask Server API
----------------

.. automodule:: server.API
   :members:

Database ORM and Schema
-----------------------

.. automodule:: server.langman_orm
   :members:

Client Stylesheet
-----------------

`Storybook Stylesheet <_static/storybook-static/index.html>`_
(Requires Javascript)

Client Application
------------------
The following describes the JavaScript client.

.. js:module:: App

.. js:class:: App

   .. js:method:: constructor(props)

   The React lifecycle method to initialise the component. Sets 
   the state ``gameStatus`` to 'logged out'. Also, binds methods.

   :param props object: The collection of properties for the 
                        object, which are typically set using JSX 
                        within a render method, but for this top 
                        level component come directly from React.
   
   .. js:method:: startGame(nameValue, langValue)

      Contacts server to start a new game, then updates the state accordingly.

      :param nameValue string: Name of player
      :param langValue string: Two-letter string indicating language choice

      State is set for ``username``, ``language``, ``gameId``, 
      ``badGuesses``, ``guessed``, ``playerId``, ``revealWord``,