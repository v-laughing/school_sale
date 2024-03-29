# -*- coding:utf-8 -*-
# __author__ = 'Shanks'
# __date__: '2017-8-25'

from flask import render_template
from . import main_blueprint


@main_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),  404


@main_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


