# -*- coding: utf-8 -*-

import os
import random


def get_photo_path(self, filename):
    """
    Devuelve un nombre aleatorio de archivo
    """
    univ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    name = "".join([random.choice(univ) for i in xrange(20)])
    root, ext = os.path.splitext(filename)

    return u'photos/%s' % (name + ext)