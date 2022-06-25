## MachineLearningProject

### Software and Account Requirement.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)

creating  conda environment 
```
conda create -p venv python==3.7 -y   (p present dirc)
```
To activate the environment
```
conda activate venv/
```
OR
```
conda activate venv
```

```
git log
```

```
git add <file_name>
```

Note : to ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all the version maintained by git
```
git log
```

To create the version/commit all the changes by git 
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```

To check remote url 

```
git remote -v
```
To check the updated repo 

```
git diff
```
To setup CI/CD pipeline in heroku we need 3 information
```
HEROKU_EMAIL = arunchaudhary6552@gmail.com
HEROKU_API_KEY = 730c82f4-002a-4123-a9f1-c950a606a260
HEROKU_APP_NAME = mlprojectregression
```

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
> Note: Image name for docker must be lowercase
```


To list docker image

```
docker images
```

Run docker images

```
docker run -p 5000:5000 -e PORT=5000 
```

To check running container in docker

```
docker ps
```
To stop the Docker container

```
docker stop <container_id>
```

```
python setup.py install
```

```
python install -r requirements.txt
```

```
python install -e . 
```


```
pip install ipykernal
```