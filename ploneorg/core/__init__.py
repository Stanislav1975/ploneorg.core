# -*- coding: utf-8 -*-
# import patches
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('ploneorg')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
