# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ssir_generator
                                 A QGIS plugin
 plugin for generating skid site investigation reports
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-08-28
        copyright            : (C) 2020 by Drew
        email                : drew.benentt@ptsinternational.co.uk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ssir_generator class from file ssir_generator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ssir_generator import ssir_generator
    return ssir_generator(iface)
