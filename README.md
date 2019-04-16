
#OUTSETTINGSVALUES [![Build Status](https://travis-ci.org/raccoongang/outsettingsvalues.svg?branch=master.svg?branch=dev_custome)](https://travis-ci.org/raccoongang/outsettingsvalues.svg?branch=master)

This package print django settings from your project.

##Dependencies

This tool compartible with Django 1.11.

##Installation

Use command:

```console
pip install -e git+ssh://git@github.com:raccoongang/outsettingsvalues.git@master#egg=outsettingsvalues
```

Next add 'outsettingsvalues' to INSTALLED_APPS in your settings file and add

    urlpatterns += [
        url(r'^settingsvars/$', include('outsettingsvalues.urls'))
    ] 
to urls.py file in your django project directory. 

##URL

This tool can be browsed from the host and port of your project and /settings url. 
For example http://localhost:18000/settingsvars.






