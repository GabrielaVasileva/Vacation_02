1.  project virtual environment
https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html
create:
    conda env create --prefix ./env --file environment.yml --force
update:
    conda env update --prefix ./env --file environment.yml  --prune

To activate this environment, use
      $ conda activate E:\gabi\Python\Vacation_02\env

To deactivate an active environment, use
      $ conda deactivate


2. Setup environment variables
    set FLASK_APP=run.py
2.1. Enable debug
    set FLASK_DEBUG=1

3. Execute the application:
    flask run

4. Get bootstrap starter template from
https://getbootstrap.com/docs/4.3/getting-started/introduction/#starter-template