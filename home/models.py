from django.db import models
from django.core.urlresolvers import reverse


class Admins(models.Model):
    userLDAP = models.CharField(max_length=30)
    privileges = models.CharField(max_length=100)


class Problem(models.Model):
    userLDAP = models.CharField(max_length=30)
    problemId = models.CharField(max_length=15)
    date = models.CharField(max_length=20)
    team = models.CharField(max_length=15)
    problemDesc = models.CharField(max_length=1500)
    status = models.CharField(max_length=15)
    problemOwner = models.CharField(max_length=50)
    urgency = models.CharField(max_length=10)
    importance = models.CharField(max_length=10)
    priority = models.CharField(max_length=10)
    jira = models.CharField(max_length=500)
    lastAction = models.CharField(max_length=1500)
    lastAction_time = models.CharField(max_length=200)

    def __str__(self):
        return self.problemId


class Comment(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    text = models.CharField(max_length=1500)


class Project(models.Model):
    userLDAP = models.CharField(max_length=30)
    projectId = models.CharField(max_length=15)
    detectionDate = models.CharField(max_length=20)
    pj_team = models.CharField(max_length=20)
    pj_teamOp = models.CharField(max_length=20)
    pj_projectDescription = models.CharField(max_length=2000)
    pj_type = models.CharField(max_length=20)
    pj_typeOfChange = models.CharField(max_length=20)
    pj_accountable = models.CharField(max_length=200)
    pj_area = models.CharField(max_length=20)
    pj_impactScope = models.CharField(max_length=200)
    pj_internalTarget = models.CharField(max_length=200)
    pj_externalConstraint = models.CharField(max_length=200)
    pj_externalConstraintType = models.CharField(max_length=100)
    pj_status = models.CharField(max_length=20)
    pj_requiredChanges = models.CharField(max_length=2000)
    pj_jira = models.CharField(max_length=1000)
    pj_rca = models.CharField(max_length=1000)
    pj_descriptionNonMandatory = models.CharField(max_length=2000)
    pj_impactDate = models.CharField(max_length=20)
    pj_changeImplemDate = models.CharField(max_length=20)
    pj_priority = models.CharField(max_length=20)
    pj_cib = models.CharField(max_length=20)
    pj_binaryAvail = models.CharField(max_length=20)
    binaryAvailchose = models.CharField(max_length=20)
    pj_goLiveDate = models.CharField(max_length=20)
    pj_externalGoLiveDate = models.CharField(max_length=20)
    pj_blockersHighBugs = models.CharField(max_length=200)
    pj_nbClient = models.CharField(max_length=200)

class ProjectLists(models.Model):
    typeList = models.CharField(max_length=2000)
    typeOfChangeList = models.CharField(max_length=2000)
    areaList = models.CharField(max_length=2000)
    externalConstraintTypeList = models.CharField(max_length=2000)
    statusList = models.CharField(max_length=2000)


class StatusAndCurrentTaskList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.CharField(max_length=30)
    text = models.CharField(max_length=3000)


class Change(models.Model):
    userLDAP = models.CharField(max_length=30)
    changeId = models.CharField(max_length=15)
    ch_team = models.CharField(max_length=50)
    ch_desc = models.CharField(max_length=1500)
    ch_date = models.CharField(max_length=20)
    ch_category = models.CharField(max_length=50)
    ch_ref = models.CharField(max_length=200)
    ch_goal = models.CharField(max_length=200)
    ch_server_account = models.CharField(max_length=200)
    ch_owner1 = models.CharField(max_length=200)
    ch_owner2 = models.CharField(max_length=200)
    ch_stat_owner1 = models.CharField(max_length=200)
    ch_stat_owner2 = models.CharField(max_length=200)
    ch_stat_owner2_comment = models.CharField(max_length=200)
    ch_stat_owner2_comment_date = models.CharField(max_length=200)
    ch_final_status = models.CharField(max_length=200)
    ch_final_status_date = models.CharField(max_length=200)
    ch_file_pushed = models.CharField(max_length=200)
    ch_rollback_file = models.CharField(max_length=200)
    ch_ckId = models.CharField(max_length=200)
    ch_template = models.CharField(max_length=200)


class ChangeTemp(models.Model):
    change = models.ForeignKey(Change, on_delete=models.CASCADE)
    temp = models.CharField(max_length=100)
    rank = models.CharField(max_length=15)
    res = models.CharField(max_length=100)
    res_req = models.CharField(max_length=200)

class ChangeTempOwner2(models.Model):
    change = models.ForeignKey(Change, on_delete=models.CASCADE)
    temp = models.CharField(max_length=100)
    rank = models.CharField(max_length=15)
    res = models.CharField(max_length=100)
    res_req = models.CharField(max_length=200)


class Check(models.Model):
    userLDAP = models.CharField(max_length=30)
    checkId = models.CharField(max_length=15)
    ck_team = models.CharField(max_length=50)
    ck_category = models.CharField(max_length=200)
    ck_date = models.CharField(max_length=200)
    ck_hour = models.CharField(max_length=200)

    ck_desc = models.CharField(max_length=200)
    ck_ref_id = models.CharField(max_length=200)
    ck_date_no_end = models.CharField(max_length=200)
    ck_date_no_end_month = models.CharField(max_length=200)
    ck_date_no_end_day = models.CharField(max_length=200)
    ck_hour_no_end = models.CharField(max_length=200)

    ck_serv_acc = models.CharField(max_length=200)
    ck_changeId = models.CharField(max_length=200)
    ck_title = models.CharField(max_length=200)
    ck_priority = models.CharField(max_length=200)
    ck_status = models.CharField(max_length=200)
    ck_change_performed = models.CharField(max_length=200)
    ck_done = models.CharField(max_length=200)
    ck_action = models.CharField(max_length=200)
    ck_rollback = models.CharField(max_length=200)

class CheckComment(models.Model):
    checkC = models.ForeignKey(Check, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    text = models.CharField(max_length=1500)