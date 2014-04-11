# coding: utf-8
from cms.plugin_base import CMSPluginBase
from .models import SliderPlugin
from cms.plugin_pool import plugin_pool

class CMSSliderPlugin(CMSPluginBase):
    model = SliderPlugin
    name = 'Slider'
    render_template = 'px/slider/slider.html'
    text_enabled = False
    admin_preview = False
    fields = ('album',)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'images': instance.images,
        })
        return context

plugin_pool.register_plugin(CMSSliderPlugin)
