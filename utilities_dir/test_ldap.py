#!/usr/bin/python


def haveLdap(request):
    str = (
                               {
                                               'shadowExpire': ['1505814662'],
                                               'uid': ['ism'],
                                               'cisco-avpair': ['shell:priv-lvl=1'],
                                               'objectClass': ['organizationalPerson', 'shadowAccount', 'entrustNamedObject', 'posixAccount', 'openradiusUser', 'person', 'emailAddressUser'],
                                               'loginShell': ['/bin/bash'],
                                               'shadowWarning': ['1296000'],
                                               'uidNumber': ['7644'],
                                               'l': ['Tunis'],
                                               'shadowMax': ['6480000'],
                                               'radiusIdleTimeout': ['300'],
                                               'gidNumber': ['1102'],
                                               'gecos': ['Ismail Elloumi'],
                                               'sn': ['Elloumi'],
                                               'radiusServiceType': ['Login'],
                                               'homeDirectory': ['/export/home/gei'],
                                               'juniper-localUserName': ['juniper-unauthorized'],
                                               'givenName': ['Ismail'],
                                               'shadowLastChange': ['1499334662'],
                                               'email': ['Ismail.Elloumi@fisglobal.com'],
                                               'cn': ['ghassen elloumi']
                               }
    )
    return str


def haveLdap2(user):
    str = (
                               {
                                               'shadowExpire': ['1505814662'],
                                               'uid': ['gei'],
                                               'cisco-avpair': ['shell:priv-lvl=1'],
                                               'objectClass': ['organizationalPerson', 'shadowAccount', 'entrustNamedObject', 'posixAccount', 'openradiusUser', 'person', 'emailAddressUser'],
                                               'loginShell': ['/bin/bash'],
                                               'shadowWarning': ['1296000'],
                                               'uidNumber': ['7644'],
                                               'l': ['Tunis'],
                                               'shadowMax': ['6480000'],
                                               'radiusIdleTimeout': ['300'],
                                               'gidNumber': ['1102'],
                                               'gecos': ['Ghassen Elloumi'],
                                               'sn': ['Elloumi'],
                                               'radiusServiceType': ['Login'],
                                               'homeDirectory': ['/export/home/gei'],
                                               'juniper-localUserName': ['juniper-unauthorized'],
                                               'givenName': ['Ghassen'],
                                               'shadowLastChange': ['1499334662'],
                                               'email': ['Ghassen.Elloumi@fisglobal.com'],
                                               'cn': ['ghassen elloumi']
                               }
    )
    return str


