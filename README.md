# Getting Started with Langman
This repo contains the ful-stack web application Langman which is based on a python server running Flask, Gunicorn, SQLAlchemy etc., and a React client connected via a REST API.

# Server
## Environment
Create a python virtual environment.

Install the [requirements.txt]: `pip install -r requirements.txt`.

## Database
Postgres will need to be installed and setup appropriately.

If using postgres and not sqlite, check postgres is running: `service postgresql status`.

Need to ensure [Usages] table is populated:

Download the [usages.csv] file and place it in the [langman/data] directory.

Ensure [FLASK_ENV] is set appropriately (`export FLASK_ENV='dev_lite'` or `export FLASK_ENV='dev_postgres'`).
Ensure [FLASK_APP] is set to [server.prepare_orm] (`export FLASK_APP='server.prepare_orm'`)

Then run `flask init-db` to populate the db.

## Running
Set the environment variables required by Flask:
* The app - `export FLASK_APP='server.app'`
* The environment, as documented above in db section.
See [server/config.yaml] for supported environments.

Then run `run flask` to run the server in dev mode at [http://localhost:5000] (gunicorn is used instead in production).

# Client
Standard Create React App blurb...

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the [/client] directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Storybook
`npm run storybook` in the [client/] directory to see the storybook full of components, screens etc. - acts as documentation and testing.

`npm run build-storybook` to compile it to static files.

## Docs
Docs use sphinx. Run `make build html` in the [server/docs] directory to recompile.

# Issues
1. No real error handling when server is down or otherwise not responding.
2. No notification to the user that something is happening while they wait for the server - problematic if slow.
3. Page doesn't load until response is recieved so repeadtedly clicking buttons could lead to multiple games being created or multiple letter guesses.
4. The size of the app screen changes depending on the content being shown...
5. The winning animation appears to restart.
6. There is no way fo rplayers to review historic wins and losses.
7. The subtitle was left off other screens to allow more space but it would probably be added.