# greengrass-pubsub
AWS IOT GreenGrass Pub Sub

## Commands

### Install gdk

``` 
python3 -m venv path/to/venv

source path/to/venv/bin/activate

python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
```

### To initilase the project/component
```
gdk component init -l python -n first-comp -t HelloWorld 
```

### To build the project/component
```
gdk component build
```

### Publish teh project/component to S3
```
gdk component publish
```