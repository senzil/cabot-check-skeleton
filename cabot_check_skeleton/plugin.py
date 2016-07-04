from django import forms
from cabot.plugins.models import StatusCheckPlugin
from os import environ as env


class SkeletonStatusCheckForm(forms.Form):
    bone_name = forms.CharField(
	help_text = 'Name of the bone to check',
    )


class SkeletonStatusCheckPlugin(StatusCheckPlugin):
    name = 'SkeletonStatusCheckPlugin'
    slug = 'cabot_check_skeleton'
    author = 'Jonathan Balls'
    version = '0.0.1'
    font_icon = 'glyphicon glyphicon-skull'

    config_form = SkeletonStatusCheckForm

    plugin_variables = [
	'SKELETON_LIST_OF_BONES',
    ]

    def run(self, check, result):

        list_of_bones = env.get('SKELETON_LIST_OF_BONES', None)

        if not list_of_bones:
            result.succeeded = False
            result.error = u'SKELETON_LIST_OF_BONES is not defined in environment variables'
            return result

        list_of_bones = list_of_bones.split(',')

        if check.bone_name in list_of_bones:
            result.succeeded = True
            return result
        else:
            result.succeeded = False
            result.error = u'%s is not in the list of bones' % check.bone_name
            return result

    def description(self, check):
        return '%s in list of bones.' % check.bone_name

