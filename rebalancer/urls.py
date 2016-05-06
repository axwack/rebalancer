"""rebalancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import equity.views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', equity.views.home, name='home'),
    url(r'^index/', equity.views.index, name='index'),

    # url(r'^selectModelAccounts/', 'equity.views.selectModelAccounts', name='selectModelAccounts'),

    url(r'^newRebalance/', equity.views.newRebalance, name='newRebalance'),
    url(r'^accountSelections/', equity.views.accountSelections, name='accountSelections'),

    url(r'^accounts/', equity.views.accounts, name='accounts'),
    url(r'^accounts/filter/(?P<id>\d+)/$', equity.views.accountsByFilter, name='accountsByFilter'),
    url(r'^filter/$', equity.views.accountsByFilter, name='accountsByFilter'),

    url(r'^referenceData/', equity.views.referenceData, name='referenceData'),
    url(r'^securities/', equity.views.securities, name='securities'),
    url(r'^rulesCreation/', equity.views.rulesCreation, name='rulesCreation'),
    # url(r'^models/([0-9]+)/$', 'equity.views.updateModelWithTargetWeights', name='models'),

    url(r'^uploadModels/', equity.views.upload, name='file_upload'),
    # You may optionally define a delete url as well
    url(r'^delete/(?P<pk>\d+)$', equity.views.upload_delete, name='file_delete'),

    url(r'^createModelName/$', equity.views.Create_Model_Name, name='createModelName'),

    url(r'^accountParameters/$', equity.views.accountParameters, name='accountParameters'),
    url(r'^accountSearchFilter/$', equity.views.accountSearchFilter, name='accountSearchFilter'),
    url(r'^modelParameters/$', equity.views.modelParameters, name='modelParameters'),
    url(r'^Account/SaveAccount/$', equity.views.save_account_list, name='save_account_list'),
    url(r'^GetAllAccount/$', equity.views.get_account_list, name='get_account_list'),

    url(r'^getClassifications/$', equity.views.getClassifications, name='getClassifications'),
    url(r'^getSavedClassificationModel/(?P<id>\w+)', equity.views.getSavedClassificationModel,
        name='getSavedClassificationModel'),

    url(r'^saveClassifications/$', equity.views.saveClassifications, name='saveClassifications'),
    url(r'^updateSecuritySelectionModels/$', equity.views.updateSecuritySelectionModels,
        name='updateSecuritySelectionModels'),

    url(r'^deleteSecuritySelectionModels/$', equity.views.deleteModel, name='deleteModel'),
    url(r'^deleteSecuritySelectionModels/(?P<id>\w+)/$', equity.views.deleteSecuritySelectionModels,
        name='deleteSecuritySelectionModels'),

    url(r'^updateModelWithSecurity/(?P<id>\w+)/$', equity.views.updateModelWithSecurity,
        name='updateModelWithSecurity'),
    url(r'^updateModelWithTargetWeights/$', equity.views.updateModelWithTargetWeights,
        name='updateModelWithTargetWeights'),
    url(r'^updateModelNodes/$', equity.views.updateModelNodes, name='updateModelNodes'),
    url(r'^uploadSecuritySelectionModels/', equity.views.uploadSecuritySelectionModels,
        name='uploadSecuritySelectionModels'),

    url(r'^getSSMList/$', equity.views.get_SSMList, name='get_SSMList'),

    url(r'^createModelWeights/$', equity.views.createModelWeights, name='createModelWeights'),

    url(r'^getModelTargetWeights/$', equity.views.getModelTargetWeights, name='getModelTargetWeights'),

    url(r'^createSecuritySelectionModels/$', equity.views.createSecuritySelectionModels,
        name='createSecuritySelectionModels'),

    # Registration
    url(r'^Accounts/', include('registration.backends.default.urls')),

    # System Administration
    url(r'^systemFeeds/$', equity.views.systemFeeds, name='systemFeeds'),
    url(r'^editSystemFeeds/$', equity.views.systemFeeds, name='editSystemFeeds'),

]
