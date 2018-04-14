#!/usr/bin/python
from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^notfound/*$', views.notfound, name='notfound'),

    url(r'^admins/*$', views.admins, name='admins'),
    url(r'^admins/addUsers/*$', views.addUsers, name='addUsers'),
    url(r'^admins/supp_user/(?P<user_id>[0-9]+)/*$', views.supp_user, name='supp_user'),
    url(r'^admins/change_adminPriv/(?P<user_id>[0-9]+)/*$', views.change_adminPriv, name='change_adminPriv'),

    url(r'^problems/*$', views.problems, name='problems'),
    url(r'^problems/get_more_tables/(?P<problem_id>[0-9]+)/*$', views.get_more_tables, name='get_more_tables'),
    url(r'^problems/comment_list/*$', views.comment_list, name='comment_list'),
    url(r'^problems/supp_pb/(?P<problem_id>[0-9]+)/*$', views.supp_pb, name='supp_pb'),
    url(r'^problems/new/*$', views.new_problem, name='new_problem'),
    url(r'^problems/new/add_problem/*$', views.add_problem, name='add_problem'),
    url(r'^problems/change_pb/(?P<problem_id>[0-9]+)/*$', views.change_pb, name='change_pb'),
    url(r'^problems/add_pb_comment/(?P<problem_id>[0-9]+)/*$', views.add_pb_comment, name='add_pb_comment'),
    url(r'^problems/change_pb_owner/(?P<problem_id>[0-9]+)/*$', views.change_pb_owner, name='change_pb_owner'),

    url(r'^projects/*$', views.projects, name='projects'),
    url(r'^projects/comment_list_project/*$', views.comment_list_project, name='comment_list_project'),
    url(r'^projects/get_more_tables_project/(?P<project_id>[0-9]+)/*$', views.get_more_tables_project, name='get_more_tables_project'),
    url(r'^projects/supp_pj/(?P<project_id>[0-9]+)/*$', views.supp_pj, name='supp_pj'),
    url(r'^projects/new/*$', views.new_project, name='new_project'),
    url(r'^projects/new/add_project/*$', views.add_project, name='add_project'),
    url(r'^projects/change_pj/(?P<project_id>[0-9]+)/*$', views.change_pj, name='change_pj'),
    url(r'^projects/add_current/(?P<project_id>[0-9]+)/*$', views.add_current, name='add_current'),
    url(r'^projects/change_projects_lists/*$', views.change_projects_lists, name='change_projects_lists'),
    url(r'^projects/change_projects_lists_default/*$', views.change_projects_lists_default, name='change_projects_lists_default'),
    url(r'^projects/apply_changes/*$', views.apply_changes, name='apply_changes'),
    url(r'^projects/new/apply_changes/*$', views.apply_changes, name='apply_changes'),

    url(r'^changes/*$', views.changes, name='changes'),
    url(r'^changes/new/*$', views.new_change, name='new_change'),
    url(r'^changes/supp_ch/(?P<change_id>[0-9]+)/*$', views.supp_ch, name='supp_ch'),
    url(r'^changes/new/add_change/*$', views.add_change, name='add_change'),
    url(r'^changes/change_temp/(?P<change_id>[0-9]+)/*$', views.change_temp, name='change_temp'),
    url(r'^changes/change_temp2/(?P<change_id>[0-9]+)/*$', views.change_temp2, name='change_temp2'),
    url(r'^changes/change_temp/change_temp_add/(?P<change_id>[0-9]+)/*$', views.change_temp_add, name='change_temp_add'),
    url(r'^changes/change_temp2/change_temp_add2/(?P<change_id>[0-9]+)/*$', views.change_temp_add2, name='change_temp_add2'),
    url(r'^changes/add_owner2/(?P<change_id>[0-9]+)/*$', views.add_owner2, name='add_owner2'),
    url(r'^changes/add_stat_owner2/(?P<change_id>[0-9]+)/*$', views.add_stat_owner2, name='add_stat_owner2'),
    url(r'^changes/add_final_status/(?P<change_id>[0-9]+)/*$', views.add_final_status, name='add_final_status'),
    url(r'^changes/add_owner2_comment/(?P<change_id>[0-9]+)/*$', views.add_owner2_comment, name='add_owner2_comment'),

    url(r'^checks/*$', views.checks, name='checks'),
    url(r'^checks/new/*$', views.new_check, name='new_check'),
    url(r'^changes/supp_ck/(?P<check_id>[0-9]+)/*$', views.supp_ck, name='supp_ck'),
    url(r'^checks/new/add_check/*$', views.add_check, name='add_check'),
    url(r'^checks/change_ck/(?P<check_id>[0-9]+)/*$', views.change_ck, name='change_ck'),
    url(r'^projects/add_comment_check/(?P<check_id>[0-9]+)/*$', views.add_comment_check, name='add_comment_check'),
    url(r'^projects/change_ck_status/(?P<check_id>[0-9]+)/*$', views.change_ck_status, name='change_ck_status'),

    url(r'^ldap/*$', views.ldap, name='ldap'),
]
