# Webpack

### Ask webpack to watch project and perform actions when it detects changes

    webpack -w

### Ask webpack to minify e'rything

    webpack -p

### Install webpack globally

    sudo npm -g install webpack

### Where should the configuration exist?

`webpack.config.js` should be placed in the root directory of the project. 

### Sample configuration for a react project

Assuming you've installed react and react-dom (`npm install react react-dom --save-dev`). And, assuming you've installed babel (`npm install babel-core babel-loader babel-preset-react --save-dev`) and you have your babel presets set in `.babelrc` (example shown below):

    {
        "presents": [
            "react"
        ]
    }

Also assuming you've installed `html-webpack-plugin` so webpack will create a dist index.html based on our existing index.html
(`npm install html-webpack-plugin --save-dev`). We can continue with the following `webpack.config.js` example:

    var HtmlWebpackPlugin = require('html-webpack-plugin');
    var HTMLWebpackPluginConfig = new HtmlWebpackPlugin({
        template: __dirname + '/src/index.html',
        filename: 'index.html',
        inject: 'body'
    });

    module.exports = {
        entry: './src/index.js',
        module: {
            loaders: [
                {test: /\.js$/, include: __dirname + '/src', loader: 'babel-loader'}
            ]
        },
        output: {
            filename: 'bundle.js',
            path: __dirname + '/dist'
        }
    };
    plugins: [HTMLWebpackPluginConfig]

Where:
 * `HTMLWebpackPluginConfig` is an instance of `HtmlWebpackPlugin` with our source `template`, output `filename` and `inject` our bundled js filename into the body.
 * `module.exports` exports this configuration object for webpack to read.
 * `module.exports.entry` is a string pointing to our *root* js file for the app. It may also point to an array of strings for multiple entries.
 * `module.exports.module.loaders` specifies files ending in .js under the directory src should use the babel-loader.
 * `module.exports.output` specified the output js filename and which directory it should put it in.
