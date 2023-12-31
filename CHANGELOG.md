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

## v1.1.0
### Changes
 - Added Mac build targeting python 3.8.10
 - Added rudimentary test on build to ensure the binary works before triggering a release

## v1.1.1
### Changes
 - Changed Mac Build to target Python 3.12
 - This is tested and working on Ventura 13.5 on M2 mac.
 - Note: OSx will complain when you download the zip. You have to right-click `PcoLive` and select `open` the first time you run it.
 - Changed the log file from .log to .txt for clarity

## v1.1.2
### Changes
- Added ability to specify only service type id at command line and select plan id interactively
- Added commandline options to Readme
- Updated README with command line options

## v1.1.3
### Changes
- Security Fix

## v1.1.4
### Changes
- Added PcoLive.sh to Mac and Linux release. PcoLive.sh will download source and build python virtual environment and run the python script on most Linux environments. This is useful for when the binary files don't work on your environment. Or for use in automations like Node-Red.
- The same command line options work with PcoLive.sh as the regular python script.
- Added `-p next` option. When a service type is specified `-p next` will automatically pick the next plan for that service type.

## v1.1.5
### Changes
- Changed the way PcoLive.sh finds the directory to be compatible with busybox environments.

## v1.1.6
### Changes
- Fixed a bug that occurred when dragging media onto a planning center item.