![Ubuntu Build](https://github.com/pastorhudson/ProPresenter-PCO-Live-Auto-Control/actions/workflows/main.yml/badge.svg?branch=main&event=workflow_dispatch&label=ubuntu-build)
![Windows Build](https://github.com/pastorhudson/ProPresenter-PCO-Live-Auto-Control/actions/workflows/main.yml/badge.svg?branch=main&event=workflow_dispatch&label=windows-build)
![macOS Build](https://github.com/pastorhudson/ProPresenter-PCO-Live-Auto-Control/actions/workflows/main.yml/badge.svg?branch=main&event=workflow_dispatch&label=macos-build)
# ProPresenter-PCO-Live-Auto-Control
### What is this?
Planning Center Services has a feature called "Live". This feature lets you click through the items in the plan and the production team can see where they are at in the service flow.
If you use Planning Center Services Live then it will record the actual times on songs and items so next time you use them they will be accurate.
Pro Presenter has the ability to disply Planning Center Live, but you have to manually click next everytime you change songs or slides. This is tedious.

This script watches ProPresenter and automatically advances Planning Center Live status when the item is changed in ProPresenter.

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

### Quick Start
- Add your Planning Center API Keys to config.ini
- Enable Network under ProPresenter Preferences / Network. Note the Port Number and IP or use the defaults.
- Run PcoLive
- Select the service type
- Select the plan
- The program will sync Services Live according to the current ProPresenter item until you close it.

---

## Command-Line Options

This utility provides several options for interacting with the PCO Live service. You can use these options to perform various operations like testing the utility, specifying a service type ID, or a plan ID.

### Usage

```bash
PcoLive [options]
```

### Options

- `-t`, `--test`  
  **Description:** Enables the test mode.  
  **Behavior:** Returns the string 'SUCCESS' and exits.  
  **Example:** `python main.py --test`

- `-s`, `--service_type_id` SERVICE_TYPE_ID  
  **Description:** Specifies the service type ID.  
  **Details:** The service type ID is used to identify a specific type of service in the PCO Live system. If you use service type ID without specifying plan ID you will be prompted to choose a plan from a list.
  **Example:** `python main.py --service_type_id 12345`

- `-p`, `--plan_id` PLAN_ID  
  **Description:** Specifies the plan ID.  
  **Details:** The plan ID is used to identify a specific plan within a service type in the PCO Live system. You must specify a service type ID if you are specifying a plan ID.
  **Example:** `python main.py --service_type_id 12345 --plan_id 67890`

### Examples

1. **Run in Test Mode:**  
   ```bash
   PcoLive --test
   ```

2. **Specify Both Service Type and Plan IDs:**  
   ```bash
   PcoLive --service_type_id 12345 --plan_id 67890
   ```

3. **Specify Only Service Type ID (with plan selection happening interactively):**  
   ```bash
   PcoLive --service_type_id 12345
   ```

4. **Specify Only Plan ID (with service type selection happening interactively):**  
   ```bash
   PcoLive --plan_id 67890
   ```

### Notes

- If no arguments are provided, the utility will prompt for service type and plan selections interactively.
- In case of any issues with Planning Center API keys, ensure they are correctly set in the `config.ini`.
- This program is free. Use at your own risk.
- This program assumes you have some technical ability to configure and run a command line program.

---

### About Me

I'm a pastor in south west PA who likes to build stuff. I run a website called https://pcochef.com full of "recipes for doing ministry" with Planning Center.