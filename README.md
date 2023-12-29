
# ProPresenter-PCO-Live-Auto-Control
Auto advance Planning Center Services Live based on ProPresenter action

### Setup

- Go to https://api.planningcenteronline.com
- Create a Personal Access Token. You must have access to control Services Live in Planning Center Services for this to work
- Edit the config.ini

```editorconfig
[app]
;Get your Planning Center application_id and secret at https://api.planningcenteronline.com/oauth/applications
application_id = pco_app_id
secret = pco_app_secret
;Default is localhost 127.0.0.1 this is for running the program on the same machine as ProPresenter
pro_presenter_ip = 127.0.0.1
pro_presenter_port = 50001
```

- Run pco_live_control.exe on windows or pco_live_control on mac
- Select the service type
- Select the plan
