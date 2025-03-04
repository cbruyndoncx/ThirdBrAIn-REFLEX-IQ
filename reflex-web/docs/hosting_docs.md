Project Path: hosting

Source Tree:

```
hosting
├── config_file.md
├── custom-domains.md
├── deploy-with-github-actions.md
├── billing.md
├── compute.md
├── adding-members.md
├── logs.md
├── app-management.md
├── tokens.md
├── deploy-quick-start.md
├── machine-types.md
├── secrets-environment-vars.md
├── regions.md
├── reflex-branding.md
└── self-hosting.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/config_file.md`:

```md
## Config File

To create a `config.yml` file for your app run the command below:

```bash
reflex cloud config
```

This will create a yaml file similar to the one below where you can edit the app configuration:

```yaml
name: medo
description: ''
regions:
  sjc: 1
  lhr: 2
vmtype: c1m1
hostname: null
envfile: .env
project: null
packages:
- procps
```


```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/custom-domains.md`:

```md

# Custom Domains


With the Pro tier of Reflex Cloud you can use your own custom domain to host your app. 

## Prerequisites

You must purchase a domain from a domain registrar such as GoDaddy, Cloudflare, Namecheap, or AWS. 

For this tutorial we will use GoDaddy and the example domain `tomgotsman.us`.


## Steps

Once you have purchased your domain, you can add it to your Reflex Cloud app by following these steps:

1 - Ensure you have deployed your app to Reflex Cloud.

2 - Once your app is deployed click the `Custom Domain` tab and add your custom domain to the input field and press the Add domain button. You should now see a page like below:

```python eval
image_zoom(rx.image(src="/custom-domains-DNS-inputs.png"))
```

```python eval
rx.box(height="20px")
```

3 - On the domain registrar's website, navigate to the DNS settings for your domain. It should look something like the image below:

```python eval
image_zoom(rx.image(src="/custom-domains-DNS-before.png"))
```

```python eval
rx.box(height="20px")
```

4 - Add all four of the DNS records provided by Reflex Cloud to your domain registrar's DNS settings. If there is already an A name record, delete it and replace it with the one provided by Reflex Cloud. Your DNS settings should look like the image below:

```python eval
image_zoom(rx.image(src="/custom-domains-DNS-after.png"))
```

```md alert warning
# It may alert you that this record will resolve on ######.tomgotsman.us.tomgotsman.us.
If this happens ensure that you select to only have the record resolve on ######.tomgotsman.us.
```

```md alert warning
# Your domain provider may not support an Apex CNAME record, in this case just use an A record.
![Image showing failed CNAME record](/custom-domains-CNAME-fail.png)
```

```python eval
rx.box(height="20px")
```

5 - Once you have added the DNS records, refresh the page on the Reflex Cloud page (it may take a few minutes to a few hours to update successfully). If the records are correct, you should see a success message like the one below:

```python eval
image_zoom(rx.image(src="/custom-domains-success.png"))
```

```python eval
rx.box(height="20px")
```

6 - Now redeploy your app using the `reflex deploy` command and your app should now be live on your custom domain!
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/deploy-with-github-actions.md`:

```md

# Deploy with Github Actions

This GitHub Action simplifies the deployment of Reflex applications to Reflex Cloud. It handles setting up the environment, installing the Reflex CLI, and deploying your app with minimal configuration.

```md alert info
# This action requires `reflex>=0.6.6`
```

**Features:**
- Deploy Reflex apps directly from your GitHub repository to Reflex Cloud.
- Supports subdirectory-based app structures.
- Securely uses authentication tokens via GitHub Secrets.

## Usage
### Add the Action to Your Workflow
Create a `.github/workflows/deploy.yml` file in your repository and add the following:

```yaml
name: Deploy Reflex App

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Reflex Cloud
        uses: reflex-dev/reflex-deploy-action@v1
        with:
          auth_token: ${\{ secrets.REFLEX_PROJECT_ID }}
          project_id: ${\{ secrets.REFLEX_PROJECT_ID }}
          app_directory: "my-app-folder" # Optional, defaults to root
          extra_args: "--env THIRD_PARTY_APIKEY=***" # Optional
          python_version: "3.12" # Optional
```

### Set Up Your Secrets
Store your Reflex authentication token securely in your repository's secrets:


1. Go to your GitHub repository.
2. Navigate to Settings > Secrets and variables > Actions > New repository secret.
3. Create new secrets for `REFLEX_AUTH_TOKEN` and `REFLEX_PROJECT_ID`. 

(Create a `REFLEX_AUTH_TOKEN` in the tokens tab of your UI, check out these [docs]({docs.hosting.tokens.path}#tokens). 

The `REFLEX_PROJECT_ID` can be found in the UI when you click on the How to deploy button on the top right when inside a project and copy the ID after the `--project` flag.)



### Inputs

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Name"),
            rx.table.column_header_cell("Description"),
            rx.table.column_header_cell("required"),
            rx.table.column_header_cell("Default"),
        ),
    ),
    rx.table.body(
        *[
            rx.table.row(
                rx.table.cell(rx.code(github_config["name"], style=get_code_style("violet"))),
                rx.table.cell(github_config["description"], style=cell_style),
                rx.table.cell(rx.code(github_config["required"], style=get_code_style("violet"))),
                rx.table.cell(rx.code(github_config["default"], style=get_code_style("violet")), min_width="100px"),
            )
            for github_config in github_actions_configs
        ]
    ),
    variant="surface",
)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/billing.md`:

```md

## Overview 

Billing for Reflex Cloud is monthly per project. Project owners and admins are able to view and manage the billing page. 

The billing for a project is comprised of two parts - number of `seats` and `compute`. 

## Seats

Projects on a paid plan can invite collaborators to join their project. 

Each additional collaborator is considered a `seat` and is charged on a flat monthly rate. Project owners and admins can manage permissions and roles for each seat in the settings tab on the project page. 

## Compute

Reflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. 

For more information on compute pricing, please see the [compute]({hosting.compute.path}) page.

## Manage Billing

To manage your billing, you can go to the `Billing` tab in the Cloud UI on the project page.

## Setting Billing Limits

If you want to set a billing limit for your project, you can do so by going to the `Billing` tab in the Cloud UI on the project page.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/compute.md`:

```md

## Compute Usage

Reflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. 

This allows you to deploy your app on larger sizes and multiple regions without worrying about paying for idle compute. We bill on a per second basis so you only pay for the compute you use.

By default your app stays alive for 5 minutes after the no users are connected. After this time your app will be considered idle and you will not be charged. Start up times usually take less than 1 second for you apps to come back online.

#### Warm vs Cold Start
- Apps below `c2m2` are considered warm starts and are usually less than 1 second.
- If your app is larger than `c2m2` it will be a cold start which takes around 15 seconds. If you want to avoid this you can reserve a machine.

## Compute Pricing Table

```python eval
compute_table_base()
```

## Reserved Machines (Coming Soon)

If you expect your apps to be continuously receiving users, you may want to reserve a machine instead of having us manage your compute. 

This will be a flat monthly rate for the machine.

## Monitoring Usage

To monitor your projects usage, you can go to the billing tab in the Reflex Cloud UI on the project page.

Here you can see the current billing and usage for your project.


## Real Life Examples of compute charges on the Pro tier


```md alert
# Single Application - Single Region

Anna, a hobbyist game developer, built a pixel art generator and hosted it on Reflex Cloud so fellow artists could use it anytime. She deployed her app in the San Francisco region, where she lives. If her users use the site for an hour a day, how much would Anna pay?

**Facts:**

- **Machine size:** `c1m1` (1 CPU, 1 GB Memory) - `$0.083` per hour
- **Regions:** `1` (SJC)
- **Avg usage per day per region:** `1 Hour`

**Maths:**

`1 region * 1 hour * 30 days = 30 compute hours`

`30 * 0.083 = 2.49`

(assuming a 30 day month)

Anna's total cost for compute would be `$2.49` for the month. However, since Pro users receive a `$10` credit, her compute cost is fully covered.

**Charge for compute:**

`$0.00 dollars`
```



```md alert
# Single Application - Multi Region

Bob created a social media application and decided to host it on Reflex Cloud. Bob has users in Paris, London, San Jose and Sydney. Bob decided to deploy his application to all those region as well as additional one in Paris since that where Bob lives. If users use the site in each region for 30 minutes a day how much would Bob pay?

**Facts:**

- **Machine size:** `c1m1` (1 CPU, 1 GB Memory) - `$0.083` Cost per hour
- **Regions:** `5` (CDG x 2, LHR x 1, SJC x 1, SYD x 1)
- **Avg usage per day per region:** `0.5 Hours`

**Maths:**

`5 regions * 0.5 hours * 30 days = 75 compute hours` 

`75 * 0.083 = 6.23`

(assuming a 30 day month)

Bob would owe `$6.23` for this month. However since Bob is a pro user they receive a `$10` credit which brings Bob's bill down to `$0`.

**Charge for compute:**

`$0.00 dollars`
```




```md alert
# Single Growing Application - Multi Region

Charlie, a small startup founder, built a finance tracking app that allows users to create and share finance insights in real time. As his user base expanded across different regions, he needed a multi-region setup to reduce latency and improve performance. To ensure a smooth experience, he deployed his app on Reflex Cloud using a `c1m2` machine in four regions.

If users access the app on average for **16 hours per week** in each region, how much would Charlie pay?

**Facts:**
- **Machine size:** `c1m2` (1 CPU, 2 GB Memory) - `$0.157` per hour  
- **Regions:** `4`  
- **Avg usage per week per region:** `16 Hours`

**Maths:**

`4 regions * 16 hours * 4 weeks = 256 compute hours` 

`256 * 0.157 = 40.19`

(assuming 4 weeks in a month)

Charlie would owe `$40.19` for this month. However since Charlie is a pro user they receive a `$10` credit which brings Bob's bill down to `$30.19`.

**Charge for compute:**

`$30.19 dollars`

```



```md alert
# Single Application High-Performance App - Single Region

David, an **AI enthusiast**, developed a **real-time image enhancement tool** that allows photographers to upscale and enhance their images using machine learning. Since his app requires more processing power, he deployed it on a **`c2m2` machine**, which offers increased CPU and memory to handle the intensive AI workloads.  

With users accessing the app **2 hours per day** over a **30-day month**, how much would David pay?

**Facts:**
- **Machine size:** `c2m2` (2 CPU, 2 GB Memory) - `$0.166` per hour  
- **Regions:** `1`  
- **Avg usage per day:** `2 Hours` 


**Maths:**

`1 region * 2 hours * 30 days = 60 compute hours` 

`60 * 0.166 = 9.96`

(assuming a 30 day month)

David would owe `$9.96` for this month. However since David is a pro user they receive a `$10` credit, he will not be charged for compute for this month.

**Charge for compute:**

`$0.00 dollars`

```


```md alert
# Single Fast Scaling App - Multiple Regions 
 
Emily, a **productivity app developer**, built a **real-time team collaboration tool** that helps remote teams manage tasks and communicate efficiently. With users spread across multiple locations, she needed **low-latency performance** to ensure a seamless experience. To achieve this, Emily deployed her app using a `c1m1` machine in **three regions**.  

With users actively using the app **6 hours per day in each region** over a **30-day month**, how much would Emily pay?


**Facts:**
- **Machine size:** `c1m1` (1 CPU, 1 GB Memory) - `$0.083` per hour  
- **Regions:** `3`  
- **Avg usage per day per region:** `6 Hours`


**Maths:**

`3 regions * 6 hours * 30 days = 540 compute hours` 

`540 * 0.083 = 44.82`

(assuming a 30 day month)

Emily would owe `$44.82` for this month. However since Emily is a pro user they receive a `$10` credit which brings Emily's bill down to `$34.82`.

**Charge for compute:**

`$34.82 dollars`

```


```md alert
# Multiple Apps - Multiple Regions 

Fred, a **freelance developer**, built a **portfolio of web applications** that cater to different clients across the globe. He has built **5 apps** where **4 apps** have a small amount of traffic with an average of **0.5 hours a day** and **1 app** that has a high amount of traffic with an average of **6 hours** a day. He has deployed the 4 small traffic apps on a `c1m1` machine in **1 region** each and the high traffic app on a `c1m1` machine in **2 regions**. How much would Fred pay?


**Facts for 4 small traffic apps:**
- **Machine size:** `c1m1` (1 CPU, 1 GB Memory) - `$0.083` per hour  
- **Regions:** `1`  
- **Avg usage per day per region:** `0.5 Hours`


**Facts for 1 large traffic app:**
- **Machine size:** `c1m1` (1 CPU, 1 GB Memory) - `$0.083` per hour  
- **Regions:** `2`  
- **Avg usage per day per region:** `6 Hours`


**Maths:**

4 small traffic apps:

`4 apps * 1 region * 0.5 hours * 30 days = 60 compute hours` 

1 large traffic apps:

`2 regions * 6 hours * 30 days = 360 compute hours` 

Total compute hours = `60 + 360 = 420 compute hours`

`420 * 0.083 = 34.86`

(assuming a 30 day month)

Fred would owe `$34.86` for this month. However since Fred is a pro user they receive a `$10` credit which brings Fred's bill down to `$24.86`.

**Charge for compute:**

`$24.82 dollars`
```

One thing that is important to note is that in the hypothetical example where you have `50 people` using your app `continuously for 24 hours` or if you have `1 person` using your app `continuously for 24 hours`, you `will be charged the same amount` as the charge is based on the amount of time your app up and not the number of users using your app. In `both these examples` your `app is up for 24 hours` and therefore you will be `charged for 24 hours of compute`.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/adding-members.md`:

```md

# Project

A project is a collection of applications (apps / websites).

Every project has its own billing page that are accessible to Admins.



## Adding Team Members

To see the team members of a project click on the `Members` tab in the Cloud UI on the project page. 

If you are a User you have the ability to create, deploy and delete apps, but you do not have the power to add or delete users from that project. You must be an Admin for that.

As an Admin you will see the an `Add user` button in the top right of the screen, as shown in the image below. Clicking on this will allow you to add a user to the project. You will need to enter the email address of the user you wish to add.

```python eval
image_zoom(rx.image(src="/hosting_adding_team_members.png", alt="Adding team members to Reflex Cloud"))
```

```python eval
rx.box(height="20px")
```

```md alert warning
# Currently a User must already have logged in once before they can be added to a project. 
At this time a User must be logged in to be added to a project. In future there will be automatic email invites sent to add new users who have never logged in before.
```


## Other project settings

Clicking on the `Settings` tab in the Cloud UI on the project page allows a user to change the `project name`, check the `project id` and, if the project is not your default project, delete the project.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/logs.md`:

```md

## View Logs

To view the app logs follow the arrow in the image below and press on the `Logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_logs.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to view logs
`reflex cloud apps logs [OPTIONS] [APP_ID]`
```

## View Deployment Logs and Deployment History

To view the deployment history follow the arrow in the image below and press on the `Deployments`.

```python eval
image_zoom(rx.image(src="/view_deployment_logs.webp"))
```

This brings you to the page below where you can see the deployment history of your app. Click on deployment you wish to explore further.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_2.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to view deployment history
`reflex cloud apps history [OPTIONS] [APP_ID]`
```

This brings you to the page below where you can view the deployment logs of your app by clicking the `Build logs` dropdown.

```python eval
image_zoom(rx.image(src="/view_deployment_logs_3.webp"))
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/app-management.md`:

```md

# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform. 

You can deploy an app using the `reflex deploy` command.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.


## Stopping an App

To stop an app follow the arrow in the image below and press on the `Stop app` button. Pausing an app will stop it from running and will not be accessible to users until you resume it. In addition, this will stop you being billed for your app.

```python eval
image_zoom(rx.image(src="/stopping_app.webp", padding_bottom="20px"))
```

```md alert info
# CLI Command to stop an app
`reflex cloud apps stop [OPTIONS] [APP_ID]`
```

## Deleting an App

To delete an app click on the `Settings` tab in the Cloud UI on the app page.

```python eval
image_zoom(rx.image(src="/environment_variables.webp"))
```

Then click on the `Danger` tab as shown below.

```python eval
image_zoom(rx.image(src="/deleting_app.webp"))
```

Here there is a `Delete app` button. Pressing this button will delete the app and all of its data. This action is irreversible.

```md alert info
# CLI Command to delete an app
`reflex cloud apps delete [OPTIONS] [APP_ID]`
```


## Other app settings

Clicking on the `Settings` tab in the Cloud UI on the app page also allows a user to change the `app name`, change the `app description` and check the `app id`.

The other app settings also allows users to edit and add secrets (environment variables) to the app. For more information on secrets, see the [Secrets (Environment Variables)]({hosting.secrets_environment_vars.path}) page.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/tokens.md`:

```md


# Tokens

A token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the `--token` flag. A good use case would be for GitHub actions (you store this token in the secrets).

Tokens are found on the Project List page under the tab `Tokens`. If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below.

```python eval
image_zoom(rx.image(src="/hosting_tokens.png", alt="Adding tokens to Reflex Cloud"))
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/deploy-quick-start.md`:

```md
# Reflex Cloud - Quick Start


So far, we have been running our apps locally on our own machines.
But what if we want to share our apps with the world? This is where
the hosting service comes in.

## Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.

### Prerequisites

1. Hosting service requires `reflex>=0.6.6`.
2. This tutorial assumes you have successfully `reflex init` and `reflex run` your app.
3. Also make sure you have a `requirements.txt` file at the top level app directory that contains all your python dependencies! (To create a `requirements.txt` file, run `pip freeze > requirements.txt`.)


### Authentication

First run the command below to login / signup to your Reflex Cloud account: (command line)

```bash
reflex login
```

You will be redirected to your browser where you can authenticate through Github or Gmail.

### Web UI

Once you are at this URL and you have successfully authenticated, click on the one project you have in your workspace. You should get a screen like this:

```python eval
image_zoom(rx.image(src="/cloud_project_page.png", alt="Reflex Cloud Dashboard"))
```

This screen shows the login command and the deploy command. As we are already logged in, we can skip the login command.

### Deployment

Now you can start deploying your app.

In your cloud UI copy the `reflex deploy` command similar to the one shown below.

```bash
reflex deploy --project 2a432b8f-2605-4753-####-####0cd1####
```

In your project directory (where you would normally run `reflex run`) paste this command.

The command is by default interactive. It asks you a few questions for information required for the deployment.


1. The first question will compare your `requirements.txt` to your python environment and if they are different then it will ask you if you want to update your `requirements.txt` or to continue with the current one. If they are identical this question will not appear. To create a `requirements.txt` file, run `pip freeze > requirements.txt`.
2. The second question will search for a deployed app with the name of your current app, if it does not find one then it will ask if you wish to proceed in deploying your new app.
3. The third question is optional and will ask you for an app description.


That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

```md alert info
# Once your code is uploaded, the hosting service will start the deployment. After a complete upload, exiting from the command **does not** affect the deployment process. The command prints a message when you can safely close it without affecting the deployment.
```

If you go back to the Cloud UI you should be able to see your deployed app and other useful app information.


```md alert info
# Setup a Cloud Config File
To create a `config.yml` file for your app to set your app configuration check out the [Cloud Config Docs]({docs.hosting.config_file.path}).
```

```md alert info
# Moving around the Cloud UI
To go back, i.e. from an app to a project or from a project to your list of projects you just click the `REFLEX logo` in the top left corner of the page.
```

```md alert info
# All flag values are saved between runs
All your flag values, i.e. environment variables or regions or tokens, are saved between runs. This means that if you run a command and you pass a flag value, the next time you run the same command the flag value will be the same as the last time you ran it. This means you should only set the flag values again if you want to change them.
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/machine-types.md`:

```md

## Machine Types


To scale your app you can choose different VMTypes. VMTypes are different configurations of CPU and RAM.

To scale your VM in the Cloud UI, click on the `Settings` tab in the Cloud UI on the app page, and then click on the `Scale` tab as shown below. Clicking on the `Change VM` button will allow you to scale your app.

```python eval
image_zoom(rx.image(src="/scaling_vms.webp", padding_bottom="20px"))
```

### VMTypes in the CLI

To get all the possible VMTypes you can run the following command:

```bash
reflex cloud vmtypes
```

To set which VMType to use when deploying your app you can pass the `--vmtype` flag with the id of the VMType. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --vmtype c2m4
```

This will deploy your app with the `c2m4` VMType, giving your app 2 CPU cores and 4 GB of RAM.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/secrets-environment-vars.md`:

```md

# Secrets (Environment Variables)


## Adding Secrets through the CLI

Below is an example of how to use an environment variable file. You can pass the `--envfile` flag with the path to the env file. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --envfile .env
```

In this example the path to the file is `.env`.


If you prefer to pass the environment variables manually below is deployment command example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --env OPENAI_API_KEY=sk-proj-vD4i9t6U############################
```

They are passed after the `--env` flag as key value pairs. 

To pass multiple environment variables, you can repeat the `--env` tag. i.e. `reflex deploy --project f88b1574-f101-####-####-5f########## --env KEY1=VALUE1 --env KEY2=VALUE`. The `--envfile` flag will override any envs set manually.


```md alert info
# More information on Environment Variables
Environment variables are encrypted and safely stored. We recommend that backend API keys or secrets are entered as `envs`. Make sure to enter the `envs` without any quotation marks. We do not show the values of them in any CLI commands, only their names (or keys).

You access the values of `envs` by referencing `os.environ` with their names as keys in your app's backend. For example, if you set an env `ASYNC_DB_URL`, you are able to access it by `os.environ["ASYNC_DB_URL"]`. Some Python libraries automatically look for certain environment variables. For example, `OPENAI_API_KEY` for the `openai` python client. The `boto3` client credentials can be configured by setting `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`. This information is typically available in the documentation of the Python packages you use.
```

## Adding Secrets through the Cloud UI

To find the secrets tab, click on the `Settings` tab in the Cloud UI on the app page.

```python eval
image_zoom(rx.image(src="/environment_variables.webp"))
```

Then click on the `Secrets` tab as shown below.

```python eval
image_zoom(rx.image(src="/environment_variables_2.webp"))
```

From here you can add or edit your environment variables. You will need to restart your app for these changes to take effect.

This functionality in the UI can be disabled by an admin of the project.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/regions.md`:

```md

## Regions

To scale your app you can choose different regions. Regions are different locations around the world where your app can be deployed. 

To scale your app to multiple regions in the Cloud UI, click on the `Settings` tab in the Cloud UI on the app page, and then click on the `Regions` tab as shown below. Clicking on the `Add new region` button will allow you to scale your app to multiple regions.

```python eval
image_zoom(rx.image(src="/scaling_regions.webp", padding_bottom="20px"))
```

The images below show all the regions that can be deployed in.

```python eval
rx.hstack(
    image_zoom(rx.image(src="/regions_1.webp", padding_bottom="20px")),
    image_zoom(rx.image(src="/regions_2.webp", padding_bottom="20px")),
)
```

### Selecting Regions to Deploy in the CLI

Below is an example of how to deploy your app in several regions:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag (`-r` also works) with the region code. Check out all the regions that we can deploy to below:


## Config File

To create a `config.yml` file for your app run the command below:

```bash
reflex cloud config
```

This will create a yaml file similar to the one below where you can edit the app configuration:

```yaml
name: medo
description: ''
regions:
  sjc: 1
  lhr: 2
vmtype: c1m1
hostname: null
envfile: .env
project: null
packages:
- procps
```


```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/reflex-branding.md`:

```md

# Reflex Branding

Remove Reflex branding from your exported or deployed sites. 

By default, Reflex branding, such as the "Built with Reflex" badge, will appear on all your published sites.


## How to remove the Reflex branding from your app

You can turn off the Reflex branding, when deploying to Reflex Cloud, by adding `show_built_with_reflex=False` to the `rx.Config()` in the `rxconfig.py` file. 

In order for this to work a user hosting with Reflex Cloud must be logged in and on a [paid plan]({pricing_path}) (at least pro tier). 


```md alert info
# A paid plan is required to remove the Reflex branding.
```

If you are self-hosting check out these instructions on [how to remove the Reflex branding from your self-hosted app]({hosting.self_hosting.path}#remove-reflex-branding-from-your-self-hosted-app).

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/hosting/self-hosting.md`:

```md

# Self Hosting

We recommend using `reflex deploy`, but if this does not fit your use case then you can also host your apps yourself.

Clone your code to a server and install the [requirements]({getting_started.installation.path}).

## API URL

Edit your `rxconfig.py` file and set `api_url` to the publicly accessible IP
address or hostname of your server, with the port `:8000` at the end. Setting
this correctly is essential for the frontend to interact with the backend state.

For example if your server is at `app.example.com`, your config would look like this:

```python
config = rx.Config(
    app_name="your_app_name",
    api_url="http://app.example.com:8000",
)
```

It is also possible to set the environment variable `API_URL` at run time or
export time to retain the default for local development.

## Production Mode

Then run your app in production mode:

```bash
reflex run --env prod
```

Production mode creates an optimized build of your app.  By default, the static
frontend of the app (HTML, Javascript, CSS) will be exposed on port `3000` and
the backend (event handlers) will be listening on port `8000`.

```md alert warning
# Reverse Proxy and Websockets
Because the backend uses websockets, some reverse proxy servers, like [nginx](https://nginx.org/en/docs/http/websocket.html) or [apache](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#protoupgrade), must be configured to pass the `Upgrade` header to allow backend connectivity.
```

## Exporting a Static Build

Exporting a static build of the frontend allows the app to be served using a
static hosting provider, like Netlify or Github Pages. Be sure `api_url` is set
to an accessible backend URL when the frontend is exported.

```bash
API_URL=http://app.example.com:8000 reflex export
```

This will create a `frontend.zip` file with your app's minified HTML,
Javascript, and CSS build that can be uploaded to your static hosting service.

It also creates a `backend.zip` file with your app's backend python code to
upload to your server and run.

You can export only the frontend or backend by passing in the `--frontend-only`
or `--backend-only` flags.

It is also possible to export the components without zipping. To do
this, use the `--no-zip` parameter. This provides the frontend in the
`.web/_static/` directory and the backend can be found in the root directory of
the project.

## Reflex Container Service

Another option is to run your Reflex service in a container. For this
purpose, a `Dockerfile` and additional documentation is available in the Reflex
project in the directory `docker-example`.

For the build of the container image it is necessary to edit the `rxconfig.py`
and the add the `requirements.txt`
to your project folder. The following changes are necessary in `rxconfig.py`:

```python
config = rx.Config(
    app_name="app",
    api_url="http://app.example.com:8000",
)
```

Notice that the `api_url` should be set to the externally accessible hostname or
IP, as the client browser must be able to connect to it directly to establish
interactivity.

You can find the `requirements.txt` in the `docker-example` folder of the
project too.

The project structure should looks like this:

```bash
hello
├── .web
├── assets
├── hello
│   ├── __init__.py
│   └── hello.py
├── rxconfig.py
├── Dockerfile
└── requirements.txt
```

After all changes have been made, the container image can now be created as follows.

```bash
docker build -t reflex-project:latest .
```

Finally, you can start your Reflex container service as follows.

```bash
docker run -d -p 3000:3000 -p 8000:8000 --name app reflex-project:latest
```


## Remove Reflex branding from your self-hosted app

To remove the Reflex branding, such as the "Built with Reflex" badge, from your self-hosted app, you must add `show_built_with_reflex=False` to the `rx.Config()` in the `rxconfig.py` file. 


```md alert info
# A paid [team plan]({pricing_path}) is required to remove the Reflex branding for self-hosted apps.
```
```