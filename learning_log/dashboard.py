from controlcenter import Dashboard, widgets
from learning_logs.models import *

class ModelItemList(widgets.ItemList):
    model = Topic
    list_display = ('pk', 'field')

class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )
