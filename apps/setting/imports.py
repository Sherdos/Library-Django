from apps.setting.models import Setting


class All():
    setting = Setting.objects.latest('id')