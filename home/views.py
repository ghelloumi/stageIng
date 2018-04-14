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

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from utilities_dir.test_ldap import haveLdap
from utilities_dir.test_ldap import haveLdap2


def ldap(request):
    myDict = {}
    for i in haveLdap(request).keys():
        myDict[i] = haveLdap(request)[i][0]
    return myDict


def ldap2(user):
    st = ''
    myDict = {}
    for i in haveLdap2(user).keys():
        myDict[i] = haveLdap2(user)[i][0]
    return myDict


def context_main(request):
    context_main = {
        'login': ldap(request),
        'test': checkAdmin(request),
        'testU': checkUser(request),
        'privileges': checkPrivileges(request),
        'testR': checkReadOnly(request),
    }
    return context_main


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def notfound(request):
    context = {

    }
    context_fin = merge_two_dicts(context_main(request), context)
    return render(request, 'home/notfound.html', context_fin)


##----------------- Index ----------------##
##----------------------------------------##
def index(request):
    context = {
        'problems': len(Problem.objects.all()),
        'projects': len(Project.objects.all()),
        'changes': len(Change.objects.all()),
        'checks': len(Check.objects.all()),
        'admins': len(Admins.objects.all()),
    }
    context_fin = merge_two_dicts(context_main(request), context)
    return render(request, 'home/index.html', context_fin)


##---------------- Admins ----------------##
##----------------------------------------##
def checkAdmin(request):
    a = Admins.objects.filter(userLDAP=ldap(request)['uid'])
    test = False
    if len(a) > 0:
        b = Admins.objects.filter(userLDAP=ldap(request)['uid'])[0].privileges
        if b == 'suser':
            test = True

    return test


def checkReadOnly(request):
    a = Admins.objects.filter(userLDAP=ldap(request)['uid'])
    test = False
    if len(a) > 0:
        b = Admins.objects.filter(userLDAP=ldap(request)['uid'])[0].privileges
        if b == 'ruser':
            test = True
    return test


def checkUser(request):
    a = Admins.objects.filter(userLDAP=ldap(request)['uid'])
    test = False
    if len(a) > 0:
        test = True

    return test


def checkPrivileges(request):
    a = Admins.objects.filter(userLDAP=ldap(request)['uid'])
    if (len(a) > 0):
        b = Admins.objects.filter(userLDAP=ldap(request)['uid'])[0].privileges
    else:
        b = ''
    return b


def context_admins(request):
    a = Admins.objects.all()
    l = []
    for u in range(0, len(a)):
        m = []
        m.append(ldap2(a[u].userLDAP)['uid'])
        m.append(ldap2(a[u].userLDAP)['gecos'].title())
        m.append(ldap2(a[u].userLDAP)['email'])

        if a[u].privileges == 'suser':
            m.append('Admin')
        elif a[u].privileges == 'user':
            m.append('Normal User')
        else:
            m.append('Read Only')

        m.append(Admins.objects.filter(userLDAP=haveLdap2(ldap2(a[u].userLDAP)['uid'])['uid'][0])[0].id)
        l.append(m)
    context_main_admins = {
        'users': l,
        'priv': ['Admin', 'Normal User', 'Read Only'],
        'priv2': ['Admin', 'Normal User'],
    }
    return context_main_admins


def addUsers(request):
    if (not request.POST.get('add_ldap')):

        context = {
        }
        context_fin_admin = merge_two_dicts(context_admins(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_admin)
        return render(request, 'home/admins.html', context_fin)
    else:
        add_ldap_err = ''

        if request.method == "POST":
            add_ldap = request.POST.get('add_ldap')
            if haveLdap2(add_ldap) == 'use not found':
                add_ldap_err = 'Please chose a valid LDAP'
            else:
                test = Admins.objects.filter(userLDAP=haveLdap2(add_ldap)['uid'][0])
                if not len(test) == 0:
                    s = ''
                    if test[0].privileges == 'suser':
                        s = "'Admin'"
                    else:
                        s = "'Normal User'"
                    add_ldap_err = add_ldap + ' already chosen as ' + s

            add_priv = request.POST.get('add_priv')
            if add_priv == '':
                add_priv = 'user'

            if not add_ldap_err:
                a = Admins(userLDAP=add_ldap,
                           privileges=add_priv
                           )
                a.save()

                context = {
                }
                context_fin_admin = merge_two_dicts(context_admins(request), context)
                context_fin = merge_two_dicts(context_main(request), context_fin_admin)
                return render(request, 'home/admins.html', context_fin)
            else:
                context = {
                    'add_ldap_err': add_ldap_err,
                }
                context_fin_admin = merge_two_dicts(context_admins(request), context)
                context_fin = merge_two_dicts(context_main(request), context_fin_admin)
                return render(request, 'home/admins.html', context_fin)


def admins(request):
    context = {
    }
    context_fin_admin = merge_two_dicts(context_admins(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_admin)
    return render(request, 'home/admins.html', context_fin)


def supp_user(request, user_id):
    if checkAdmin(request):
        Admins.objects.filter(id=user_id).delete()
    context = {
    }
    context_fin_admin = merge_two_dicts(context_admins(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_admin)
    return render(request, 'home/admins.html', context_fin)


def change_adminPriv(request, user_id):
    a = Admins.objects.get(id=user_id)

    if a.privileges == 'suser' or a.privileges == 'ruser':
        a.privileges = 'user'
    else:
        a.privileges = 'suser' or a.privileges == 'ruser'
    a.save()
    context = {
    }
    context_fin_admin = merge_two_dicts(context_admins(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_admin)
    return render(request, 'home/admins.html', context_fin)


##---------------- Problem ---------------##
##----------------------------------------##
def context_problems(request):
    ad = Admins.objects.all()
    l = []
    for i in ad:
        l.append(ldap2(i.userLDAP)['givenName'].title())

    context_main_problem = {
        't': [1, 2, 3, 4],
        'status': ["Dev Analysis", "Analysis", "Change", "Dev Fix", "Closed", "Project"],
        'problems': Problem.objects.all(),
        'comments': Comment.objects.all(),
        'admins': l,
    }
    return context_main_problem


def problems(request):
    context = {
    }
    context_fin_problem = merge_two_dicts(context_problems(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_problem)
    return render(request, 'home/problems.html', context_fin)


def comment_list(request):
    if request.method == "POST":
        pbIdC = request.POST.get('pbIdC')
        a = Problem.objects.filter(id=pbIdC)
        context = {
            'a': a[0],
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        return render(request, 'home/problems/comments.html', context_fin)
    else:
        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        return render(request, 'home/problems.html', context_fin)


def get_more_tables(request, problem_id):
    a = Problem.objects.filter(id=problem_id)[0]
    context = {
        'a': a,
    }
    context_fin_problem = merge_two_dicts(context_problems(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_problem)
    return render(request, 'home/get_more_tables.html', context_fin)


def supp_pb(request, problem_id):
    if not checkReadOnly(request) and checkUser(request):
        Problem.objects.filter(id=problem_id).delete()
    context = {
    }
    context_fin_problem = merge_two_dicts(context_problems(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_problem)
    response = render(request, 'home/problems.html', context_fin)
    response['Cache-Control'] = 'no-cache'
    return response


def new_problem(request):
    context = {
    }
    context_fin_problem = merge_two_dicts(context_problems(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_problem)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/problems/new_problem.html', context_fin)
    else:
        return render(request, 'home/problems.html', context_fin)


def add_problem(request):
    if (not request.POST.get('pb_type')):
        context = {
        }
        context_fin = merge_two_dicts(context_main(request), context)
        return render(request, 'home/problems.html', context_fin)
    else:
        pb_desc_err = ''
        test_desc = True

        pb_status_err = ''
        test_status = True

        pb_urgency_err = ''
        test_urgency = True

        pb_importance_err = ''
        test_importance = True

        if request.method == "POST":
            pb_type = request.POST.get('pb_type')
            description = request.POST.get('description')
            if description == '':
                pb_desc_err = 'Please write description'
                test_desc = False

            status = request.POST.get('status')
            if status == '':
                pb_status_err = 'Please chose a status'
                test_status = False

            urgency = request.POST.get('urgency')
            if urgency == '':
                pb_urgency_err = 'Please chose an urgency'
                test_urgency = False

            importance = request.POST.get('importance')
            if importance == '':
                pb_importance_err = 'Please chose an importance'
                test_importance = False

            jira = request.POST.get('jira')
            comment = request.POST.get('comment')

            now = datetime.datetime.utcnow()
            pbID = ''

        if test_desc and test_status and test_urgency and test_importance:
            now = datetime.datetime.utcnow()
            a = Problem.objects.all()
            id = 1
            i = 0
            while i < len(a):
                if id < a[i].id:
                    id = a[i].id
                i = i + 1

            if len(a) == 0:
                pbId = '01'

            else:
                s = 0
                for i in a:
                    if str(i)[5:-3] == now.strftime('%m'):
                        s += 1

                i = 0
                while i < len(a) and str(a[i])[5:-3] == now.strftime('%m'):
                    pbId = str(int(str(a[i])[8:]) + 1)
                    i += 1

            if len(pbId) == 1:
                pbId = '0' + pbId

            # b = Comment(problem_id=id + 1, name=ldap(request)['gecos'].split()[0].title(),
            #             date=now.strftime("%d/%m/%y-%H:%M"),
            #             text=comment)
            # b.save()

            a = Problem(userLDAP=ldap(request)['uidNumber'],
                        problemId='PB-' + now.strftime("%y%m") + '-' + pbId, date=datetime.date.today(),
                        team=pb_type, problemDesc=description,
                        status=status,
                        problemOwner=ldap(request)['givenName'].capitalize(),
                        urgency=urgency, importance=importance,
                        priority=int((2 + int(importance)) * (4 + int(urgency))),
                        jira=jira,
                        lastAction='',
                        lastAction_time=''
                        )
            a.save()
            context = {
            }
            context_fin_problem = merge_two_dicts(context_problems(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_problem)
            return render(request, 'home/problems.html', context_fin)
        else:
            context = {
                'pb_desc_err': pb_desc_err,
                'pb_status_err': pb_status_err,
                'pb_urgency_err': pb_urgency_err,
                'pb_importance_err': pb_importance_err,
                'description': description,
                'pbstatus': status,
                'urgency': urgency,
                'importance': importance,
                'statusList': ["Dev Analysis", "Analysis", "Change", "Dev Fix", "Closed", "Project"],
            }
            context_fin_problem = merge_two_dicts(context_problems(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_problem)
            return render(request, 'home/problems/new_problem.html', context_fin)


def change_pb(request, problem_id):
    if request.method == "POST":
        problemDesc = request.POST.get('problemDesc' + problem_id)
        pb_statue = request.POST.get('pb_statue' + problem_id)
        pb_imp = request.POST.get('pb_imp' + problem_id)
        pb_urgency = request.POST.get('pb_urgency' + problem_id)
        pb_Jira = request.POST.get('pb_Jira' + problem_id)

        a = Problem.objects.get(id=problem_id)
        a.problemDesc = problemDesc
        a.status = pb_statue
        a.importance = pb_imp
        a.urgency = pb_urgency
        a.jira = pb_Jira
        a.priority = (2 + int(pb_imp)) * (4 + int(pb_urgency))

        now = datetime.datetime.utcnow()
        a.save()

        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        response = render(request, 'home/problems.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        response = render(request, 'home/problems.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def add_pb_comment(request, problem_id):
    l = []
    if request.method == "POST":
        a = Problem.objects.get(id=problem_id)
        now = datetime.datetime.utcnow()

        add_pb_commentF = request.POST.get('add_pb_commentF' + problem_id)

        add_to_comment = False;
        c = Comment.objects.filter(problem_id=problem_id).filter(text=add_pb_commentF)

        if len(c) == 0:
            add_to_comment = True

        if add_to_comment:
            b = Comment(problem_id=a.id, name=ldap(request)['gecos'].split()[0].title(),
                        date=now.strftime("%d/%m/%y-%H:%M"),
                        text=add_pb_commentF)
            b.save()

        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        response = render(request, 'home/problems.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        response = render(request, 'home/problems.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def change_pb_owner(request, problem_id):
    if request.method == "POST":
        a = Problem.objects.get(id=problem_id)
        a.problemOwner = request.POST.get('changePbOwnerSelect' + problem_id)
        a.save()

        context = {
        }
        context_fin_problem = merge_two_dicts(context_problems(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_problem)
        return render(request, 'home/problems.html', context_fin)


##--------------- Project ----------------##
##----------------------------------------##
def context_projects(request):
    context_main_project = {
        'projects': Project.objects.all(),
        'teamOpList': ['MarketMap', 'SGN'],
        'typeList': ProjectLists.objects.get(id=1).typeList.split(','),
        'typeOfChangeList': ProjectLists.objects.get(id=1).typeOfChangeList.split(','),
        'areaList': ProjectLists.objects.get(id=1).areaList.split(','),
        'externalConstraintTypeList': ProjectLists.objects.get(id=1).externalConstraintTypeList.split(','),
        'statusList': ProjectLists.objects.get(id=1).statusList.split(','),
        'priorityList': ['Low', 'Medium', 'High', 'Critical'],
        'statusAndCurrentTaskList': StatusAndCurrentTaskList.objects.all(),
        'lists': ProjectLists.objects.get(id=1)
    }
    return context_main_project


def change_projects_lists(request):
    if request.method == "POST":
        typeList = request.POST.get('typeList')
        typeOfChangeList = request.POST.get('typeOfChangeList')
        areaList = request.POST.get('areaList')
        externalConstraintTypeList = request.POST.get('externalConstraintTypeList')
        statusList = request.POST.get('statusList')

        a = ProjectLists.objects.get(id=1)

        a.typeList = typeList
        a.typeOfChangeList = typeOfChangeList
        a.areaList = areaList
        a.externalConstraintTypeList = externalConstraintTypeList
        a.statusList = statusList

        a.save()

        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        return render(request, 'home/projects.html', context_fin)
    else:
        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        return render(request, 'home/projects.html', context_fin)


def change_projects_lists_default(request):
    a = ProjectLists.objects.get(id=1)

    a.typeList = "Client,FIS,FIX,INFRA,LIFECYCLE,MMAP,NORM,SP,XCHG"
    a.typeOfChangeList = "CONF,CONTRACT,DRP SESSION,INFRA,LICENSE,PROGRAM,SOFT,TEST SESSION"
    a.areaList = "APAC,EMEA,LATAM,NORAM,WORLD"
    a.externalConstraintTypeList = "GO LIVE,BIG BANG,BEG // RUN,END // RUN,Internal"
    a.statusList = "NEW,CAB,CLOSED,IN PROGRESS,INFO,ON HOLD,WAIT DEV,WAIT INFRA"

    a.save()

    context = {
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    return render(request, 'home/projects.html', context_fin)


def apply_changes(request):
    context = {
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    return render(request, 'home/projects/apply_changes.html', context_fin)


def projects(request):
    a = ProjectLists.objects.all()
    if len(a) == 0:
        a = ProjectLists(typeList="Client,FIS,FIX,INFRA,LIFECYCLE,MMAP,NORM,SP,XCHG",
                         typeOfChangeList="CONF,CONTRACT,DRP SESSION,INFRA,LICENSE,PROGRAM,SOFT,TEST SESSION",
                         areaList="APAC,EMEA,LATAM,NORAM,WORLD",
                         statusList="NEW,CAB,CLOSED,IN PROGRESS,INFO,ON HOLD,WAIT DEV,WAIT INFRA"
                        )
        a.save()

    context = {
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    return render(request, 'home/projects.html', context_fin)


def comment_list_project(request):
    if request.method == "POST":
        pjIdC = request.POST.get('pjIdC')
        a = Project.objects.filter(id=pjIdC)
        context = {
            'a': a[0],
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        return render(request, 'home/projects/comments.html', context_fin)
    else:
        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        return render(request, 'home/projects.html', context_fin)


def get_more_tables_project(request, project_id):
    a = Project.objects.filter(id=project_id)[0]
    context = {
        'a': a,
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    return render(request, 'home/get_more_tables_project.html', context_fin)


def supp_pj(request, project_id):
    if not checkReadOnly(request) and checkUser(request):
        Project.objects.filter(id=project_id).delete()
    context = {
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    response = render(request, 'home/projects.html', context_fin)
    response['Cache-Control'] = 'no-cache'
    return response


def new_project(request):
    a = Project.objects.all()
    i = 0
    s = []
    while i < len(a):
        if not a[i].projectId in s:
            s.append(a[i].projectId)
        i = i + 1

    context = {
        'a': a,
        's': s,
    }
    context_fin_project = merge_two_dicts(context_projects(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_project)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/projects/new_project.html', context_fin)
    else:
        return render(request, 'home/projects.html', context_fin)


def add_project(request):
    if not request.POST.get('pj_team'):
        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        return render(request, 'home/projects.html', context_fin)
    else:
        pj_teamOp_err = ''
        test_pj_teamOp = True

        pj_projectDescription_err = ''
        test_pj_projectDescription = True

        pj_type_err = ''
        test_pj_type = True

        pj_typeOfChange_err = ''
        test_pj_typeOfChange = True

        pj_accountable_err = ''
        test_pj_accountable = True

        pj_area_err = ''
        test_pj_area = True

        pj_impactScope_err = ''
        test_pj_impactScope = True

        pj_internalTarget_err = ''
        test_pj_internalTarget = True

        pj_externalConstraint_err = ''
        test_pj_externalConstraint = True

        pj_externalConstraintType_err = ''
        test_pj_externalConstraintType = True

        pj_requiredChanges_err = ''
        test_pj_requiredChanges = True

        pj_statusCurrent_err = ''
        test_pj_statusCurrent = True

        if request.method == "POST":
            # Mandatory fields
            pj_team = request.POST.get('pj_team')
            pj_teamOp = request.POST.get('pj_teamOp')
            if pj_teamOp == '':
                pj_teamOp_err = 'Please chose team'
                test_pj_teamOp = False

            pj_id = request.POST.get('project_id')
            pj_projectDescription = request.POST.get('projectDesc')
            if pj_projectDescription == '':
                pj_projectDescription_err = 'Please write description'
                test_pj_projectDescription = False

            pj_type = request.POST.get('type')
            if pj_type == '':
                pj_type_err = 'Please chose a type'
                test_pj_type = False

            pj_typeOfChange = request.POST.get('typeOfChange')
            if pj_typeOfChange == '':
                pj_typeOfChange_err = 'Please chose a type of change'
                test_pj_typeOfChange = False

            pj_accountable = request.POST.get('accountable')
            if pj_accountable == '':
                pj_accountable_err = 'Please write something'
                test_pj_accountable = False

            pj_area = request.POST.get('area')
            if pj_area == '':
                pj_area_err = 'Please chose an area'
                test_pj_area = False

            pj_impactScope = request.POST.get('impactScope')
            if pj_impactScope == '':
                pj_impactScope_err = 'Please write something'
                test_pj_impactScope = False

            pj_internalTarget = request.POST.get('internalTarget')
            if pj_internalTarget == '':
                pj_internalTarget_err = 'Please write something'
                test_pj_internalTarget = False

            pj_externalConstraint = request.POST.get('externalConstraint')
            if pj_externalConstraint == '':
                pj_externalConstraint_err = 'Please chose a date'
                test_pj_externalConstraint = False

            pj_externalConstraintType = request.POST.get('externalConstraintType')
            if pj_externalConstraintType == '':
                pj_externalConstraintType_err = 'Please chose a type'
                test_pj_externalConstraintType = False

            pj_detectionDate = datetime.date.today()

            pj_status = request.POST.get('status')

            pj_requiredChanges = request.POST.get('requiredChanges')
            if pj_requiredChanges == '':
                pj_requiredChanges_err = 'Please chose write something'
                test_pj_requiredChanges = False

            pj_statusCurrent = request.POST.get('statusCurrent')
            if pj_statusCurrent == '':
                pj_statusCurrent_err = 'Please chose write something'
                test_pj_statusCurrent = False

            # Non-Mandatory fiels:
            pj_jira = request.POST.get('jira')
            pj_rca = request.POST.get('rca')
            pj_descriptionNonMandatory = request.POST.get('description')
            pj_impactDate = request.POST.get('impactDate')
            pj_changeImplemDate = request.POST.get('changeImplemDate')
            pj_priority = request.POST.get('priority')
            pj_cib = request.POST.get('cib')
            pj_binaryAvail = request.POST.get('binaryAvail')
            binaryAvailchose = request.POST.get('binaryAvailchose')
            pj_goLiveDate = request.POST.get('goLiveDate')
            pj_externalGoLiveDate = request.POST.get('externalGoLiveDate')
            pj_blockersHighBugs = request.POST.get('blockersHighBugs')
            pj_nbClient = request.POST.get('nbClient')

            now = datetime.datetime.utcnow()
            pjId = ''

            if test_pj_statusCurrent and test_pj_requiredChanges and test_pj_externalConstraintType and test_pj_externalConstraint and test_pj_internalTarget and test_pj_impactScope and test_pj_area and test_pj_accountable and test_pj_typeOfChange and test_pj_type and test_pj_projectDescription:
                if pj_id == 'new':
                    a = Project.objects.all()
                    if len(a) == 0:
                        pjId = '01'

                    else:
                        test = False
                        i = 0
                        while not test and i < len(a):
                            if str(a[i].projectId)[5:-3] == now.strftime('%m'):
                                test = True
                            i = i + 1

                        if test:
                            ch = int(str(a[i - 1].projectId)[8:])
                            j = i
                            while j < len(a):
                                if str(a[j].projectId)[5:-3] == now.strftime('%m'):
                                    if ch < int(str(a[j].projectId)[8:]):
                                        ch = int(str(a[j].projectId)[8:])
                                j = j + 1
                            pjId = str(ch + 1)
                        else:
                            pjId = '01'

                    if len(pjId) == 1:
                        pjId = '0' + pjId

                    pjId = 'PJ-' + now.strftime("%y%m") + '-' + pjId
                else:
                    pjId = pj_id

                a = Project(userLDAP=ldap(request)['uidNumber'],
                            projectId=pjId,
                            detectionDate=pj_detectionDate,
                            pj_team=pj_team,
                            pj_teamOp=pj_teamOp,
                            pj_projectDescription=pj_projectDescription,
                            pj_type=pj_type,
                            pj_typeOfChange=pj_typeOfChange,
                            pj_accountable=pj_accountable,
                            pj_area=pj_area,
                            pj_impactScope=pj_impactScope,
                            pj_internalTarget=pj_internalTarget,
                            pj_externalConstraint=pj_externalConstraint,
                            pj_externalConstraintType=pj_externalConstraintType,
                            pj_status=pj_status,
                            pj_requiredChanges=pj_requiredChanges,
                            pj_jira=pj_jira,
                            pj_rca=pj_rca,
                            pj_descriptionNonMandatory=pj_descriptionNonMandatory,
                            pj_impactDate=pj_impactDate,
                            pj_changeImplemDate=pj_changeImplemDate,
                            pj_priority=pj_priority,
                            pj_cib=pj_cib,
                            pj_binaryAvail=pj_binaryAvail,
                            binaryAvailchose=binaryAvailchose,
                            pj_goLiveDate=pj_goLiveDate,
                            pj_externalGoLiveDate=pj_externalGoLiveDate,
                            pj_blockersHighBugs=pj_blockersHighBugs,
                            pj_nbClient=pj_nbClient
                            )
                a.save()

                now = datetime.datetime.utcnow()
                a = Project.objects.all()
                id = 1
                i = 0
                while i < len(a):
                    if id < a[i].id:
                        id = a[i].id
                    i = i + 1
                date = now.strftime("%d/%m/%y-%H:%M")

                b = StatusAndCurrentTaskList(project_id=id, date=date, text=pj_statusCurrent)
                b.save()

                context = {
                }
                context_fin_project = merge_two_dicts(context_projects(request), context)
                context_fin = merge_two_dicts(context_main(request), context_fin_project)
                return render(request, 'home/projects.html', context_fin)
            else:
                a = Project.objects.all()
                i = 0
                s = []
                while i < len(a):
                    if not a[i].projectId in s:
                        s.append(a[i].projectId)
                    i = i + 1
                context = {
                    'pj_teamOp': pj_teamOp,
                    'pj_projectDescription': pj_projectDescription,
                    'pj_type': pj_type,
                    'pj_typeOfChange': pj_typeOfChange,
                    'pj_accountable': pj_accountable,
                    'pj_area': pj_area,
                    'pj_impactScope': pj_impactScope,
                    'pj_internalTarget': pj_internalTarget,
                    'pj_externalConstraint': pj_externalConstraint,
                    'pj_externalConstraintType': pj_externalConstraintType,

                    'pj_requiredChanges': pj_requiredChanges,
                    'pj_statusCurrent': pj_statusCurrent,

                    'pj_teamOp_err': pj_teamOp_err,
                    'pj_projectDescription_err': pj_projectDescription_err,
                    'pj_type_err': pj_type_err,
                    'pj_typeOfChange_err': pj_typeOfChange_err,
                    'pj_accountable_err': pj_accountable_err,
                    'pj_area_err': pj_area_err,
                    'pj_impactScope_err': pj_impactScope_err,
                    'pj_internalTarget_err': pj_internalTarget_err,
                    'pj_externalConstraint_err': pj_externalConstraint_err,
                    'pj_externalConstraintType_err': pj_externalConstraintType_err,

                    'pj_requiredChanges_err': pj_requiredChanges_err,
                    'pj_statusCurrent_err': pj_statusCurrent_err,

                    's': s,
                    'a': a,
                }
                context_fin_project = merge_two_dicts(context_projects(request), context)
                context_fin = merge_two_dicts(context_main(request), context_fin_project)
                return render(request, 'home/projects/new_project.html', context_fin)
        else:
            a = Project.objects.all()
            i = 0
            s = []
            while i < len(a):
                if not a[i].projectId in s:
                    s.append(a[i].projectId)
                i = i + 1
            context = {
                's': s,
                'a': a,
                'test': checkAdmin(request),
                'testU': checkUser(request)
            }
            context_fin_project = merge_two_dicts(context_projects(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_project)
            return render(request, 'home/projects/new_project.html', context_fin)


def change_pj(request, project_id):
    if request.method == "POST":
        pj_projectDescription = request.POST.get('pj_projectDescription' + project_id)
        pj_type = request.POST.get('pj_type' + project_id)
        pj_typeOfChange = request.POST.get('pj_typeOfChange' + project_id)
        pj_accountable = request.POST.get('pj_accountable' + project_id)
        pj_area = request.POST.get('pj_area' + project_id)
        pj_impactScope = request.POST.get('pj_impactScope' + project_id)
        pj_internalTarget = request.POST.get('pj_internalTarget' + project_id)
        pj_externalConstraint = request.POST.get('pj_externalConstraint' + project_id)
        pj_externalConstraintType = request.POST.get('pj_externalConstraintType' + project_id)
        pj_status = request.POST.get('pj_status' + project_id)
        pj_requiredChanges = request.POST.get('pj_requiredChanges' + project_id)
        pj_jira = request.POST.get('pj_jira' + project_id)
        pj_rca = request.POST.get('pj_rca' + project_id)
        pj_descriptionNonMandatory = request.POST.get('pj_descriptionNonMandatory' + project_id)
        pj_impactDate = request.POST.get('pj_impactDate' + project_id)
        pj_changeImplemDate = request.POST.get('pj_changeImplemDate' + project_id)
        pj_priority = request.POST.get('pj_priority' + project_id)
        pj_cib = request.POST.get('pj_cib' + project_id)
        pj_binaryAvail = request.POST.get('pj_binaryAvail' + project_id)
        pj_goLiveDate = request.POST.get('pj_goLiveDate' + project_id)
        pj_externalGoLiveDate = request.POST.get('pj_externalGoLiveDate' + project_id)
        pj_blockersHighBugs = request.POST.get('pj_blockersHighBugs' + project_id)
        pj_nbClient = request.POST.get('pj_nbClient' + project_id)

        a = Project.objects.get(id=project_id)

        a.pj_projectDescription = pj_projectDescription
        a.pj_type = pj_type
        a.pj_typeOfChange = pj_typeOfChange
        a.pj_accountable = pj_accountable
        a.pj_area = pj_area
        a.pj_impactScope = pj_impactScope
        a.pj_internalTarget = pj_internalTarget
        a.pj_externalConstraint = pj_externalConstraint
        a.pj_externalConstraintType = pj_externalConstraintType
        a.pj_status = pj_status
        a.pj_requiredChanges = pj_requiredChanges
        a.pj_jira = pj_jira
        a.pj_rca = pj_rca
        a.pj_descriptionNonMandatory = pj_descriptionNonMandatory
        a.pj_impactDate = pj_impactDate
        a.pj_changeImplemDate = pj_changeImplemDate
        a.pj_priority = pj_priority
        a.pj_cib = pj_cib
        a.pj_binaryAvail = pj_binaryAvail
        a.pj_goLiveDate = pj_goLiveDate
        a.pj_externalGoLiveDate = pj_externalGoLiveDate
        a.pj_blockersHighBugs = pj_blockersHighBugs
        a.pj_nbClient = pj_nbClient

        a.save()
        a = Project.objects.all()
        context = {
        }

        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        response = render(request, 'home/projects.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        context = {
        }

        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        response = render(request, 'home/projects.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def add_current(request, project_id):
    l = []
    if request.method == "POST":
        a = Project.objects.get(id=project_id)
        now = datetime.datetime.utcnow()

        add_pj_commentF = request.POST.get('add_pj_commentF' + project_id)

        add_to_comment = False;
        c = StatusAndCurrentTaskList.objects.filter(project_id=project_id).filter(text=add_pj_commentF)

        if len(c) == 0:
            add_to_comment = True

        if add_to_comment:
            b = StatusAndCurrentTaskList(project_id=a.id,
                                         date=now.strftime("%d/%m/%y-%H:%M"),
                                         text=add_pj_commentF)
            b.save()

        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        response = render(request, 'home/projects.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        context = {
        }
        context_fin_project = merge_two_dicts(context_projects(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_project)
        response = render(request, 'home/projects.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


##--------------- change -----------------##
##----------------------------------------##
def context_changes(request):
    context_main_change = {
        'changes': Change.objects.all(),
        'admins': Admins.objects.all(),
    }
    return context_main_change


def changes(request):
    context = {
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    return render(request, 'home/changes.html', context_fin)


def supp_ch(request, change_id):
    if not checkReadOnly(request) and checkUser(request):
        Change.objects.filter(id=change_id).delete()

    context = {
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    return render(request, 'home/changes.html', context_fin)


def new_change(request):
    a = Project.objects.filter(pj_teamOp='Ops')
    i = 0
    s = []
    while i < len(a):
        if not a[i].projectId in s:
            s.append(a[i].projectId)
        i = i + 1
    pj_Ops = s

    a = Project.objects.filter(pj_teamOp='SDM')
    i = 0
    s = []
    while i < len(a):
        if not a[i].projectId in s:
            s.append(a[i].projectId)
        i = i + 1
    pj_SDM = s

    change_date = ''
    if request.method == "POST":
        change_date = request.POST.get('change_date')

    context = {
        'pj_Ops': pj_Ops,
        'pj_SDM': pj_SDM,
        'pb': Problem.objects.all(),
        'category': ['Incident', 'Request', 'SR', 'SDM Project', 'Ops Project', 'Problem'],
        'n': change_date,
        'checks': Check.objects.all(),
        'templates': ['License by User', 'License by Exchange', 'Release', 'APS Update', 'Feeds.ini/gltrade.ini',
                      'File.ini'],
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/changes/new_change.html', context_fin)
    else:
        return render(request, 'home/changes.html', context_fin)


def add_change(request):
    if not request.POST.get('ch_team'):
        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        return render(request, 'home/changes.html', context_fin)

    else:
        varList_res = [list(), list(), list(), list(), list(), list()]
        varList_res_req = [list(), list(), list(), list(), list(), list()]

        ch_ref_err = ''
        test_ch_ref = True

        ch_goal_err = ''
        test_ch_goal = True

        ch_server_account_err = ''
        test_ch_server_account = True

        ch_category_err = ''
        test_ch_category = True

        ch_desc_err = ''
        test_ch_desc = True

        ch_file_pushed_err = ''
        test_ch_file_pushed = True

        ch_rollback_file_err = ''
        test_ch_rollback_file = True

        ch_template_err = ''
        test_ch_template = True

        ok = ''

        if request.method == "POST":
            ch_team = request.POST.get('ch_team')

            ch_desc = request.POST.get('ch_desc')
            if ch_desc == '':
                ch_desc_err = 'Please write something'
                test_ch_desc = False

            ch_date = request.POST.get('ch_date')

            ch_category = request.POST.get('ch_category')
            if ch_category == '':
                ch_category_err = 'Please chose category'
                test_ch_category = False

            ch_ref = request.POST.get('ch_ref')
            ch_ref_s = request.POST.get('ch_ref_s')
            ch_ref_sdm = request.POST.get('ch_ref_sdm')
            ch_ref_ops = request.POST.get('ch_ref_ops')
            ch_ref_pb = request.POST.get('ch_ref_pb')

            if not (ch_ref != '' or ch_ref_s != '' or ch_ref_sdm != '' or ch_ref_ops != '' or ch_ref_pb != ''):
                ch_ref_err = 'Please put reference'
                test_ch_ref = False

            ch_goal = request.POST.get('ch_goal')
            if ch_goal == '':
                ch_goal_err = 'Please write a change goal'
                test_ch_goal = False

            ch_server_account = request.POST.get('ch_server_account')
            if ch_server_account == '':
                ch_server_account_err = 'Please put a server/account'
                test_ch_server_account = False

            ch_file_pushed = request.POST.get('ch_file_pushed')
            if ch_file_pushed == '':
                ch_file_pushed_err = 'Please write something'
                test_ch_file_pushed = False

            ch_rollback_file = request.POST.get('ch_rollback_file')
            if ch_rollback_file == '':
                ch_rollback_file_err = 'Please write something'
                test_ch_rollback_file = False

            checkId = request.POST.get('checkId')
            if not checkId:
                checkId = ''
                ok = ''
            else:
                ok = 'ok'

            ch_template = request.POST.get('selectTemplate')
            if ch_template == '':
                ch_template_err = 'Please chose template'
                test_ch_template = False

        chId = ''
        if test_ch_ref and test_ch_goal and test_ch_server_account and test_ch_category and test_ch_desc and test_ch_file_pushed and test_ch_rollback_file and test_ch_template:
            now = datetime.datetime.now()
            a = Change.objects.all()

            # ------ ID gen -----#	2017-08-08  Problem: another day: no increment id
            if ch_date == str(now.strftime("%Y-%m-%d")):
                thisDay = str(now.strftime("%y%m%d"))
            else:
                thisDay = ch_date[2:].replace("-", "")

            if len(a) == 0:
                chId = '01'
            else:
                id = 1
                i = 0
                test = True
                while i < len(a):
                    if str(a[i].changeId)[3:-3] == thisDay:
                        test = False
                        if int(str(a[i].changeId)[10:]) > id:
                            id = int(str(a[i].changeId)[10:])
                    i = i + 1

                if not test:
                    id += 1
                chId = str(id)
                if len(chId) == 1:
                    chId = '0' + chId

            chIdFinal = 'CH-' + thisDay + '-' + chId

            # ------ Change ref gen -----#

            ch_ref_final = ''

            s = [ch_ref_s, ch_ref, ch_ref_sdm, ch_ref_pb, ch_ref_ops]
            for i in s:
                if i != '':
                    ch_ref_final = i

            a = Change(userLDAP=ldap(request)['uidNumber'],
                       changeId=chIdFinal,
                       ch_team=ch_team,
                       ch_desc=ch_desc,
                       ch_date=ch_date,
                       ch_category=ch_category,
                       ch_ref=ch_ref_final,
                       ch_goal=ch_goal,
                       ch_server_account=ch_server_account,
                       ch_owner1=ldap(request)['uid'],
                       ch_owner2='',
                       ch_stat_owner1=ok,
                       ch_stat_owner2='',
                       ch_stat_owner2_comment='',
                       ch_stat_owner2_comment_date='',
                       ch_final_status='',
                       ch_file_pushed=ch_file_pushed,
                       ch_rollback_file=ch_rollback_file,
                       ch_ckId=checkId,
                       ch_template=ch_template,
                       )
            a.save()

            # For template
            s = Change.objects.filter(changeId=chIdFinal)[0].id
            chIdFinal = s
            defineVarList(request, varList_res, varList_res_req, 18, 1)

            defineVarList(request, varList_res, varList_res_req, 8, 2)

            defineVarList(request, varList_res, varList_res_req, 7, 3)

            defineVarList(request, varList_res, varList_res_req, 7, 4)

            defineVarList(request, varList_res, varList_res_req, 13, 5)

            defineVarList(request, varList_res, varList_res_req, 4, 6)

            if ch_template == "License by User":
                toDbVarList(17, 0, ch_template, varList_res, varList_res_req, chIdFinal)
            elif ch_template == "License by Exchange":
                toDbVarList(7, 1, ch_template, varList_res, varList_res_req, chIdFinal)
            elif ch_template == "Release":
                toDbVarList(6, 2, ch_template, varList_res, varList_res_req, chIdFinal)
            elif ch_template == "APS Update":
                toDbVarList(6, 3, ch_template, varList_res, varList_res_req, chIdFinal)
            elif ch_template == "Feeds.ini/gltrade.ini":
                toDbVarList(12, 4, ch_template, varList_res, varList_res_req, chIdFinal)
            elif ch_template == "File.ini":
                toDbVarList(3, 5, ch_template, varList_res, varList_res_req, chIdFinal)

            context = {
            }
            context_fin_change = merge_two_dicts(context_changes(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_change)
            return render(request, 'home/changes.html', context_fin)
        else:
            a = Project.objects.filter(pj_teamOp='Ops')
            i = 0
            s = []
            while i < len(a):
                if not a[i].projectId in s:
                    s.append(a[i].projectId)
                i = i + 1
            pj_Ops = s

            a = Project.objects.filter(pj_teamOp='SDM')
            i = 0
            s = []
            while i < len(a):
                if not a[i].projectId in s:
                    s.append(a[i].projectId)
                i = i + 1
            pj_SDM = s

            context = {
                'ch_category_err': ch_category_err,
                'ch_ref_err': ch_ref_err,
                'ch_goal_err': ch_goal_err,
                'ch_server_account_err': ch_server_account_err,
                'ch_desc_err': ch_desc_err,
                'ch_desc': ch_desc,
                'ch_date': ch_date,
                'ch_category': ch_category,
                'ch_ref': ch_ref,
                'ch_ref_s': ch_ref_s,
                'ch_ref_sdm': ch_ref_sdm,
                'ch_ref_ops': ch_ref_ops,
                'ch_ref_pb': ch_ref_pb,
                'ch_goal': ch_goal,
                'ch_template_err': ch_template_err,
                'ch_template': ch_template,
                'templates': ['License by User', 'License by Exchange', 'Release', 'APS Update',
                              'Feeds.ini/gltrade.ini',
                              'File.ini'],
                'ch_rollback_file_err': ch_rollback_file_err,
                'ch_file_pushed_err': ch_file_pushed_err,
                'ch_file_pushed': ch_file_pushed,
                'ch_rollback_file': ch_rollback_file,
                'ch_server_account': ch_server_account,
                'pj_Ops': pj_Ops,
                'pj_SDM': pj_SDM,
                'pb': Problem.objects.all(),
                'category': ['Incident', 'Request', 'SR', 'SDM Project', 'Ops Project', 'Problem'],
                'checks': Check.objects.all()
            }
            context_fin_change = merge_two_dicts(context_changes(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_change)
            return render(request, 'home/changes/new_change.html', context_fin)


def add_owner2_comment(request, change_id):
    a = Change.objects.get(id=change_id)
    ch_stat_owner2_comment = request.POST.get('ch_stat_owner2_comment' + change_id)
    if not ch_stat_owner2_comment:
        ch_stat_owner2_comment = ''

    a.ch_stat_owner2_comment = ch_stat_owner2_comment
    a.ch_stat_owner2_comment_date = datetime.datetime.utcnow().strftime("%d/%m/%y-%H:%M")

    a.save()
    context = {
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    return render(request, 'home/changes.html', context_fin)


# ---------------- For Owner 1 ------------------#
def change_temp(request, change_id):
    a = Change.objects.filter(id=change_id)
    b = ChangeTemp.objects.filter(change_id=change_id).order_by('id')
    c = Check.objects.all()

    context = {
        'a': a[0],
        'b': b,
        'c': c,
        'templates': ['License by User', 'License by Exchange', 'Release', 'APS Update', 'Feeds.ini/gltrade.ini',
                      'File.ini'],
        'temp3': ['Source SLC/PP', 'MDS Plugin', 'P3', 'NI', 'MDS'],
        'temp6': ['Add', 'Update', 'Remove'],
        'temp5': ['Yes', 'No'],
        'temp51': ['Feed Service', 'Physical Line'],
        'temp4': ['Add', 'Remove'],
        'temp11': ['Realtime', 'Delayed', 'Referential'],
        'temp12': ['Equities> EMEA', 'Equities> AMER', 'Equities> APAC', 'Derivative> EMEA', 'Derivative> AMER',
                   'Derivative> APAC', 'Derivative> 524'],
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/changes/changetemp.html', context_fin)
    else:
        return render(request, 'home/changes.html', context_fin)


def defineVarList(request, varList_res, varList_res_req, max, tempNum):
    for j in range(1, max):
        if (not request.POST.getlist("temp" + str(tempNum) + "_rank" + str(j - 1) + "_res")):
            varList_res[tempNum - 1].append('')
        else:
            r = request.POST.getlist("temp" + str(tempNum) + "_rank" + str(j - 1) + "_res")

            l = ''
            for i in r:
                l = l + i + ','
            l2 = ''
            for i in range(0, len(l) - 1):
                l2 = l2 + l[i]

            varList_res[tempNum - 1].append(l2)
        if (not request.POST.get("temp" + str(tempNum) + "_rank" + str(j - 1) + "_res_req")):
            varList_res_req[tempNum - 1].append('')
        else:
            varList_res_req[tempNum - 1].append(
                request.POST.get("temp" + str(tempNum) + "_rank" + str(j - 1) + "_res_req"))


def toDbVarList(x, y, selectTemplate, varList_res, varList_res_req, change_id):
    for i in range(1, x):
        a = ChangeTemp(change_id=change_id,
                       temp=selectTemplate,
                       rank=i,
                       res=varList_res[y][i],
                       res_req=varList_res_req[y][i],
                       )
        a.save()


def change_temp_add(request, change_id):
    if not request.POST.get("fileToBePushed"):
        context = {
        }
        context_fin = merge_two_dicts(context_main(request), context)
        return render(request, 'home/changes.html', context_fin)
    else:
        ChangeTemp.objects.filter(change_id=change_id).delete()

        varList_res = [list(), list(), list(), list(), list(), list()]
        varList_res_req = [list(), list(), list(), list(), list(), list()]

        if request.method == "POST":
            defineVarList(request, varList_res, varList_res_req, 18, 1)

            defineVarList(request, varList_res, varList_res_req, 8, 2)

            defineVarList(request, varList_res, varList_res_req, 7, 3)

            defineVarList(request, varList_res, varList_res_req, 7, 4)

            defineVarList(request, varList_res, varList_res_req, 13, 5)

            defineVarList(request, varList_res, varList_res_req, 4, 6)

            ch_server_account = request.POST.get("ch_server_account")
            ch_goal = request.POST.get("ch_goal")
            ch_ref = request.POST.get("ch_ref")
            fileToBePushed = request.POST.get("fileToBePushed")
            rollbackFile = request.POST.get("rollbackFile")
            checkCaseID = request.POST.get("checkCaseID")
            selectTemplate = request.POST.get("selectTemplate")
            ch_ckId = request.POST.get("ch_ckId")

            if selectTemplate == "License by User":
                toDbVarList(17, 0, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "License by Exchange":
                toDbVarList(7, 1, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "Release":
                toDbVarList(6, 2, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "APS Update":
                toDbVarList(6, 3, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "Feeds.ini/gltrade.ini":
                toDbVarList(12, 4, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "File.ini":
                toDbVarList(3, 5, selectTemplate, varList_res, varList_res_req, change_id)

            b = Change.objects.filter(id=change_id)[0]
            b.ch_ref = ch_ref
            b.ch_goal = ch_goal
            b.ch_server_account = ch_server_account
            b.ch_file_pushed = fileToBePushed
            b.ch_rollback_file = rollbackFile
            b.checkCaseID = checkCaseID
            if ch_ckId == '':
                b.ch_ckId = ''
                b.ch_stat_owner1 = ''
            else:
                b.ch_ckId = ch_ckId
                b.ch_stat_owner1 = 'ok'

            b.ch_template = selectTemplate
            b.save()

            context = {
            }
            context_fin_change = merge_two_dicts(context_changes(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_change)
            return render(request, 'home/changes.html', context_fin)


# ---------------- For Owner 2 ------------------#
def change_temp2(request, change_id):
    context = {
        'a': Change.objects.filter(id=change_id)[0],
        'b': ChangeTempOwner2.objects.filter(change_id=change_id).order_by('id'),
        'c': Check.objects.all(),
        'templates': ['License by User', 'License by Exchange', 'Release', 'APS Update', 'Feeds.ini/gltrade.ini',
                      'File.ini'],
        'temp3': ['Source SLC/PP', 'MDS Plugin', 'P3', 'NI', 'MDS'],
        'temp6': ['Add', 'Update', 'Remove'],
        'temp5': ['Yes', 'No'],
        'temp51': ['Feed Service', 'Physical Line'],
        'temp4': ['Add', 'Remove'],
        'temp11': ['Realtime', 'Delayed', 'Referential'],
        'temp12': ['Equities> EMEA', 'Equities> AMER', 'Equities> APAC', 'Derivative> EMEA', 'Derivative> AMER',
                   'Derivative> APAC', 'Derivative> 524'],
    }
    context_fin_change = merge_two_dicts(context_changes(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_change)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/changes/changetemp2.html', context_fin)
    else:
        return render(request, 'home/changes.html', context_fin)


def toDbVarList2(x, y, selectTemplate, varList_res, varList_res_req, change_id):
    for i in range(1, x):
        a = ChangeTempOwner2(change_id=change_id,
                             temp=selectTemplate,
                             rank=i,
                             res=varList_res[y][i],
                             res_req=varList_res_req[y][i],
                             )
        a.save()


def change_temp_add2(request, change_id):
    if not request.POST.get("fileToBePushed"):
        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        return render(request, 'home/changes.html', context_fin)
    else:
        ChangeTempOwner2.objects.filter(change_id=change_id).delete()

        varList_res = [list(), list(), list(), list(), list(), list()]
        varList_res_req = [list(), list(), list(), list(), list(), list()]

        if request.method == "POST":
            defineVarList(request, varList_res, varList_res_req, 18, 1)

            defineVarList(request, varList_res, varList_res_req, 8, 2)

            defineVarList(request, varList_res, varList_res_req, 7, 3)

            defineVarList(request, varList_res, varList_res_req, 7, 4)

            defineVarList(request, varList_res, varList_res_req, 13, 5)

            defineVarList(request, varList_res, varList_res_req, 4, 6)

            ch_server_account = request.POST.get("ch_server_account")
            ch_goal = request.POST.get("ch_goal")
            ch_ref = request.POST.get("ch_ref")
            fileToBePushed = request.POST.get("fileToBePushed")
            rollbackFile = request.POST.get("rollbackFile")
            checkCaseID = request.POST.get("checkCaseID")
            selectTemplate = request.POST.get("selectTemplate")
            ch_ckId = request.POST.get("ch_ckId")

            if selectTemplate == "License by User":
                toDbVarList2(17, 0, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "License by Exchange":
                toDbVarList2(7, 1, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "Release":
                toDbVarList2(6, 2, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "APS Update":
                toDbVarList2(6, 3, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "Feeds.ini/gltrade.ini":
                toDbVarList2(12, 4, selectTemplate, varList_res, varList_res_req, change_id)
            elif selectTemplate == "File.ini":
                toDbVarList2(3, 5, selectTemplate, varList_res, varList_res_req, change_id)

            b = Change.objects.filter(id=change_id)[0]
            b.ch_ref = ch_ref
            b.ch_goal = ch_goal
            b.ch_server_account = ch_server_account
            b.ch_file_pushed = fileToBePushed
            b.ch_rollback_file = rollbackFile
            b.checkCaseID = checkCaseID
            b.ch_template = selectTemplate
            b.ch_stat_owner2 = 'ok'
            b.ch_ckId = ch_ckId

            b.save()

            context = {
            }
            context_fin_change = merge_two_dicts(context_changes(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_change)
            return render(request, 'home/changes.html', context_fin)


def add_owner2(request, change_id):
    if request.method == "POST":
        owner2 = request.POST.get('owner2' + change_id)

        a = Change.objects.filter(id=change_id)[0]
        a.ch_owner2 = owner2
        a.save()

        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response

    else:
        context = {
        }

        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def add_stat_owner2(request, change_id):
    if request.method == "POST":
        ch_stat_owner2 = request.POST.get('ch_stat_owner2' + change_id)

        a = Change.objects.filter(id=change_id)[0]
        a.ch_stat_owner2 = ch_stat_owner2
        a.save()

        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response

    else:
        context = {
        }

        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def add_final_status(request, change_id):
    if request.method == "POST":
        ch_final_status = request.POST.get('ch_final_status' + change_id)

        a = Change.objects.filter(id=change_id)[0]
        a.ch_final_status = ch_final_status
        a.ch_final_status_date = datetime.datetime.utcnow().strftime("%d/%m/%y-%H:%M")
        a.save()

        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response

    else:
        context = {
        }
        context_fin_change = merge_two_dicts(context_changes(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_change)
        response = render(request, 'home/changes.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


##--------------- Check ------------------##
##----------------------------------------##
def context_checks(request):
    context_main_check = {
        'checks': Check.objects.all(),
        'changes': Change.objects.all(),
        'checkComments': CheckComment.objects.all()
    }
    return context_main_check


def checks(request):
    context = {
    }
    context_fin_check = merge_two_dicts(context_checks(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_check)
    return render(request, 'home/checks.html', context_fin)


def supp_ck(request, check_id):
    if not checkReadOnly(request) and checkUser(request):
        Check.objects.filter(id=check_id).delete()

    context = {
    }
    context_fin_check = merge_two_dicts(context_checks(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_check)
    return render(request, 'home/checks.html', context_fin)


def new_check(request):
    change_date = ''
    if request.method == "POST":
        change_date = request.POST.get('change_date')
    context = {
    }
    context_fin_check = merge_two_dicts(context_checks(request), context)
    context_fin = merge_two_dicts(context_main(request), context_fin_check)
    if not checkReadOnly(request) and checkUser(request):
        return render(request, 'home/checks/new_check.html', context_fin)
    else:
        return render(request, 'home/checks.html', context_fin)


def add_check(request):
    if not request.POST.get('ck_type'):
        context = {
        }
        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        return render(request, 'home/checks.html', context_fin)

    else:
        if request.method == "POST":
            ch_team = request.POST.get('ck_type')
            ck_category = request.POST.get('ck_category')
            ck_date = request.POST.get('ck_date')
            ck_hour = request.POST.get('ck_hour')

            ck_desc = request.POST.get('ck_desc')
            if not ck_desc:
                ck_desc = ''
            ck_ref_id = request.POST.get('ck_ref_id')
            if not ck_ref_id:
                ck_desc = ''

            ck_date_no_end = request.POST.get('ck_date_no_end')
            if not ck_date_no_end:
                ck_date_no_end = ''

            ck_date_no_end_month = request.POST.get('ck_date_no_end_month')
            if not ck_date_no_end_month:
                ck_date_no_end_month = ''

            ck_date_no_end_day = request.POST.get('ck_date_no_end_day')
            if not ck_date_no_end_day:
                ck_date_no_end_day = ''


            ck_hour_no_end = request.POST.get('ck_hour_no_end')
            if not ck_hour_no_end:
                ck_hour_no_end = ''

            ck_serv_acc = request.POST.get('ck_serv_acc')
            ck_changeId = request.POST.get('ck_changeId')
            ck_title = request.POST.get('ck_title')
            ck_priority = request.POST.get('ck_priority')

            ck_change_performed = request.POST.get('ck_change_performed')
            ck_done = request.POST.get('ck_done')
            ck_action = request.POST.get('ck_action')
            ck_rollback = request.POST.get('ck_rollback')

            # ------ ID gen -----#	2017-08-08  Problem: another day: no increment id
            ckId = ''
            now = datetime.datetime.utcnow()
            a = Check.objects.all()

            thisDay = str(now.strftime("%y%m%d"))

            if len(a) == 0:
                ckId = '01'
            else:
                id = 1
                i = 0
                test = True
                while i < len(a):
                    if str(a[i].checkId)[3:-3] == thisDay:
                        test = False
                        if int(str(a[i].checkId)[10:]) > id:
                            id = int(str(a[i].checkId)[10:])
                    i = i + 1

                if not test:
                    id += 1
                ckId = str(id)
                if len(ckId) == 1:
                    ckId = '0' + ckId

            ckIdFinal = 'CK-' + thisDay + '-' + ckId

            a = Check(userLDAP=ldap(request)['uidNumber'],
                      checkId=ckIdFinal,
                      ck_team=ch_team,
                      ck_category=ck_category,
                      ck_date=ck_date,
                      ck_hour=ck_hour,

                      ck_desc=ck_desc,
                      ck_ref_id=ck_ref_id,
                      ck_date_no_end=ck_date_no_end,
                      ck_date_no_end_month=ck_date_no_end_month,
                      ck_date_no_end_day=ck_date_no_end_day,
                      ck_hour_no_end=ck_hour_no_end,

                      ck_serv_acc=ck_serv_acc,
                      ck_changeId=ck_changeId,
                      ck_title=ck_title,
                      ck_priority=ck_priority,
                      ck_status='Open',

                      ck_change_performed=ck_change_performed,
                      ck_done=ck_done,
                      ck_action=ck_action,
                      ck_rollback=ck_rollback
                      )
            a.save()

            context = {
                'ck_date_no_end_month':ck_date_no_end_month,
            }
            context_fin_check = merge_two_dicts(context_checks(request), context)
            context_fin = merge_two_dicts(context_main(request), context_fin_check)
            return render(request, 'home/checks.html', context_fin)


def change_ck(request, check_id):
    if request.method == "POST":
        ck_category = request.POST.get('ck_category' + check_id)
        ck_date = request.POST.get('ck_date' + check_id)
        ck_hour = request.POST.get('ck_hour' + check_id)
        ck_serv_acc = request.POST.get('ck_serv_acc' + check_id)
        ck_changeId = request.POST.get('ck_changeId' + check_id)
        ck_title = request.POST.get('ck_title' + check_id)
        ck_priority = request.POST.get('ck_priority' + check_id)
        ck_status = request.POST.get('ck_status' + check_id)
        ck_change_performed = request.POST.get('ck_change_performed' + check_id)
        ck_done = request.POST.get('ck_done' + check_id)
        ck_action = request.POST.get('ck_action' + check_id)
        ck_rollback = request.POST.get('ck_rollback' + check_id)

        a = Check.objects.get(id=check_id)
        a.ck_category = ck_category
        a.ck_date = ck_date
        a.ck_hour = ck_hour
        a.ck_serv_acc = ck_serv_acc
        a.ck_changeId = ck_changeId
        a.ck_title = ck_title
        a.ck_priority = ck_priority
        a.ck_status = ck_status
        a.ck_change_performed = ck_change_performed
        a.ck_done = ck_done
        a.ck_action = ck_action
        a.ck_rollback = ck_rollback

        a.save()
        a = Check.objects.all()

        context = {
        }

        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        response = render(request, 'home/checks.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response
    else:
        context = {
        }

        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        response = render(request, 'home/checks.html', context_fin)
        response['Cache-Control'] = 'no-cache'
        return response


def add_comment_check(request, check_id):
    if request.method == "POST":
        now = datetime.datetime.utcnow()
        a = Check.objects.get(id=check_id)

        add_comment_field = request.POST.get('add_comment_field' + check_id)

        add_to_comment = False;
        if not add_to_comment == '':
            add_to_comment = True

        if add_to_comment:
            b = CheckComment(check_id=a.id, name=ldap(request)['gecos'].split()[0].capitalize(),
                             date=now.strftime("%d/%m/%y-%H:%M"),
                             text=add_comment_field)
            b.save()

        context = {
        }
        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        return render(request, 'home/checks.html', context_fin)
    else:
        context = {
        }
        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        return render(request, 'home/checks.html', context_fin)


def change_ck_status(request, check_id):
    if request.method == "POST":
        a = Check.objects.get(id=check_id)

        ck_status = request.POST.get('ck_status' + check_id)

        a.ck_status = ck_status
        a.save()

        context = {
        }
        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        return render(request, 'home/checks.html', context_fin)
    else:
        context = {
        }
        context_fin_check = merge_two_dicts(context_checks(request), context)
        context_fin = merge_two_dicts(context_main(request), context_fin_check)
        return render(request, 'home/checks.html', context_fin)
