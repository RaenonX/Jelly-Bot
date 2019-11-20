from django.urls import path

from .code import (
    InsertOutcomeCodeView, GetOutcomeCodeView, OperationOutcomeCodeView, UpdateOutcomeCodeView,
    APIActionCodeView, ExecodeCodeView
)
from .terms import TermsExplanationView
from .botcmd import BotCommandMainView, BotCommandHelpView, BotOldCommandMainView, BotOldCommandHelpView

urlpatterns = [
    path('terms/', TermsExplanationView.as_view(), name="page.doc.terms"),
    path('outcome/insert/', InsertOutcomeCodeView.as_view(), name="page.doc.code.insert"),
    path('outcome/get/', GetOutcomeCodeView.as_view(), name="page.doc.code.get"),
    path('outcome/operation/', OperationOutcomeCodeView.as_view(), name="page.doc.code.ops"),
    path('outcome/update/', UpdateOutcomeCodeView.as_view(), name="page.doc.code.update"),
    path('action/api/', APIActionCodeView.as_view(), name="page.doc.code.api"),
    path('action/execode/', ExecodeCodeView.as_view(), name="page.doc.code.excde"),
    path('botcmd/', BotCommandMainView.as_view(), name="page.doc.botcmd.main"),
    path('botcmd/<str:code>/', BotCommandHelpView.as_view(), name="page.doc.botcmd.cmd"),
    path('botcmd-old/', BotOldCommandMainView.as_view(), name="page.doc.botcmd.main.old"),
    path('botcmd-old/<str:code>/', BotOldCommandHelpView.as_view(), name="page.doc.botcmd.cmd.old")
]
