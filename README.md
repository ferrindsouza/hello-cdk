
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
---

## Troubleshooting Section
### 1. Pip install fails for aws-cdk-lib
Error:
```
ERROR: No matching distribution found for aws-cdk-lib==2.214.0
```

Cause:
You were on an older pip (20.0.2), which didn’t recognize newer CDK versions. The requested version 2.214.0 wasn’t available yet in PyPI.

Solution:
```
# Upgrade pip:

python3 -m pip install --upgrade pip

# Use a valid version of aws-cdk-lib (e.g. 2.183.0, which is currently the latest published). Update requirements.txt:

aws-cdk-lib==2.183.0
constructs>=10.0.0,<11.0.0
```

### 2.  Git push rejected because of private email

Error:
```
remote: error: GH007: Your push would publish a private email address.
```

Cause:
GitHub blocks pushes if you’re using your private email which I did because I didn't do git config with my no-reply email before previous commit.

Solution:
```
# Configure Git to use your GitHub “noreply” email:

git config --global user.email "ferrindsouza@users.noreply.github.com"
```
Or disable email privacy in GitHub settings:
GitHub → Settings → Emails → uncheck “Block command line pushes that expose my email”.
Or run the following command after git config
```
git commit --amend --reset-author
# This changes the last commit to use your current git config (with the no reply email)
```

### 3. CDK bootstrap error: no credentials configured

Error:
```
Need to perform AWS calls for account but no credentials have been configured
```

Cause:
CDK couldn’t find AWS credentials in your WSL environment.

Solution:
If using static keys:
```
aws configure
```
If using AWS IAM Identity Center (SSO) with a profile (e.g., admin):
```
aws sso login --profile admin
export AWS_PROFILE=admin
cdk bootstrap
```

### 4. Python NameError: self is not defined

Error:
```
File "hello_cdk_stack.py", line XX
    self, "HelloWorldFunction",
NameError: name 'self' is not defined
```

Cause:
You placed CDK constructs (like Lambda definitions) at the class level instead of inside the _init_ method. Python doesn’t know what self is outside of methods.

Solution:
Move all constructs inside the _init_ method located in hello_cdk/hello_cdk_stack.py::
```

class HelloCdkStack(Stack):
    def _init_(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super()._init_(scope, construct_id, **kwargs)

        my_function = _lambda.Function(
            self, "HelloWorldFunction",
            runtime=_lambda.Runtime.NODEJS_20_X,
            handler="index.handler",
            code=_lambda.Code.from_inline("..."),
        )
```
---
## Final Output
### 1. Before using cdk diff
<img width="1250" height="177" alt="Screenshot 2025-09-18 131252" src="https://github.com/user-attachments/assets/5a661bf3-e790-4dd4-8670-0e2c94f86c13" />

### 2. After using cdk diff
<img width="1919" height="993" alt="Screenshot 2025-09-18 131059" src="https://github.com/user-attachments/assets/ba1bd688-d97b-494a-8fa1-cd43955f3f52" /> <br>

<img width="1221" height="187" alt="Screenshot 2025-09-18 131310" src="https://github.com/user-attachments/assets/00dd3002-8542-42e5-8ac3-2ded2c058017" />






