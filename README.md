## 3.0 Deploying an app to a Swarm
This portion of the tutorial will guide you through the creation and customization of a voting app. It's important that you follow the steps in order, and make sure to customize the portions that are customizable.

**Important.**
To complete this section, you will need to have Docker installed on your machine as mentioned in the [Setup](./setup.md) section. You'll also need to have git installed. There are many options for installing it. For instance, you can get it from [GitHub](https://help.github.com/articles/set-up-git/).

### Voting app
For this application we will use the [Docker Example Voting App](https://github.com/docker/example-voting-app). This app consists of five components:

* Python webapp which lets you vote between two options
* Redis queue which collects new votes
* .NET worker which consumes votes and stores them in…
* Postgres database backed by a Docker volume
* Node.js webapp which shows the results of the voting in real time

Clone the repository onto your machine and `cd` into the directory:

```
git clone https://github.com/docker/example-voting-app.git
cd example-voting-app
```

**THIS IS THE END**
