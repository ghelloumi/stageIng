from django.contrib import admin
from home.models import Problem
from home.models import Comment
from home.models import Project
from home.models import StatusAndCurrentTaskList
from home.models import Change
from home.models import ChangeTemp
from home.models import Admins
from home.models import Check
from home.models import CheckComment
from home.models import ChangeTempOwner2
from home.models import ProjectLists

admin.site.register(Admins)
admin.site.register(Problem)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(StatusAndCurrentTaskList)
admin.site.register(Change)
admin.site.register(ChangeTemp)
admin.site.register(Check)
admin.site.register(CheckComment)
admin.site.register(ChangeTempOwner2)
admin.site.register(ProjectLists)
