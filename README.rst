Django-Threaded-Multihost
=========================
djangoplicity-threaded multihost provides support utilities to enable easy multi-site awareness in Django apps.

Installing Django-Threaded-Multihost
------------------------------------

With threaded_multihost on your PYTHONPATH, just add the Threadlocal middleware to your MIDDLEWARE_CLASSES entry in your "settings.py" file.

For example::

 MIDDLEWARE_CLASSES = (
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
 )


Testing
-------

Test suite can be done by running ./manage.py test in the "tests" directory.

Contributing to django-threaded-multihost
-----------------------------------------

We are pleased to accept contributions and bugfixes for django-threaded-multihost.

To make a contribution:

1. First fork the project from bitbucket.

2. Build and test your addon or update.  You **must** provide tests for us to accept your contribution, and these tests *should* be unit tests rather than doctests.  However, doctests in models are acceptible.  If you are fixing a bug, it is a good rule of thumb to provide a test which provides a regression-test against that bug.

3. If this is a simple patch, go to `django-threaded-multihost on bitbucket`_ and enter a bug with the patch.

4. If this is a larger patch or a new feature, make a branch and propose its merger:

   - Make a fork on bitbucket for your addition
   - Make your changes to the fork
   - Issue a pull request when it is ready for inclusion into tip.

.. _`django-threaded-multihost on bitbucket`: https://bitbucket.org/bkroeze/django-threaded-multihost


Threaded Multihost Authors and Contributors
-------------------------------------------

Core developers
---------------

- [Bruce Kroeze brucek@solidsitesolutions.com]

Contributors
------------

- Herbert Poul http://sct.sphene.net, for inspiration, ideas, and the original Threadlocals we have heavily modified.
- Dirk Datzert <dirk@datzert.de> for contributing the initial test suite
  and the UserField/CreatorField/EditorField in fields.py