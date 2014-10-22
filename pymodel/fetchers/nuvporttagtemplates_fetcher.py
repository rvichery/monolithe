# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVPortTagTemplatesFetcher(NURESTFetcher):
    """ VPortTagTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPortTagTemplate
        return NUVPortTagTemplate