from django.urls import path

from .linesticker import (
    LineStickerAnimatedGifDownloadView, LineStickerAnimatedFramesDownloadView, LineStickerAnimatedPngRedirectView,
    LineStickerPackageDownloadView, LineStickerDownloadView
)
from .shorturl import ShortUrlMainView

urlpatterns = [
    path(
        'linesticker/download',
        LineStickerDownloadView.as_view(),
        name="service.linesticker.ui"
    ),
    path(
        'linesticker/<int:pack_id>/stickers.zip',
        LineStickerPackageDownloadView.as_view(),
        name="service.linesticker.pack"
    ),
    path(
        'linesticker/<int:pack_id>/<int:sticker_id>/sticker.gif',
        LineStickerAnimatedGifDownloadView.as_view(),
        name="service.linesticker.animated.gif"
    ),
    path(
        'linesticker/<int:pack_id>/<int:sticker_id>/frames.zip',
        LineStickerAnimatedFramesDownloadView.as_view(),
        name="service.linesticker.animated.frames"
    ),
    path(
        'linesticker/<int:pack_id>/<int:sticker_id>/sticker.png',
        LineStickerAnimatedPngRedirectView.as_view(),
        name="service.linesticker.animated.apng"
    ),
    path('shorturl/', ShortUrlMainView.as_view(), name="service.shorturl"),
]
