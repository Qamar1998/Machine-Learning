FROM python:3

# set a directory for the app
WORKDIR /Linear Regression_Pickling

# copy all the files to the container
COPY . /Linear Regression_Pickling

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD [ "python3", "./linear_model.py"]




