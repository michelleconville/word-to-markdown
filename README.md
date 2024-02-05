# word-to-markdown
A django word to markdown converter

## Installing pandoc in Gitpod

In Gitpod, you can install Pandoc within your workspace without needing to install it on your local computer. Gitpod provides an online development environment where you can install and use software tools like Pandoc directly within the workspace.

Steps
1. Open your Gitpod workspace where your Django project is located.
2. Run the following command in the terminal within Gitpod  to install Pandoc:

   ```
   sudo apt update
   sudo apt install pandoc
   ```
This command updates the package index and then installs Pandoc on the Gitpod workspace.

3. After installation, you can verify that Pandoc is installed by running:

   ```
   pandoc --version
   ```

This command should display the version of Pandoc installed in your Gitpod workspace.


You can now use Pandoc within your Django application to convert documents to different formats, including Word to Markdown. Ensure that your Django views are configured to call Pandoc using the `subprocess` module or similar methods.

You can leverage Pandoc within your Gitpod workspace to perform document conversions without needing to install it on your local computer. This may need to be re-installed everytime you open your workspace.
