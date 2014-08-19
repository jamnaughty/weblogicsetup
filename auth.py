connect('weblogic','weblogic12','t3://127.0.0.1:7001')
edit()
startEdit(-1,-1,'false')
cmo.getSecurityConfiguration().getDefaultRealm().createAuthenticationProvider('ADAuthenticator', 'weblogic.security.providers.authentication.ActiveDirectoryAuthenticator')
cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('ADAuthenticator').setControlFlag('OPTIONAL')
cd('/SecurityConfiguration')
cd('dev6ExternalWLS')
cd('Realms/myrealm/AuthenticationProviders')
cd('ADAuthenticator')
cmo.setGroupBaseDN('CN=Users,DC=faisal,DC=bea,DC=com')
cmo.setUserBaseDN('CN=Users,DC=faisal,DC=bea,DC=com')
cmo.setAllGroupsFilter('(objectclass=group)')
cmo.setPrincipal('CN=Administrator,CN=Users,DC=faisal,DC=bea,DC=com')
cmo.setCredential('Passw0rd')
cmo.setPort(389)
cmo.setHost('127.0.0.1')
save()
activate()
