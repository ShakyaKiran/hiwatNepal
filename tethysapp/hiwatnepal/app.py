from tethys_sdk.base import TethysAppBase, url_map_maker


class Hiwatnepal(TethysAppBase):
    """
    Tethys app class for Hiwatnepal.
    """

    name = 'Hiwatnepal'
    index = 'hiwatnepal:home'
    icon = 'hiwatnepal/images/icon.gif'
    package = 'hiwatnepal'
    root_url = 'hiwatnepal'
    color = '#8e44ad'
    description = 'Place a brief description of your app here.'
    tags = 'HIWAT'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hiwatnepal',
                controller='hiwatnepal.controllers.index'),
            UrlMap(
                name='chartHiwat',
                url='hiwatnepal/chartHiwat',
                controller='hiwatnepal.controllers.chartHiwat'),

        )
        return url_maps
