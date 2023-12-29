# Changelog
All notable changes to this project will be documented in this file.

## v1.0.0
### Changes
 - First Release

## v1.0.1
### Changes
 - Added the -t --test option to test if the executable works
 - Added the -s --service_type_id option to skip the interactive chooser this has to be used with -p
 - Added the -p --plan_id option to skip the interactive chooser this has to be used with -s
 - Default still shows an interactive service/plan chooser.
 - If you want to skip the interactive service/plan chooser you must specify both planning center service type id and planning center plan id.
 - You can get the service_type_id and plan_id from the url in planning center. When you have a plan loaded the plan_id is in the url.
 - If you click on the service type in the top right of the plan screen then the service_type_id will be in the url.
 - You can also run the program and select the service type and plan and the corresponding ID's will be shown.
 - The service type will probably stay the same from week to week, but the plan_id will always change.

## v1.0.2
### Changes
 - Added descriptive error when the Planning Center API keys are not working.
 - Added Readme, Liscence, and Changelog to the release downloads
 - Changed folder from dist to PcoLive for the release archives
