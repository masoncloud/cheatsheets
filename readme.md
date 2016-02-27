# LAHacknight Cheat Sheets

Looking for a quick tutorial or have one you'd like to share? Here's the place. 

## Table of Contents

 * [AWS](https://github.com/LAHacknight/cheatsheets/blob/master/aws.md#aws)
     * [Spinning up an EC2 Instance, the Clicky Way](https://github.com/LAHacknight/cheatsheets/blob/master/aws.md#spinning-up-an-ec2-instance-the-clicky-way)
     * [Setting up Route 53 to Host DNS, the Clicky Way](https://github.com/LAHacknight/cheatsheets/blob/master/aws.md#setting-up-route-53-to-host-dns-the-clicky-way)
 * [Bootstrap](https://github.com/LAHacknight/cheatsheets/blob/master/bootstrap.md#bootstrap)
     * [Download a Local Copy](https://github.com/LAHacknight/cheatsheets/blob/master/bootstrap.md#download-a-local-copy)
 * [CalDAV](https://github.com/LAHacknight/cheatsheets/blob/master/caldav.md#caldav)
     * [Server Software](https://github.com/LAHacknight/cheatsheets/blob/master/caldav.md#server-software)
         * [Up and Running on Baikal/Apache in 15 Minutes or so](https://github.com/LAHacknight/cheatsheets/blob/master/caldav.md#up-and-running-on-baikalapache-in-15-minutes-or-so)
 * [Django Configuration](https://github.com/LAHacknight/cheatsheets/blob/master/django-configuration.md#django-configuration)
     * [Disable debug mode providing full tracebacks to visitors](https://github.com/LAHacknight/cheatsheets/blob/master/django-configuration.md#disable-debug-mode-providing-full-tracebacks-to-visitors)
 * [Django Forms](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#django-forms)
     * [Obtain form HTML from form instance](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#obtain-form-html-from-form-instance)
     * [Specify which model a ModelForm applies to](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#specify-which-model-a-modelform-applies-to)
     * [Override ModelForm widget attributes](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#override-modelform-widget-attributes)
     * [Customize error message returned on invalid ModelForm input](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#customize-error-message-returned-on-invalid-modelform-input)
     * [Use form in template](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#use-form-in-template)
     * [Access database object completed form is bound to](https://github.com/LAHacknight/cheatsheets/blob/master/django-forms.md#access-database-object-completed-form-is-bound-to)
 * [Django Installation](https://github.com/LAHacknight/cheatsheets/blob/master/django-installation.md#django-installation)
     * [Install using PIP](https://github.com/LAHacknight/cheatsheets/blob/master/django-installation.md#install-using-pip)
 * [Django Logging](https://github.com/LAHacknight/cheatsheets/blob/master/django-logging.md#django-logging)
     * [Have debug log outputted to the terminal](https://github.com/LAHacknight/cheatsheets/blob/master/django-logging.md#have-debug-log-outputted-to-the-terminal)
 * [Django Magic](https://github.com/LAHacknight/cheatsheets/blob/master/django-magic.md#django-magic)
     * [Because URL definitions belong in the model, said no one ever](https://github.com/LAHacknight/cheatsheets/blob/master/django-magic.md#because-url-definitions-belong-in-the-model-said-no-one-ever)
 * [Django Management](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#django-management)
     * [Create a new Django project](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#create-a-new-django-project)
     * [Create a new Django app](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#create-a-new-django-app)
     * [Create migration scripts](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#create-migration-scripts)
     * [Update database schema](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#update-database-schema)
     * [Start Django development webserver](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#start-django-development-webserver)
     * [Collect all static files and place in STATIC_ROOT directory](https://github.com/LAHacknight/cheatsheets/blob/master/django-management.md#collect-all-static-files-and-place-in-staticroot-directory)
 * [Django Models](https://github.com/LAHacknight/cheatsheets/blob/master/django-models.md#django-models)
     * [Instruct a model to enforce uniqueness across multiple fields](https://github.com/LAHacknight/cheatsheets/blob/master/django-models.md#instruct-a-model-to-enforce-uniqueness-across-multiple-fields)
     * [Instruct a model to enforce uniqueness across several sets](https://github.com/LAHacknight/cheatsheets/blob/master/django-models.md#instruct-a-model-to-enforce-uniqueness-across-several-sets)
     * [Specify field which objects should ordered by](https://github.com/LAHacknight/cheatsheets/blob/master/django-models.md#specify-field-which-objects-should-ordered-by)
 * [Django Production](https://github.com/LAHacknight/cheatsheets/blob/master/django-production.md#django-production)
     * [Using Gunicorn to serve your Django application](https://github.com/LAHacknight/cheatsheets/blob/master/django-production.md#using-gunicorn-to-serve-your-django-application)
     * [Make Gunicorn use Unix domain sockets instead of binding to a TCP port](https://github.com/LAHacknight/cheatsheets/blob/master/django-production.md#make-gunicorn-use-unix-domain-sockets-instead-of-binding-to-a-tcp-port)
 * [Django Templates](https://github.com/LAHacknight/cheatsheets/blob/master/django-templates.md#django-templates)
     * [Concatenate value to argument sent to include](https://github.com/LAHacknight/cheatsheets/blob/master/django-templates.md#concatenate-value-to-argument-sent-to-include)
 * [Django Testing](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#django-testing)
     * [Run all tests](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#run-all-tests)
     * [Running specific tests](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#running-specific-tests)
     * [Verify model raises validation error on invalid value within unit test](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#verify-model-raises-validation-error-on-invalid-value-within-unit-test)
     * [Verify validation when database backend does not support constraint defined in model](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#verify-validation-when-database-backend-does-not-support-constraint-defined-in-model)
     * [Verify form validation](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#verify-form-validation)
     * [Verify page returns correct template](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#verify-page-returns-correct-template)
     * [Verify page uses correct form](https://github.com/LAHacknight/cheatsheets/blob/master/django-testing.md#verify-page-uses-correct-form)
 * [Git](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#git)
     * [Installation](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#installation)
         * [Install Git on Ubuntu/Debian](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#install-git-on-ubuntudebian)
         * [Initialize a Git Repository in the Current Directory](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#initialize-a-git-repository-in-the-current-directory)
         * [Add a Remote Repository Alias](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#add-a-remote-repository-alias)
         * [Clone a Repository Into a Specific Directory](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#clone-a-repository-into-a-specific-directory)
         * [Remove Git Tracking Within a Project](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#remove-git-tracking-within-a-project)
     * [Tagging](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#tagging)
         * [List Available Tags](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#list-available-tags)
         * [Inspect a Tag](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#inspect-a-tag)
         * [Create Annotated Tag](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#create-annotated-tag)
         * [Create Lightweight Tag](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#create-lightweight-tag)
         * [Push Tags to Remote Repo](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#push-tags-to-remote-repo)
     * [Log / History](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#log--history)
         * [View Tidy Text Graph of Git Log](https://github.com/LAHacknight/cheatsheets/blob/master/git.md#view-tidy-text-graph-of-git-log)
 * [GPG](https://github.com/LAHacknight/cheatsheets/blob/master/gpg.md#gpg)
     * [List Keys](https://github.com/LAHacknight/cheatsheets/blob/master/gpg.md#list-keys)
     * [Create a New Key Pair](https://github.com/LAHacknight/cheatsheets/blob/master/gpg.md#create-a-new-key-pair)
 * [Konami](https://github.com/LAHacknight/cheatsheets/blob/master/konami.md#konami)
     * [Konami Code](https://github.com/LAHacknight/cheatsheets/blob/master/konami.md#konami-code)
 * [Mail](https://github.com/LAHacknight/cheatsheets/blob/master/mail.md#mail)
     * [Send message via command line (one-liner)](https://github.com/LAHacknight/cheatsheets/blob/master/mail.md#send-message-via-command-line-one-liner)
 * [Nginx](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#nginx)
     * [Installation](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#installation)
         * [Installing Nginx on Ubuntu/Debian via APT Package](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#installing-nginx-on-ubuntudebian-via-apt-package)
     * [Configuration](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#configuration)
         * [Create Site Configuration Which Proxies to Local Webserver](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#create-site-configuration-which-proxies-to-local-webserver)
         * [Creating a Location Within a Site Which Serves Static Content](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#creating-a-location-within-a-site-which-serves-static-content)
         * [Configure Nginx to Connect Via Unix Domain Sockets](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#configure-nginx-to-connect-via-unix-domain-sockets)
         * [Default Log Location on Ubuntu/Debian](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#default-log-location-on-ubuntudebian)
         * [Verify Current Nginx Configuration is Valid](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#verify-current-nginx-configuration-is-valid)
     * [Usage](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#usage)
         * [Starting Nginx Web Server](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#starting-nginx-web-server)
         * [Reload Nginx Configuration](https://github.com/LAHacknight/cheatsheets/blob/master/nginx.md#reload-nginx-configuration)
 * [PyCharm](https://github.com/LAHacknight/cheatsheets/blob/master/pycharm.md#pycharm)
     * [Mark Subfolder Within Project as Source](https://github.com/LAHacknight/cheatsheets/blob/master/pycharm.md#mark-subfolder-within-project-as-source)
 * [Python Fabric](https://github.com/LAHacknight/cheatsheets/blob/master/python-fabric.md#python-fabric)
     * [Use Context Manager to Allow Run To Warn Only](https://github.com/LAHacknight/cheatsheets/blob/master/python-fabric.md#use-context-manager-to-allow-run-to-warn-only)
     * [Run a collection of commands under sudo](https://github.com/LAHacknight/cheatsheets/blob/master/python-fabric.md#run-a-collection-of-commands-under-sudo)
 * [Python Installation](https://github.com/LAHacknight/cheatsheets/blob/master/python-install.md#python-installation)
     * [Typical Python Installation on Ubuntu/Debian](https://github.com/LAHacknight/cheatsheets/blob/master/python-install.md#typical-python-installation-on-ubuntudebian)
 * [Python Object Oriented Programming](https://github.com/LAHacknight/cheatsheets/blob/master/python-oop.md#python-object-oriented-programming)
     * [Simple Python inheritance and polymorphism example](https://github.com/LAHacknight/cheatsheets/blob/master/python-oop.md#simple-python-inheritance-and-polymorphism-example)
 * [Python Selenium](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#python-selenium)
     * [Initialize Firefox webdriver](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#initialize-firefox-webdriver)
     * [Make a request](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#make-a-request)
     * [Check if value in body](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#check-if-value-in-body)
     * [Set browser window dimensions](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#set-browser-window-dimensions)
     * [Ask selenium to explicitly wait until an element is present](https://github.com/LAHacknight/cheatsheets/blob/master/python-selenium.md#ask-selenium-to-explicitly-wait-until-an-element-is-present)
 * [Python Unittest](https://github.com/LAHacknight/cheatsheets/blob/master/python-unittest.md#python-unittest)
     * [How to temporarily skip a unit test](https://github.com/LAHacknight/cheatsheets/blob/master/python-unittest.md#how-to-temporarily-skip-a-unit-test)
     * [Force a test to fail](https://github.com/LAHacknight/cheatsheets/blob/master/python-unittest.md#force-a-test-to-fail)
     * [Test long strings for equality, show diff output](https://github.com/LAHacknight/cheatsheets/blob/master/python-unittest.md#test-long-strings-for-equality-show-diff-output)
 * [Python Virtual Environment](https://github.com/LAHacknight/cheatsheets/blob/master/python-venv.md#python-virtual-environment)
     * [Create a Virtual Environment](https://github.com/LAHacknight/cheatsheets/blob/master/python-venv.md#create-a-virtual-environment)
     * [Create a Virtual Environment With a Specific Interpreter Version](https://github.com/LAHacknight/cheatsheets/blob/master/python-venv.md#create-a-virtual-environment-with-a-specific-interpreter-version)
     * [Activate a Virtual Environment](https://github.com/LAHacknight/cheatsheets/blob/master/python-venv.md#activate-a-virtual-environment)
     * [Deactivate Current Virtual Environment](https://github.com/LAHacknight/cheatsheets/blob/master/python-venv.md#deactivate-current-virtual-environment)
 * [SSH](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#ssh)
     * [Key Management](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#key-management)
         * [Add an identity to authentication agent](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#add-an-identity-to-authentication-agent)
         * [Remove an identity from authentication agent](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#remove-an-identity-from-authentication-agent)
         * [Remove all identities from authentication agent](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#remove-all-identities-from-authentication-agent)
         * [Obtain and save public key from an existing private key](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#obtain-and-save-public-key-from-an-existing-private-key)
         * [Generating, deploying and using private key for SSH authentication](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#generating-deploying-and-using-private-key-for-ssh-authentication)
         * [Adding user's public key to authorized keys as another user](https://github.com/LAHacknight/cheatsheets/blob/master/ssh.md#adding-users-public-key-to-authorized-keys-as-another-user)
 * [Ubuntu](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#ubuntu)
     * [User Administration](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#user-administration)
         * [Adding a new user, granting sudo, and setting password](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#adding-a-new-user-granting-sudo-and-setting-password)
         * [Allow group to run sudo without providing password](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#allow-group-to-run-sudo-without-providing-password)
     * [System](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#system)
         * [Determine number of processors/cores/sockets on a system](https://github.com/LAHacknight/cheatsheets/blob/master/ubuntu.md#determine-number-of-processorscoressockets-on-a-system)
 * [Upstart](https://github.com/LAHacknight/cheatsheets/blob/master/upstart.md#upstart)
     * [Use upstart to have an app start at system boot](https://github.com/LAHacknight/cheatsheets/blob/master/upstart.md#use-upstart-to-have-an-app-start-at-system-boot)
     * [Determine status of upstart job](https://github.com/LAHacknight/cheatsheets/blob/master/upstart.md#determine-status-of-upstart-job)
